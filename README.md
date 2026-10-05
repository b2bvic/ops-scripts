# Telegram notification shell script: tg-notify

Tg-notify sends Telegram bot messages for system operators. Use its formatting retry to handle an API rejection of a Markdown message.

[Project page](https://scalewithsearch.com/code/tg-notify)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/tg-notify
cd tg-notify
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## How it works

- JSON-encode message text before sending it.
- Retry without a parse mode after an API rejection.
- Log rejected attempts and return failure when both API responses are rejected.

## Limits

- Invocation sends a live message when credentials are available.
- A retry does not guarantee delivery.
- Transport failures can exit before the formatting retry.
- Logs can contain message text and API response details.

## Related repositories

- [watchdog](https://github.com/b2bvic/watchdog)
- [social-poster](https://github.com/b2bvic/social-poster)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
