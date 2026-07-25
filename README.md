# tg-notify

A shell notification sender with a plain-text retry path.

## Principle cluster

This repository demonstrates **P10 (production means persistence, bounded autonomy, and observability)** because it encodes message text as JSON and retries without formatting when the first response is rejected.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./tg-notify "recipient" "Build complete."
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
