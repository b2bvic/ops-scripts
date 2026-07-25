# imessage-pull

A macOS command-line reader for extracting recent records from the local Messages database.

## Principle cluster

This repository demonstrates **P02 (own the memory plane)** and **P04 (synthesis starts from sources)** because it queries the local SQLite store by contact identifier and returns a bounded result set.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
./imessage-pull 5551234567 20
```

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
