# MacOS iMessage history reader: imessage-pull

Imessage-pull reads local message records for macOS users. Use a contact lookup to inspect recent Messages history without exporting the entire database.

[Project page](https://scalewithsearch.com/code/imessage-pull)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/imessage-pull
cd imessage-pull
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## How it works

- Open the Messages SQLite database in read-only mode.
- Bind the contact substring and positive message limit as SQL parameters.
- Print plain text and heuristically recover attributed message bodies.

## Limits

- The terminal needs permission to read the Messages database.
- Contact matching uses a literal substring rather than a resolved contact identity.
- Attributed-body recovery can omit text or return attachment placeholders.
- Output can contain private conversations.

## Related repositories

- [web2md](https://github.com/b2bvic/web2md)
- [twitter-bookmarks](https://github.com/b2bvic/twitter-bookmarks)
- [sws-skills](https://github.com/b2bvic/sws-skills)

## Development

```bash
.venv/bin/python -m pytest -q
.venv/bin/python -m ruff check --select E9,F63,F7,F82 tests
```

CI runs the portable tests and checks syntax-related Python lint rules.

## License

MIT. See [LICENSE](LICENSE).
