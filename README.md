# twitter-bookmarks

Capture your Twitter/X bookmarks to local markdown files. Reads Chrome cookies directly (no browser extension), polls the GraphQL API, classifies by topic, writes structured markdown.

Built by [Victor Valentine Romo](https://victorvalentineromo.com) at [Scale With Search](https://scalewithsearch.com).

## What It Does

1. Decrypts Chrome's cookie database (macOS Keychain integration)
2. Authenticates to Twitter's internal GraphQL Bookmarks endpoint
3. Diffs against previously seen bookmark IDs
4. Classifies each bookmark by keyword matching (tech, marketing, personal — configurable)
5. Writes markdown files with tweet text, author, URL, timestamps, and domain classification

## Usage

```bash
twitter-bookmarks                    # Pull new bookmarks
twitter-bookmarks --limit 50         # Pull up to 50
twitter-bookmarks --dry-run          # See what would be captured
```

## Install

```bash
git clone https://github.com/b2bvic/twitter-bookmarks.git
cd twitter-bookmarks
pip install cryptography requests    # Only two dependencies
```

## Configuration

### Output directory

```bash
export BOOKMARKS_OUTPUT=~/my-bookmarks
```

Default: `~/twitter-bookmarks/`

### Custom domain classification

Create `~/.config/twitter-bookmarks/domains.json`:

```json
{
  "ai": ["claude", "openai", "llm", "prompt", "agent"],
  "web": ["react", "css", "javascript", "frontend"],
  "business": ["saas", "pricing", "startup", "revenue"]
}
```

## How It Works

### Chrome Cookie Decryption

macOS Chrome encrypts cookies with a key stored in Keychain under "Chrome Safe Storage". This script:

1. Retrieves the encryption key via `security find-generic-password`
2. Derives the AES key using PBKDF2 (1003 iterations, SHA1)
3. Decrypts the `auth_token` cookie from Chrome's SQLite database
4. No browser extension needed, no OAuth app needed

### GraphQL API

Uses Twitter's internal `Bookmarks` query (the same one twitter.com uses). Requires an active logged-in session in Chrome — no API keys or developer account needed.

## Requirements

- macOS (Chrome cookie decryption uses Keychain)
- Chrome with an active Twitter/X login
- Python 3.9+
- `cryptography` and `requests` packages

## License

MIT
