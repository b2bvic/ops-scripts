# Linux host health checker: watchdog

`watchdog` inspects Linux host health for system operators. Use configured timer and disk checks to identify conditions that need review.

[Project page](https://scalewithsearch.com/code/ops-scripts#watchdog)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/ops-scripts
cd ops-scripts/components/watchdog
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## Usage

Set the Telegram credentials before a run. List one expected timer name on each line of the timers file.

```bash
export TELEGRAM_BOT_TOKEN="<bot-token>"
export TELEGRAM_CHAT_ID="<chat-id>"
WATCHDOG_TIMERS=~/.config/watchdog/timers.txt ./watchdog
```

A run sends one Telegram alert for each issue it finds. Optional variables are `WATCHDOG_DISK_THRESHOLD` (default 80) and `SYNCTHING_API_KEY`.

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

## Model assistance

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
