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


def test_markdown_rejection_retries_plain_text(sandbox):
    home, _, calls, env = sandbox
    env.update(TELEGRAM_BOT_TOKEN="demo", REJECT_FIRST="1")
    result = run("tg-notify", ["demo-chat", 'Quoted "text"\nnext'], env)
    assert result.returncode == 0, result.stderr
    requests = [json.loads(line) for line in calls.read_text().splitlines()]
    payloads = [json.loads(args[args.index("-d") + 1]) for args in requests]
    assert len(payloads) == 2
    assert payloads[0]["parse_mode"] == "Markdown"
    assert "parse_mode" not in payloads[1]
    assert payloads[1]["text"] == 'Quoted "text"\nnext'


def test_missing_token_sends_nothing(sandbox):
    _, _, calls, env = sandbox
    result = run("tg-notify", ["demo-chat", "Test"], env)
    assert result.returncode == 1
    assert not calls.exists()
