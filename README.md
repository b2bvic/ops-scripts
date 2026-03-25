# watchdog

VPS health monitor with Telegram alerts. Checks systemd timers, failed services, disk usage, Syncthing peers, and Claude Code auth status.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## What It Checks

| Check | Alert When |
|-------|-----------|
| Systemd timers | Expected timer missing from `list-timers` |
| Failed services | Any `--user` service in failed state |
| Disk usage | Root partition exceeds threshold (default 80%) |
| Syncthing peer | No connected peers for >1 hour |
| Claude Code auth | Token expired or `claude -p` failing |

## Install

```bash
curl -o ~/.local/bin/watchdog https://raw.githubusercontent.com/b2bvic/watchdog/main/watchdog
chmod +x ~/.local/bin/watchdog
```

## Usage

```bash
# Run once
watchdog

# Run hourly via cron
0 * * * * ~/.local/bin/watchdog
```

## Configuration

### Environment variables

```bash
export TELEGRAM_BOT_TOKEN="your-bot-token"
export TELEGRAM_CHAT_ID="your-chat-id"
export WATCHDOG_DISK_THRESHOLD=80          # Optional, default 80%
export SYNCTHING_API_KEY="your-api-key"    # Optional, enables sync check
```

Or source from `~/.env.automation`.

### Timer watchlist

Create `~/.config/watchdog/timers.txt` with one timer name per line:

```
my-backup
daily-report
sync-service
```

Lines starting with `#` are ignored. If no file exists, timer check is skipped.

## License

MIT
