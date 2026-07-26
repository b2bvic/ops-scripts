# twitter-bookmarks

A command-line importer for collecting and classifying saved posts.

## Principle cluster

This repository demonstrates **P02 (own the memory plane)** and **P04 (synthesis starts from sources)** because it fetches bookmark records, compares them with seen identifiers, classifies new items, and writes Markdown files.

[Read the principles](https://victorvalentineromo.com/principles).

## Worked example

```bash
export TWITTER_BEARER_TOKEN="your-current-X-web-client-bearer-token"
export BOOKMARK_WEBHOOK_URL="https://your-host.example/webhook/bookmarks" # only for --notify
./twitter-bookmarks --dry-run
```

`TWITTER_BEARER_TOKEN` is required because X's web GraphQL endpoint expects the
current public web-client bearer value alongside your authenticated Chrome
cookies. The token is runtime configuration and is not stored in this
repository.

`BOOKMARK_WEBHOOK_URL` is optional unless `--notify` is used. No personal host
or endpoint is embedded in the script.

## License

MIT.

## How this was built

This 2026 README refit used model assistance.

No claim is made about how the underlying code was authored or reviewed.
