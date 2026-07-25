---
name: x-read-article
description: Read the full text of an X (Twitter) post, thread, or long-form X Article when a normal fetch fails. x.com answers unauthenticated server-side fetches with 402 Payment Required, so this drives the user's already-logged-in Chrome instead. Trigger phrases: "read this x post", "read this tweet", "what does this thread say", "x.com 402", "402 payment required", "received 0 bytes", "can you read https://x.com/...", "summarize this X article", "twitter link", "read this twitter thread".
---

# Read an X post or article

## Why the plain fetch fails

`x.com` returns `402 Payment Required` with an empty body to any unauthenticated server-side request. That is X's anti-scraping gate: reading X programmatically otherwise requires a paid X API tier.

It is **not** a charge to the user and **not** an Anthropic billing event. Say that plainly if the user asks about the 402, and never offer to pay for anything.

Do not retry `WebFetch`, do not fall back to `curl`, and do not go looking for a nitter or mirror instance. Go straight to the browser: the user's Chrome profile is already signed in.

## Steps

1. Load the browser tools in ONE `ToolSearch` call:

   ```text
   select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__get_page_text
   ```

2. `navigate` to the post URL. Called standalone with no `tabId`, it opens a tab in the session's group and returns the tab list in its result.

3. `get_page_text` on that tab. It targets the `<article>` element, which is the whole post, and for an X Article it returns the entire long-form body in one call. `read_page` is not needed and costs far more context.

## What comes back

Text arrives in this order: display name, `@handle`, title, four engagement counts (replies, reposts, likes, views), the body, then the timestamp and the counts again. Strip the duplicated count runs when quoting or summarizing; they are page chrome, not content.

## Gotchas

- A body that stops at "Show more", or a login wall, means that Chrome profile is signed out. Say so and stop. Do not attempt to sign in.
- On a thread, `get_page_text` returns the focused post plus whatever replies happen to be rendered. Identify which parts are the author's own continuation before summarizing as "the thread".
- Read only. Do not like, repost, reply, follow, or click through.
- Quote sparingly and attribute; summarize in your own words rather than reproducing the article wholesale.
- For syncing many saved posts at once rather than reading one, use the `scrape-x-bookmarks` skill instead.
