import os
import sqlite3
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def database(tmp_path):
    path = tmp_path / "Library/Messages/chat.db"
    path.parent.mkdir(parents=True)
    db = sqlite3.connect(path)
    db.executescript("CREATE TABLE message(text TEXT, attributedBody BLOB, date INTEGER, is_from_me INTEGER); CREATE TABLE chat(chat_identifier TEXT); CREATE TABLE chat_message_join(message_id INTEGER, chat_id INTEGER);")
    db.execute("INSERT INTO chat VALUES (?)", ("demo-contact",))
    db.execute("INSERT INTO message VALUES (?, NULL, ?, 0)", ("Synthetic message", 1_000_000_000))
    db.execute("INSERT INTO chat_message_join VALUES (1, 1)")
    db.commit()
    db.close()
    return path


def invoke(tmp_path, phone, limit="20"):
    env = {"HOME": str(tmp_path), "PATH": os.environ["PATH"]}
    return subprocess.run(["bash", str(ROOT / "imessage-pull"), phone, limit], env=env, capture_output=True, text=True)


def test_synthetic_database_read(tmp_path):
    database(tmp_path)
    result = invoke(tmp_path, "demo-contact")
    assert result.returncode == 0, result.stderr
    assert "Synthetic message" in result.stdout


def test_contact_is_bound_as_data(tmp_path):
    database(tmp_path)
    result = invoke(tmp_path, "' OR 1=1 --")
    assert result.returncode == 0, result.stderr
    assert "Synthetic message" not in result.stdout


def test_limit_must_be_positive_integer(tmp_path):
    database(tmp_path)
    result = invoke(tmp_path, "demo-contact", "-1")
    assert result.returncode != 0
    assert "positive integer" in result.stderr


def test_contact_cannot_inject_python(tmp_path):
    database(tmp_path)
    marker = tmp_path / "marker"
    payload = '\"); __import__("pathlib").Path(' + repr(str(marker)) + ').touch(); #'
    result = invoke(tmp_path, payload)
    assert result.returncode == 0, result.stderr
    assert not marker.exists()


def test_contact_wildcards_are_literal(tmp_path):
    database(tmp_path)
    result = invoke(tmp_path, "%")
    assert result.returncode == 0, result.stderr
    assert "Synthetic message" not in result.stdout
