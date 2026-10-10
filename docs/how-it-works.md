# How it works

Moved verbatim from the old README.md.

## Pinterest Board Backup

It uses the Pinterest API v5 with the `boards:read` and `pins:read` scopes to
list the boards on my account, read the pins on those boards, and save the
largest available image variant of each pin to local disk.

There is no server, no database, and no third party. Nothing leaves the machine
it runs on. See [PRIVACY.md](../PRIVACY.md).

## Landing page

`index.html` is an unrelated static page — the *trip dancer* landing page —
served from this repo via GitHub Pages. It is self-contained: no build step, no
framework, no external requests except the Google Fonts stylesheet.
