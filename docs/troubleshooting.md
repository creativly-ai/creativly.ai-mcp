# Troubleshooting

## “Creativly’s tools are unavailable”

A selected plugin name or a link to the setup guide is not necessarily an authenticated connection. Check that the configured server is **https://mcp.creativly.ai/mcp**, complete OAuth, then ask for projects and balance before trying generation.

If an imported plugin offers no Connect action, add the endpoint as a custom MCP server. Do not work around a missing client connection by hard-coding private plugin IDs, authorization callbacks or a copied access token.

## The browser says the authorization request expired

Start Connect again from the client. OAuth codes/state and PKCE challenges belong to that fresh attempt. An old authorization URL copied out of a tab is not a reusable sign-in link.

## The project I want is missing

`list_projects` returns projects approved for this OAuth connection, not every project someone else owns. Reauthorize with the projects you intend to use. New project creation also depends on the permission granted at connection time.

## I cannot upload a reference

New uploads need `assets:write`; an older grant may not have it. Reauthorize if needed. In a supported UI client, ask to open Creativly’s upload picker. In a programmatic client with file access, use the reserve → PUT → complete → ready flow.

The agent cannot assume that a file attached to the host’s chat is automatically a Creativly asset. A file must finish moderation before it can be used by a model.

## I see “Load image” or a host warning

Some clients ask before fetching an external image URL. Use the native preview included by `get_asset` or the supported gallery where possible; the original download remains a signed external URL. These are different surfaces, and the hosted service cannot promise to remove a client’s confirmation UI.

## A video only appears as a link

The client may not render MCP Apps. The same asset still has a native download and Creativly session link. In a UI-capable client, completed videos are shown with `show_assets`; `show_generation` handles live image jobs rather than live video previews.

## The new video card replaced the source images

A host may replace a prior app view. Pass the source images and completed videos together to `show_assets`; related owned source images are included automatically by default. Keep the same session ID instead of creating one session for images and another for the videos.

## A download expired

Use `get_asset` on the saved asset ID for a fresh download link. Links last 15 minutes. Keep IDs for later edits; do not store a signed URL as a permanent reference.

## The request timed out

If you received a batch ID, use `get_job` or `resume_session`. If submission was uncertain, retry the exact same arguments with the same `client_request_id`. A new ID represents a new request and may spend credits again.

## A model or edit is unavailable

Inspect `get_model` and obtain a quote for the exact operation/settings. A catalog entry is not a promise that every operation is exposed to every account. A video model that supports an image-to-video reference does not necessarily support a first-frame image alongside a video edit.
