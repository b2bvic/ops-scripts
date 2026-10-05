# Linux host health checker: watchdog

Watchdog inspects Linux host health for system operators. Use configured timer and disk checks to identify conditions that need review.

[Project page](https://scalewithsearch.com/code/watchdog)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/watchdog
cd watchdog
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## How it works

- Check configured user-systemd timers and failed services.
- Compare root filesystem usage with a configured threshold.
- Send Telegram alerts with caller-supplied credentials.

## Limits

- A run can send alerts and write logs.
- Tests replace host commands and HTTP calls with fixtures.
- The optional authentication probe classifies specific error text rather than proving complete service health.
- The timer file uses WATCHDOG_TIMERS; the documented legacy --config argument is not implemented.

## Related repositories

- [tg-notify](https://github.com/b2bvic/tg-notify)
- [social-poster](https://github.com/b2bvic/social-poster)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
