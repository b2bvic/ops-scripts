# imessage-pull

Pull iMessage history from any contact. Reads the macOS Messages SQLite database directly, including NSArchiver-encoded rich text blobs.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## Usage

```bash
imessage-pull 5551234567        # Last 20 messages
imessage-pull 5551234567 50     # Last 50 messages
```

## Output

```
--- Messages with 5551234567 (last 20) ---

2026-03-25 14:22:01 | Them: Hey are you free tomorrow?
2026-03-25 14:23:15 | You: Yeah after 2pm works
2026-03-25 14:23:45 | Them: Perfect, let's grab coffee
```

## How It Works

macOS stores iMessages in `~/Library/Messages/chat.db` (SQLite). Modern messages use NSArchiver-encoded `attributedBody` blobs instead of plain `text` fields. This script handles both:

1. Plain text messages: read directly
2. NSArchiver blobs: decode Latin-1, regex-extract readable text, filter NSObject class noise, return the longest clean run

## Requirements

- macOS only
- Full Disk Access for Terminal/iTerm2 (System Settings > Privacy & Security > Full Disk Access)
- Python 3 (included with macOS)

## Install

```bash
curl -o ~/.local/bin/imessage-pull https://raw.githubusercontent.com/b2bvic/imessage-pull/main/imessage-pull
chmod +x ~/.local/bin/imessage-pull
```

## License

MIT
