import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def sandbox(tmp_path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "python3").symlink_to(sys.executable)
    calls = tmp_path / "calls.jsonl"
    (bin_dir / "curl").write_text("#!/usr/bin/env python3\nimport json, os, sys\np=os.environ['CALL_LOG']\nwith open(p, 'a') as f: f.write(json.dumps(sys.argv[1:])+'\\n')\nn=len(open(p).readlines())\nprint(json.dumps({'ok': n>1 if os.environ.get('REJECT_FIRST') else True}))\n")
    (bin_dir / "curl").chmod(0o755)
    env = {"HOME": str(tmp_path), "PATH": str(bin_dir) + ":/usr/bin:/bin", "CALL_LOG": str(calls)}
    return tmp_path, bin_dir, calls, env


def run(script, args, env):
    return subprocess.run(["/bin/bash", str(ROOT / script), *args], env=env, capture_output=True, text=True)


def test_timer_and_disk_failures_emit_mocked_alerts(sandbox):
    home, bin_dir, calls, env = sandbox
    commands = {"systemctl": "#!/bin/bash\nif [[ $* == *list-timers* ]]; then echo present.timer; fi\n", "df": "#!/bin/bash\nprintf 'Filesystem Size Used Avail Use%% Mounted\nmock 100 90 10 90%% /\n'\n", "claude": "#!/bin/bash\necho mock-auth-ok\n", "timeout": "#!/bin/bash\nshift\nexec \"$@\"\n"}
    for name, text in commands.items():
        path = bin_dir / name
        path.write_text(text)
        path.chmod(0o755)
    timers = home / "timers.txt"
    timers.write_text("missing.timer\n")
    env.update(TELEGRAM_BOT_TOKEN="demo", TELEGRAM_CHAT_ID="demo-chat", WATCHDOG_TIMERS=str(timers))
    result = run("watchdog", [], env)
    assert result.returncode == 0, result.stderr
    requests = [json.loads(line) for line in calls.read_text().splitlines()]
    assert len(requests) == 2
    payloads = [json.loads(args[args.index("-d") + 1]) for args in requests]
    assert "missing.timer" in payloads[0]["text"]
    assert "90%" in payloads[1]["text"]


def test_missing_configuration_sends_nothing(sandbox):
    _, _, calls, env = sandbox
    assert run("watchdog", [], env).returncode == 1
    assert not calls.exists()
