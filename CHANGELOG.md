# Changelog

General changelog for the configs repository. Detailed entries live in the
per-folder changelog:

- [`plugins/CHANGELOG.md`](plugins/CHANGELOG.md) — example configuration changes

## 2026-11-19

- Added `configshunter/cyberpunk`, a complete preset for the `confighunter`
  command: main roulette config, 16 variants, banners, logos and 16 image
  logos stored as base64 `.b64` assets without image extensions.
- `configshunter/cyberpunk` no longer bundles `themes/`: equisdots theme-sync
  owns that directory and generates one theme per palette. The preset now
  requires `xfetch extension install theme-sync` at runtime.

## 2026-11-16

- `plugins/roulette-animation-example/xfetch/routes-anim.json` now uses
  `~/.config/xfetch/...` instead of a hardcoded home directory, so the example
  works for every user after copying it into place.
- `scripts/validate.py` now rejects personal absolute paths (`/home/<user>`,
  `/Users/<user>`, `C:\Users\<user>`) so examples stay portable.

## 2026-09-12 — wasm-guests

- Added WebAssembly guest example configs (plugins, effects and config providers) — see [plugins/CHANGELOG.md](plugins/CHANGELOG.md).
- Fixed the broken `swap` glyph in `xfetch/defaults/config.jsonc` and replaced the palette emoji in two layout presets with the Nerd Font palette glyph; `scripts/validate.py` now rejects U+FFFD, control characters and emoji in every validated file.

## 2026-08-19

- Themes moved to their own repository ([`xfetch-cli/themes`](https://github.com/xfetch-cli/themes)) — registry, schema and theme files now live there.

## 2026-08-13 — roulette-animation-example

- Added the animated-logo example configuration — see [plugins/CHANGELOG.md](plugins/CHANGELOG.md).
