"""Download images from your own Pinterest boards to ./downloads/<board>/.

Usage:
    pip install requests
    export PINTEREST_TOKEN='...'    # from developers.pinterest.com -> your app
    python download_pins.py

Needs the boards:read and pins:read scopes (plus the *_secret variants for
secret boards). Re-running skips files that already exist.
"""

import os
import pathlib
import sys
import time

import requests

API = "https://api.pinterest.com/v5"
OUT = pathlib.Path("downloads")

token = os.environ.get("PINTEREST_TOKEN")
if not token:
    sys.exit("set PINTEREST_TOKEN first")

session = requests.Session()
session.headers["Authorization"] = f"Bearer {token}"


def paged(path):
    """Yield every item from a paginated v5 endpoint."""
    params = {"page_size": 100}
    while True:
        r = session.get(f"{API}{path}", params=params, timeout=30)
        if r.status_code == 429:
            time.sleep(int(r.headers.get("Retry-After", 30)))
            continue
        r.raise_for_status()
        body = r.json()
        yield from body.get("items", [])
        bookmark = body.get("bookmark")
        if not bookmark:
            return
        params["bookmark"] = bookmark


def largest_image(pin):
    """URL of the biggest available variant, or None for non-image pins."""
    images = (pin.get("media") or {}).get("images") or {}
    if not images:
        return None
    return max(images.values(), key=lambda i: i.get("width") or 0).get("url")


def safe(name):
    return "".join(c for c in name if c not in '/\\:*?"<>|').strip() or "untitled"


for board in paged("/boards"):
    folder = OUT / safe(board["name"])
    folder.mkdir(parents=True, exist_ok=True)

    for pin in paged(f"/boards/{board['id']}/pins"):
        url = largest_image(pin)
        if not url:
            continue

        dest = folder / f"{pin['id']}.jpg"
        if dest.exists():
            continue

        image = session.get(url, timeout=30)
        image.raise_for_status()
        dest.write_bytes(image.content)
        print(dest)
