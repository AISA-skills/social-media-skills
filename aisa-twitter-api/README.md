# AIsa Twitter API

Flagship Twitter/X command center for research, monitoring, watchlists, and OAuth-approved posting through the AIsa relay.

## What it does

- Search Twitter/X profiles, tweets, trends, lists, communities, and Spaces
- Inspect timelines, mentions, replies, quotes, and thread context
- Support watchlist-style monitoring and approved posting workflows through OAuth
- Relay API requests, OAuth approval, and approved media uploads through `https://api.aisa.one`
- Optionally run read-only tweet search through Xquik with `XQUIK_API_KEY`

## Best fit

- Use this as the primary Twitter/X skill when the user wants one general-purpose surface for research, monitoring, watchlists, and approved posting.
- Use `aisa-twitter-engagement-suite` when the task is mainly likes, follows, replies, or other engagement actions.
- Use `aisa-twitter-command-center` when the task is mainly watchlists, trend scanning, and monitoring.

## Setup

```bash
export AISA_API_KEY="your-key"
export XQUIK_API_KEY="your-xquik-key" # Optional, only for xquik-search
```

Requires:

- `python3`
- `AISA_API_KEY`
- `XQUIK_API_KEY` when using the optional Xquik search command
- network access to `https://api.aisa.one`
- network access to `https://xquik.com` when using Xquik search
- explicit OAuth approval before posting
- user-provided media files for image or video uploads

## Common Commands

```bash
python3 scripts/twitter_client.py search --query "AI agents" --type Latest
python3 scripts/twitter_client.py xquik-search --query "AI agents" --limit 20
python3 scripts/twitter_oauth_client.py authorize
python3 scripts/twitter_oauth_client.py post --text "Hello from AIsa"
```

## Security & Trust

- Requires only `AISA_API_KEY` as the declared environment secret.
- Uses `XQUIK_API_KEY` only for optional read-only Xquik search.
- Uses a relay-based flow to `https://api.aisa.one` for reads, OAuth handling, and approved uploads.
- External writes happen only after explicit OAuth approval.
- Does not require passwords or browser cookies.
- Do not claim posting succeeded until the relay returns success.

## Legal

Xquik is an independent third-party service. Not affiliated with X Corp. "Twitter" and "X" are trademarks of X Corp.
