# macOS iMessage history reader: imessage-pull

`imessage-pull` reads local message records for macOS users. Use a contact lookup to inspect recent Messages history without exporting the entire database.

[Project page](https://scalewithsearch.com/code/ops-scripts#imessage-pull)

## Install

Requirements: Python 3.11 or later.

```bash
gh repo clone b2bvic/ops-scripts
cd ops-scripts/components/imessage-pull
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

## Quick start

```bash
.venv/bin/python -m pytest -q
```

These checks use synthetic input and perform no live sends.

## Usage

Give the terminal Full Disk Access before a run.

```bash
./imessage-pull 5551234567 20
```

The first argument is a substring of the chat identifier, such as a phone number or an email address. The second argument is the message count. The default count is 20.

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

## Model assistance

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
