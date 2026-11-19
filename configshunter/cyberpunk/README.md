# Cyberpunk complete preset

Complete xfetch configuration with 16 cyberpunk variants, randomized through
`config-roulette`, plus themes, ASCII logos and image logos. The images are
stored as base64 (`.b64`) and are decoded to `.jpg` by the `confighunter`
command during installation.

## What is included

- `config.jsonc`: main config with `config-roulette` and `theme-sync`.
- `fetchs/cyberpunk/config.jsonc`: roulette fallback config.
- `fetchs/cyberpunk/routes.json`: 16 routes, one per variant.
- `fetchs/cyberpunk/configs/`: the 16 variant configs.
- `fetchs/cyberpunk/banners/`: the Japanese banner texts.
- `fetchs/cyberpunk/images/`: 16 base64 image logos (`*.b64`, no image
  extension in the source name).
- `themes/`: the full local theme collection.
- `logos/`: ASCII logos used by the config.

## Install with confighunter

```bash
xfetch command install confighunter
xfetch run confighunter install cyberpunk
```

The command:

1. Downloads the preset from `xfetch-cli/configs`.
2. Decodes every `*.b64` asset to `*.jpg` in `~/.config/xfetch`.
3. Backs up the files it replaces under
   `~/.config/xfetch/.confighunter/backups/<timestamp>/`.
4. Prints this README and the requirement checklist.

To try a branch before merging:

```bash
xfetch run confighunter install cyberpunk --branch <branch>
```

## Manual install

```bash
cp -r configshunter/cyberpunk/. ~/.config/xfetch/
find ~/.config/xfetch/fetchs/cyberpunk/images -name '*.b64' -print0 |
  while IFS= read -r -d '' file; do
    base64 -d "$file" > "${file%.b64}.jpg" && rm "$file"
  done
```

The config paths use `~/.config/xfetch/fetchs/cyberpunk`, so the preset must be
installed there. The main config also uses that path for the roulette routes,
the banner and the image logos.

## Requirements

- xfetch 1.0.4 or newer.
- Plugins: `banner`, `banner-text`, `gauges`, `display-resolution`.
- Extensions: `config-roulette`, `theme-sync`.
- A Nerd Font (Hack Nerd Font recommended) for the module icons.
- A Japanese/CJK font (Noto Sans CJK JP recommended) for the banners.
- `python3` for the `theme-sync` extension.

Install the addons with xfetch:

```bash
xfetch plugin install banner-text
xfetch plugin install gauges
xfetch plugin install display-resolution
xfetch plugin install banner
xfetch extension install config-roulette
xfetch extension install theme-sync
```

`banner` and `gauges` are local builds in the current setup; if they are not
available from the catalog on your machine, build them from
`xfetch-cli/plugins` or disable those module entries.

`theme-sync` reads `~/.config/hypr/settings.json`. If that file does not exist,
it falls back to the `x` theme, which is included in this preset.

## Run

```bash
xfetch
```

The default config uses the roulette. To pin one variant:

```bash
xfetch --config ~/.config/xfetch/fetchs/cyberpunk/configs/01-neon-tokyo.jsonc
```

## Images

The source files are named `01-neon-tokyo.b64`, `02-acid-terminal.b64`, and so
on. The decoded files are `01-neon-tokyo.jpg`, `02-acid-terminal.jpg`, and so
on, matching the `logo_path` entries in the variant configs. No image
extension is used in the repository source names.

## License

The configuration files are distributed under the repository license. The
`confighunter` command addon is licensed separately under GPL-3.0-only.
