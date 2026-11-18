# Contributing

Help make Creativly easier to connect and use: improve a client guide, clarify a tool parameter or contribute a useful brief. This repository documents the hosted MCP server.

## Update the tool reference

`schemas/tools.json` is a public contract snapshot. The connected server's `tools/list` remains authoritative. When the public contract changes, update the snapshot from the service and regenerate the reference with Python 3.10 or later:

```sh
python3 tools/render_reference.py
```

The renderer uses the standard library and does not connect to an account or spend credits.

Keep model settings and credit prices discoverable through the server. Do not add an independent pricing catalog or private client identifiers to a connection guide.

## Submit a focused change

- Describe the client and version when reporting a connection or display issue. Hosts support different MCP features.
- Redact OAuth tokens, callbacks, signed asset URLs, private project data and customer files from reports.
- Keep notebook checkpoints, caches, local credentials and generated media out of commits. Showcase media stays on Creativly's CDN.
- Open pull requests against `master` and explain how you verified the change. See the [security policy](SECURITY.md) for sensitive reports.
