# watchdog

A shell health checker that records system conditions and emits remote alerts.

## Principle cluster

This repository demonstrates **P10 (production means persistence, bounded autonomy, and observability)** because it reads a configured check list, reports missing entries, and evaluates disk usage.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
WATCHDOG_TIMERS=~/.config/watchdog/timers.txt ./watchdog
```

The expected-timer list comes from `WATCHDOG_TIMERS` (default `~/.config/watchdog/timers.txt`). The script requires the two Telegram credential variables it names in its header and posts alerts through them.

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
