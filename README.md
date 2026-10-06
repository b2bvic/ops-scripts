# ops-scripts

Use these scripts to send alerts, check Linux hosts, export personal records, and automate X workflows.

[Project page](https://scalewithsearch.com/code/ops-scripts)

## Install

Use Python 3.11 or later and Bash. Host checks need Linux and systemd. Personal-data readers need macOS permissions.

```bash
gh repo clone b2bvic/ops-scripts
cd ops-scripts
python3 -m venv .venv
.venv/bin/python -m pip install -r components/tg-notify/requirements-dev.txt
.venv/bin/python -m pip install -r components/twitter-bookmarks/requirements-dev.txt
```

Install runtime dependencies for X bookmark capture with `requests` and `cryptography` from its requirements file.
Shell scripts use `python3` and `curl` from your PATH. Activate your environment before running them.

## Quick start

Run the portable component tests before configuring credentials:

```bash
source .venv/bin/activate
for component in tg-notify watchdog imessage-pull twitter-bookmarks social-poster; do
  (cd "components/$component" && python -m pytest -q)
done
python components/twitter-bookmarks/twitter-bookmarks --help
```

Tests use synthetic records, temporary directories, and mocked HTTP calls.
They do not read your Messages database or browser cookies and do not publish posts.
No root test runner or root CI workflow is supplied. Component workflows remain in their imported folders.

## Components

| Job | Component | Reads personal data | Live writes |
| --- | --- | --- | --- |
| Alerts and host checks | [tg-notify](#tg-notify) | Caller message text and bot credentials | Sends Telegram messages; writes failure logs |
| Alerts and host checks | [watchdog](#watchdog) | Host state and configured credentials | Sends Telegram alerts; writes logs and peer state |
| Personal data export | [imessage-pull](#imessage-pull) | Local Messages database, contact identifiers, and message bodies | Prints private conversations; database access is read-only |
| X automation | [twitter-bookmarks](#twitter-bookmarks) | Chrome cookies, Keychain key, and saved X posts with author handles | Writes Markdown and seen IDs; `--notify` posts records to a configured webhook |
| X automation | [social-poster](#social-poster) | X credentials, queued post files, and posting history | `post-twitter` and `blitz-poster` publish to X; update queue, history, and error logs |

## Alerts and host checks

<a id="tg-notify"></a>
### tg-notify

Send Telegram bot messages with a plain-text retry after a formatting rejection.
A configured invocation sends a live message. Failure logs can contain message previews and API responses.

Supply `TELEGRAM_BOT_TOKEN` and the intended chat identifier only when you intend to send.
See [tg-notify documentation](components/tg-notify/README.md).

<a id="watchdog"></a>
### watchdog

Check user-systemd timers, failed services, root disk usage, optional Syncthing peers, and optional Claude authentication.
A run sends Telegram alerts for detected issues and writes local logs and peer state.
The optional Claude probe invokes a live model command and can use account capacity.

Configure `WATCHDOG_TIMERS`, `TELEGRAM_BOT_TOKEN`, and `TELEGRAM_CHAT_ID` before a host run.
The legacy `--config` argument does not configure the timer file.
See [watchdog documentation](components/watchdog/README.md).

## Personal data export

<a id="imessage-pull"></a>
### imessage-pull

Read recent conversations from your local macOS Messages SQLite database using a contact identifier substring.
Database access is read-only. Output contains contact identifiers, timestamps, and private message bodies.

Give your terminal Full Disk Access before using your real database.
Protect terminal output and any redirected exports.
See [imessage-pull documentation](components/imessage-pull/README.md).

## X automation

<a id="twitter-bookmarks"></a>
### twitter-bookmarks

Read Chrome cookies and its Keychain storage key to authenticate a bookmark fetch.
Classify saved posts and write Markdown records, an index, and seen identifiers.
These records contain post text, author handles, and your bookmark selections.

Supply `TWITTER_BEARER_TOKEN` through your environment. Configure `BOOKMARKS_OUTPUT` for exports.
`--dry-run` still reads credentials and fetches bookmarks; it can create its cache directory.
`--notify` sends bookmark records to `BOOKMARK_WEBHOOK_URL` through an HTTP POST.
This component does not publish X posts.
See [twitter-bookmarks documentation](components/twitter-bookmarks/README.md).

<a id="social-poster"></a>
### social-poster

Preview queued content with `blitz-poster --dry-run`.
The preview displays only five lines. Read the complete content file before publishing.

`post-twitter` immediately posts to X. `blitz-poster` publishes eligible queue items unless you pass `--dry-run`.
Both read X credentials from `~/.cache/social-auto/twitter-credentials.json`.
The queue uses `~/.cache/social-auto/blitz-queue.jsonl`; successful runs update queue status and posting history.
Set `SOCIAL_POSTER_ROOT` when queued content paths use a different base directory.
`post-linkedin` is retired and exits without an API call.
See [social-poster documentation](components/social-poster/README.md).

## Privacy and history

Full source histories are preserved through subtree imports without squash.
Older `twitter-bookmarks` commits retain an X web-client bearer token and a VPS webhook address.
Earlier READMEs also contain message and post examples whose origins need review.
Older commit metadata also retains personal email addresses and local hostnames.
The packet privacy report lists each finding by commit, path, and line with credential values redacted.
Review that report before publishing this repository. No history is rewritten by this rollup.

## Model assistance

Each component's earlier README contains this disclosure, retained in its component documentation:

> This 2026 README refit used model assistance.
>
> No claim is made about how the underlying code was authored or reviewed.

The rollup documentation uses Codex assistance.

## License

All five components use the MIT license. The root [LICENSE](LICENSE) and each component license retain the copyright notice.
