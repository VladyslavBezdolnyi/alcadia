---
name: pinterest
description: Personal single-user Pinterest board backup — a Python script that pulls the largest image of every pin on my own boards via API v5 to local disk; the repo also hosts the unrelated trip dancer landing page on GitHub Pages (repo alcadia).
---

# pinterest

## Map

### In the repo
- `download_pins.py` — the backup tool; run by hand with `PINTEREST_TOKEN` set.
- `downloads/` — backup output, `<board name>/<pin id>.jpg`; gitignored.
- `PRIVACY.md` — privacy policy for the Pinterest developer app.
- `index.html` — trip dancer landing page, unrelated to the backup tool; served by GitHub Pages (`.nojekyll` disables Jekyll).
- `assets/` — the landing page's WebP images, generated from `webpage-assets/` with `cwebp`.
- `webpage-assets/` — original PNG sources for `assets/`; gitignored, exists only on this machine.

### Docs
- `docs/how-it-works.md` — which API scopes the backup uses, why nothing leaves the machine, and what the landing page depends on.
