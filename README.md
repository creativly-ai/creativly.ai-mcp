<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://www.creativly.ai/logos/creativly-wordmark-on-dark-576w.webp">
    <img src="https://www.creativly.ai/logos/creativly-wordmark-on-light-576w.webp" alt="Creativly" width="230">
  </picture>
</p>

<h1 align="center">Creativly MCP</h1>
<p align="center">Your next image or video starts in the conversation.</p>
<p align="center">
  <a href="https://www.creativly.ai/mcp">Interactive setup</a> ·
  <a href="docs/setup.md">Connect your client</a> ·
  <a href="docs/tools.md">22 tools</a> ·
  <a href="examples/briefs.md">Try a brief</a> ·
  <a href="https://www.creativly.ai/developers">Building with an API?</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2563eb.svg" alt="MIT license"></a>
</p>

Create images, edit references and make videos from **ChatGPT, Claude, Codex or Claude Code**. Creativly keeps the work in your projects and sessions, so you can return to it, change a detail or turn an image into a film.

This is the connection guide, tool reference and example collection for the **hosted Creativly MCP server**. Connect it once and use your own Creativly account through OAuth.

<table>
  <tr>
    <td width="50%"><img src="https://cdn.creativly.ai/mcp/examples/2026-11-originals/trail-launch-nano-banana-2-1-native-1a00a119ff1d01b4.webp" alt="Moss-green trail shoe with an orange lace on wet volcanic rock" width="100%"></td>
    <td width="50%" align="center"><img src="https://cdn.creativly.ai/mcp/examples/2026-11-originals/paper-crab-nano-banana-2-1-native-640-8fd58cad3fe72c23.webp" alt="Red folded-paper crab on a pale blue tabletop" width="70%"></td>
  </tr>
  <tr>
    <td><strong>“Give it a strong editorial feel.”</strong><br>A product-launch brief becomes a finished image.</td>
    <td><strong>“Make it feel handmade.”</strong><br>A paper character, ready for a playful little film.</td>
  </tr>
</table>

*Examples featured in the live Creativly MCP/API guides. Images made with Nano Banana 2.1; films made with Gemini Omni 1.1 Flash. [Prompts and original films →](examples/showcase.md)*

## Connect

**Server URL · Streamable HTTP · OAuth**

```text
https://mcp.creativly.ai/mcp
```

<table>
  <tr><th>ChatGPT</th><th>Claude</th><th>Codex</th><th>Claude Code</th></tr>
  <tr>
    <td>Add a custom MCP server in Plugins. Paste the URL and choose OAuth.</td>
    <td>Add a custom connector in Settings → Connectors.</td>
    <td>Run the two commands below.</td>
    <td>Add the HTTP server, then authenticate with <code>/mcp</code>.</td>
  </tr>
</table>

**Codex**

```sh
codex mcp add creativly --url https://mcp.creativly.ai/mcp
codex mcp login creativly
```

**Claude Code**

```sh
claude mcp add --transport http creativly https://mcp.creativly.ai/mcp
```

Then open Claude Code, run `/mcp`, select Creativly and authenticate.

Sign in through Creativly, choose the projects you want to share and set the connection’s credit limits. You do not paste a Creativly API key into this OAuth connection. Client features and connector availability depend on the host you use.

[Step-by-step setup and configuration files →](docs/setup.md)

## Ask for something you actually want to make

> Use Creativly to create a launch image for a moss-green trail shoe on rain-dark volcanic rock. Give it a strong editorial feel, with a bright orange lace and low mist behind it.

Or start without spending anything:

> Use Creativly to show my projects and credit balance.

Then keep working naturally:

> Make the lighting a little moodier. Keep the orange lace.

> Turn the image into a short product film. Keep it in this session.

Defaults are **Nano Banana 2.1** for images/image edits and **Gemini Omni 1.1 Flash** for video/supported video edits. Ask for another model when you want one; the agent can discover the current catalog and check access and settings before submission.

## From a still to a six-second film

<a href="https://cdn.creativly.ai/mcp/setup/2026-11-fresh/bakery-morning/bakery-morning-omni-1-1-flash-native-cc0be13ba05bba16.mp4"><img src="https://cdn.creativly.ai/mcp/setup/2026-11-fresh/bakery-morning/bakery-morning-omni-1-1-flash-native-poster-d04e31dcee82f9a1.webp" alt="Watch the bakery example: a croissant pulled apart in warm morning light" width="100%"></a>

**[▶ Watch the result](https://cdn.creativly.ai/mcp/setup/2026-11-fresh/bakery-morning/bakery-morning-omni-1-1-flash-native-cc0be13ba05bba16.mp4)** · Gemini Omni 1.1 Flash · 6 seconds

> Turn this bakery photo into a six-second film. Gently pull the croissant apart so a few crisp flakes fall through the warm morning light.

Use an image already in a project, or add one through the private upload picker in a supported client. The agent can reuse its asset ID, submit a video job and return the finished film without losing the original image.

## What the connection can do

| Work | Tools |
| --- | --- |
| Find your workspace | `get_account`, `list_projects`, `create_project` |
| Keep a session going | `list_sessions`, `create_session`, `resume_session` |
| Choose models and check cost | `list_models`, `get_model`, `quote_generation` |
| Make or edit media | `generate_image`, `edit_image`, `generate_video`, `edit_video` |
| Follow jobs and retrieve originals | `get_job`, `list_assets`, `get_asset` |
| Show results in supported clients | `show_generation`, `show_assets` |
| Add your own files | `show_upload`, `reserve_upload`, `complete_upload`, `get_upload` |

[Every tool, its exact parameters and the machine-readable schemas →](docs/tools.md)

### Made to keep the work together

A session can contain **both images and videos**. Ask for two images, animate them, then return to the originals: those are related pieces of the same session, not a reason to open a new one for every prompt.

Accepted jobs return durable IDs promptly. Disconnecting the chat does not cancel them. The agent checks progress at the server’s suggested interval and can resume the saved session later.

### Previews, playback and full originals

Compatible clients can show live image-generation progress, image previews, video playback and result actions in a compact gallery. Related source images can stay alongside the videos made from them.

Clients without that UI still receive the job data, asset metadata and links. `get_asset` can include native image/poster pixels; `download_url` is the unchanged full original. Download links expire after 15 minutes and can be refreshed from the asset ID. Your saved asset stays in Creativly.

[How sessions, uploads and result cards work →](docs/workflows.md)

## Your account, with limits you choose

OAuth gives this connection access to the projects and actions you approve. Read tools, quotes, uploads and gallery views do not spend generation credits. Generation uses your existing balance and must fit the quote, request cap, account access and connection limits.

Uploading a new file requires `assets:write` permission. Existing connections are not silently given that permission; reconnect and approve it when needed. The server does not automatically read files attached to an unrelated chat.

[Authentication and credit details →](docs/workflows.md#authentication-and-credits)

## Browse the repository

[Client setup](docs/setup.md) · [Tool reference](docs/tools.md) · [Workflows](docs/workflows.md) · [Troubleshooting](docs/troubleshooting.md) · [Prompt collection](examples/briefs.md) · [Schemas](schemas)

[Contributing](CONTRIBUTING.md) · [Report a security issue](SECURITY.md) · [Creativly API on GitHub](https://github.com/creativly-ai/creativly.ai-api)

The documentation and configuration examples use the [MIT license](LICENSE). This repository connects to the hosted service; it does not contain a self-hosted copy of Creativly’s production backend. Linked brand/showcase media are separate from this code license.
