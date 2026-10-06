import pytest


def test_classification_and_fallback(tool):
    assert tool.classify_bookmark({"text": "python github api"})[0] == "tech"
    assert tool.classify_bookmark({"text": "unmatched words"}) == ("GENERAL", {"GENERAL": 0.5})


def test_implementation_score_is_bounded(tool):
    tweet = {"text": "github.com tutorial api setup", "bookmarks": 101, "likes": 1001}
    assert tool.score_implementation(tweet) == 1
    assert tool.score_implementation({"text": ""}) == 0


def test_cookie_values_are_not_printed(tool, monkeypatch, capsys):
    monkeypatch.setattr(tool, "X_BEARER_TOKEN", "demo")
    monkeypatch.setattr(tool, "get_twitter_cookies", lambda: {"auth_token": "AUTH_SECRET_MARKER", "ct0": "CSRF_SECRET_MARKER"})
    monkeypatch.setattr(tool, "fetch_bookmarks", lambda cookies, limit: [])
    monkeypatch.setattr(tool.sys, "argv", ["twitter-bookmarks", "--dry-run"])
    with pytest.raises(SystemExit) as result:
        tool.main()
    assert result.value.code == 0
    output = capsys.readouterr().out
    assert "MARKER" not in output
    assert "CSRF_SEC" not in output
    assert "Authenticated cookies found." in output
