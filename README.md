# ops-scripts

Five operator scripts, each one file: `tg-notify` sends a Telegram message with a plain-text retry, `watchdog` checks a Linux host and alerts on Telegram, `imessage-pull` reads recent macOS Messages for one contact, `twitter-bookmarks` saves your X bookmarks as Markdown, and `blitz-poster` publishes a dated X queue.
Each script has pytest coverage that uses fixtures and mocked HTTP, so you can run the tests before you give it a credential.

[Project page](https://scalewithsearch.com/code/ops-scripts)

Three of these scripts read personal data or make live writes. The table below says which, and every component README repeats it.

## Quick start

Use Python 3.11 or later and Bash. Host checks need Linux with systemd. The macOS readers need Full Disk Access or Keychain access.

```bash
git clone https://github.com/b2bvic/ops-scripts.git
cd ops-scripts
python3 -m venv .venv
.venv/bin/python -m pip install -r components/tg-notify/requirements-dev.txt -r components/twitter-bookmarks/requirements-dev.txt
for component in tg-notify watchdog imessage-pull twitter-bookmarks social-poster; do
  (cd "components/$component" && ../../.venv/bin/python -m pytest -q)
done
.venv/bin/python components/twitter-bookmarks/twitter-bookmarks --help
```

The 18 tests read no Messages database, no browser cookies, and publish nothing.
There is no root test runner or root CI workflow; each component folder keeps its own.

Send a live Telegram message once the tests pass:

```bash
export TELEGRAM_BOT_TOKEN="<bot-token>"
components/tg-notify/tg-notify "<chat-id>" "Build complete."
```

## Components

| Component | Reads personal data | Live writes |
| --- | --- | --- |
| [tg-notify](#tg-notify) | Caller message text and bot token | Sends a Telegram message; appends `~/logs/tg-notify.log` on failure |
| [watchdog](#watchdog) | Host state and configured credentials | Sends Telegram alerts; writes logs and peer state |
| [imessage-pull](#imessage-pull) | `~/Library/Messages/chat.db`, read-only: contact identifiers and message bodies | Prints private conversations to stdout |
| [twitter-bookmarks](#twitter-bookmarks) | Chrome cookies, the Chrome Safe Storage key in Keychain, and your saved X posts | Writes Markdown and seen IDs; `--notify` POSTs records to `BOOKMARK_WEBHOOK_URL` |
| [social-poster](#social-poster) | X credentials, queued post files, posting history | `post-twitter` and `blitz-poster` publish to X and update queue, history, and error logs |

<a id="tg-notify"></a>

## tg-notify

`tg-notify <chat-id> <message>` sends through the Telegram Bot API with Markdown parse mode, then retries as plain text when Telegram rejects the formatting.
It reads `TELEGRAM_BOT_TOKEN` from the environment or from `~/.env.automation`. A configured call sends a live message, and the failure log can contain message text and API responses. [README](components/tg-notify/README.md)

<a id="watchdog"></a>

## watchdog

`watchdog` checks the user-systemd timers listed in `WATCHDOG_TIMERS`, failed services, root disk usage against `WATCHDOG_DISK_THRESHOLD` (default 80 percent), Syncthing peers when `SYNCTHING_API_KEY` is set, and Claude CLI authentication when `claude` is on the PATH.
Each finding sends one Telegram alert through `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID`. The Claude probe runs `claude -p` and can use account capacity. The legacy `--config` argument is not implemented. [README](components/watchdog/README.md)

<a id="imessage-pull"></a>

## imessage-pull

`imessage-pull 5551234567 20` prints the last 20 messages whose chat identifier contains the substring, from the local Messages database opened with `mode=ro`.
Give your terminal Full Disk Access first. Output contains private conversations; protect anything you redirect to a file. [README](components/imessage-pull/README.md)

<a id="twitter-bookmarks"></a>

## twitter-bookmarks

`twitter-bookmarks` decrypts Chrome's cookie store with the Safe Storage key from Keychain, fetches your bookmarks from the X web API with `TWITTER_BEARER_TOKEN`, classifies each post by keyword score, writes Markdown records and an index under `BOOKMARKS_OUTPUT`, and tracks seen IDs in its cache directory.
`--dry-run` still reads credentials and fetches bookmarks; it skips the writes. `--notify` sends new records to `BOOKMARK_WEBHOOK_URL` by HTTP POST. The web API is unofficial and can change. This script does not publish posts. [README](components/twitter-bookmarks/README.md)

<a id="social-poster"></a>

## social-poster

`blitz-poster --dry-run` lists today's pending items from `~/.cache/social-auto/blitz-queue.jsonl` and shows the first five lines of each content file. Without `--dry-run` it publishes every eligible item and marks it posted.
`post-twitter "text"` and `post-twitter --thread "Post 1" "Post 2"` publish at once with no preview. Both read `~/.cache/social-auto/twitter-credentials.json`. Set `SOCIAL_POSTER_ROOT` when content paths use a different base directory. `post-linkedin` is retired and exits without an API call. [README](components/social-poster/README.md)

## Privacy and history

Component histories were imported with Git subtree merges without squashing.
Older `twitter-bookmarks` commits retain an X web-client bearer token and a VPS webhook address. Older commit metadata retains personal email addresses and local hostnames, and earlier READMEs contain message and post examples.
Review the history before you fork this repository for a team.

## Model assistance

Each component README carries this disclosure:

> This 2026 README refit used model assistance.
>
> No claim is made about how the underlying code was authored or reviewed.

This rollup README was written with Codex assistance.

## License

All five components use the MIT license. The root [LICENSE](LICENSE) and each component license keep the copyright notice.
