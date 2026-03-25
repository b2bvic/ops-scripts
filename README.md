# tg-notify

Self-healing Telegram notification sender. Tries Markdown, falls back to plain text. Logs failures instead of swallowing them.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
export TELEGRAM_BOT_TOKEN="your-bot-token"
tg-notify 123456789 "Deploy complete. *All services green.*"
```

If Telegram rejects the Markdown (unmatched `*`, `_`, etc.), it automatically retries as plain text. Both attempts logged if failed.

## Install

```bash
curl -o ~/.local/bin/tg-notify https://raw.githubusercontent.com/b2bvic/tg-notify/main/tg-notify
chmod +x ~/.local/bin/tg-notify
```

## Token Sources

1. `TELEGRAM_BOT_TOKEN` environment variable
2. `~/.env.automation` file (auto-sourced if env var missing)

## License

MIT
