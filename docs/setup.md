# Connect Creativly

**MCP endpoint:** `https://mcp.creativly.ai/mcp`<br>
**Transport:** Streamable HTTP<br>
**Authentication:** OAuth through your Creativly account<br>
**Visual setup guide:** https://www.creativly.ai/mcp

The setup guide is a web page. It is not the server URL. Use the full MCP endpoint above in your client.

## ChatGPT

1. Open Plugins and choose **Add custom MCP server**.
2. Name it **Creativly**, paste the endpoint, and select OAuth authentication.
3. Connect your account in the browser. Choose the projects and credit limits you want to approve.
4. In a chat, select Creativly and ask: **“Show my projects and credit balance.”**

Client availability and settings can vary by account or workspace. If an imported plugin never offers Connect, use the custom MCP server flow with the same endpoint; do not paste an expiring authorization callback or a private connector ID.

[OpenAI’s custom MCP setup](https://developers.openai.com/plugins/quickstart)

## Claude

1. Open Settings → Connectors and add a custom connector.
2. Name it **Creativly** and enter the endpoint.
3. Finish the browser sign-in and authorization.
4. Enable Creativly in your conversation, then try the read-only account prompt above.

A workspace may require an administrator to enable custom connectors. Start with the [live Claude guide](https://www.creativly.ai/mcp?tab=claude) if your account’s navigation differs.

## Codex

```sh
codex mcp add creativly --url https://mcp.creativly.ai/mcp
codex mcp login creativly
codex mcp list
```

Complete authorization in the browser when prompted. To configure the URL directly, add the [example TOML entry](../config/codex.toml) to your existing configuration; preserve your other MCP servers.

```toml
[mcp_servers.creativly]
url = "https://mcp.creativly.ai/mcp"
```

The entry supplies connection settings, not credentials. Use `codex mcp login creativly` for authorization rather than committing access tokens.

[Official Codex MCP documentation](https://developers.openai.com/codex/mcp)

## Claude Code

```sh
claude mcp add --transport http creativly https://mcp.creativly.ai/mcp
```

Open Claude Code, run `/mcp`, select Creativly and authenticate. For project configuration, merge [this JSON example](../config/claude-code.mcp.json) into `.mcp.json` rather than replacing an existing server list:

```json
{
  "mcpServers": {
    "creativly": {
      "type": "http",
      "url": "https://mcp.creativly.ai/mcp"
    }
  }
}
```

[Official Claude Code MCP documentation](https://code.claude.com/docs/en/mcp)

## Other MCP clients

Use a client that supports remote Streamable HTTP and OAuth with PKCE. The server publishes protected-resource metadata; its authorization server lives at `https://www.creativly.ai`. Let the client perform discovery and authorization. Do not manually construct an authorization URL with another client’s callback or reuse a one-time code.

You can check public discovery without signing in:

```sh
curl https://mcp.creativly.ai/.well-known/oauth-protected-resource
```

Protected tools require authentication. A `401` when unauthenticated is expected and should lead a capable client into its connection flow.

## First check

> Use Creativly to show my projects and credit balance.

This is read-only. Once it works, try a brief from [the examples](../examples/briefs.md). If tools are missing, check the connection first; a link to the web setup page is not evidence of an authenticated MCP session.
