# X bookmarks to Markdown importer: twitter-bookmarks

`twitter-bookmarks` imports saved X posts for researchers and content teams. Use classified Markdown records to retain social research in files you control.

[Project page](https://scalewithsearch.com/code/twitter-bookmarks)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/twitter-bookmarks
cd twitter-bookmarks
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python twitter-bookmarks --help
.venv/bin/python -m pytest -q
```

## How it works

- Read configured browser cookie storage on macOS when capture is requested.
- Fetch bookmark records through the configured X web API endpoint.
- Write Markdown and track seen identifiers; optionally call a configured webhook.

## Limits

- Capture depends on browser storage, Keychain access, and an unstable web API.
- Dry-run still authenticates and fetches bookmarks.
- Classification scores are keyword heuristics.
- Protect output files and credentials separately.

## Related repositories

- [web2md](https://github.com/b2bvic/web2md)
- [sws-skills](https://github.com/b2bvic/sws-skills)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 twitter-bookmarks tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
