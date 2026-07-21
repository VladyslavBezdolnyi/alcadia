# Pinterest Board Backup

A personal, single-user tool that downloads images from my own Pinterest boards
to my own computer for offline backup.

It uses the Pinterest API v5 with the `boards:read` and `pins:read` scopes to
list the boards on my account, read the pins on those boards, and save the
largest available image variant of each pin to local disk.

There is no server, no database, and no third party. Nothing leaves the machine
it runs on. See [PRIVACY.md](PRIVACY.md).

## Usage

```bash
pip install requests
export PINTEREST_TOKEN='...'    # from developers.pinterest.com -> your app
python3 download_pins.py
```

Images are written to `downloads/<board name>/<pin id>.jpg`. Re-running skips
files that already exist, so an interrupted run simply resumes.

## Notes

- Secret boards additionally require the `boards:read_secret` and
  `pins:read_secret` scopes.
- Trial access tokens generated from the app dashboard expire after 24 hours.
- Video pins are skipped.
