# XFetch Cyberpunk Configs

Ten standalone xfetch configs with cyberpunk-oriented layouts, the `gauges`
plugin for memory/swap/disk/battery and the `banner` plugin for a Japanese line
under the logo.

No themes and no custom color maps are used: the configs inherit xfetch's
default colors. Add a `colors` block later if you want a custom scheme. All
configs keep the full default field set.

## Configs

| # | File | Layout | Banner |
|---|------|--------|--------|
| 01 | `configs/01-neon-tokyo.jsonc` | `section` | 永遠は朽ち、儚さが記憶を刻む |
| 02 | `configs/02-acid-terminal.jsonc` | `section-box` | コードの精確さと言葉の感性 |
| 03 | `configs/03-chrome-sunset.jsonc` | `compact` | 経験は文学の素材となる |
| 04 | `configs/04-ghost-protocol.jsonc` | `tree` | 状況の重ね合わせ |
| 05 | `configs/05-blood-machine.jsonc` | `default` | 永遠回帰 |
| 06 | `configs/06-violet-grid.jsonc` | `box` | 秘密の距離 |
| 07 | `configs/07-toxic-rain.jsonc` | `minimal` | 存在しない権利 |
| 08 | `configs/08-magenta-overdrive.jsonc` | `pacman` | 運命の前の儚さ |
| 09 | `configs/09-blue-shadow.jsonc` | `side-block` | 廃墟の間の超越 |
| 10 | `configs/10-amber-relic.jsonc` | `custom-x` | 芥子の舞 |

The file names keep their original style labels; they no longer define colors.

## Install

The configs, routes and banner paths point to
`~/.config/xfetch/fetchs/cyberpunk`, so copy the preset there:

```bash
mkdir -p ~/.config/xfetch/fetchs
cp -r xfetch/presets/cyberpunk ~/.config/xfetch/fetchs/
```

If you install the preset somewhere else, update the paths in `routes.json`
and in each config's `logo_animation.frames_path`.

## Requirements

- xfetch 1.0.0 or newer.
- The `gauges` and `banner` plugin binaries.
- A Nerd Font for the module icons.
- A Japanese/CJK font for the banners.

### Install the plugins

From a clone of `xfetch-cli/plugins`:

```bash
cargo build --release -p xfetch-plugin-gauges -p xfetch-plugin-banner
mkdir -p ~/.config/xfetch/plugins
cp target/release/xfetch-plugin-gauges target/release/xfetch-plugin-banner ~/.config/xfetch/plugins/
```

### Install a Japanese font (Arch Linux)

```bash
sudo pacman -S --needed noto-fonts-cjk adobe-source-han-sans-otc-fonts
fc-cache -f
```

Restart the terminal afterwards. Check with:

```bash
fc-list :lang=ja | head
```

## Run

The banners use `~` paths, so you can run from anywhere after installing:

```bash
xfetch --config ~/.config/xfetch/fetchs/cyberpunk/configs/01-neon-tokyo.jsonc
```

Browse all ten:

```bash
cd ~/.config/xfetch/fetchs/cyberpunk
for f in configs/*.jsonc; do
    clear
    echo "== $f =="
    xfetch --config "$f"
    printf "\nEnter para la siguiente..."
    read -r _
done
```

## Roulette

The preset includes `config.jsonc` (a full fallback config plus the
`config-roulette` provider) and `routes.json` (the 10 routes). Install the
extension first:

```bash
xfetch extension install config-roulette
```

Run the roulette:

```bash
xfetch --config ~/.config/xfetch/fetchs/cyberpunk/config.jsonc
```

`random` is the default. To keep the same config all day and change at
midnight, edit `config.jsonc` and set:

```json
"strategy": "daily"
```

Important: `config-roulette` parses each route with strict JSON, not JSONC. The
10 configs are therefore comment-free JSON despite the `.jsonc` extension.
Keep them strict if you edit them. The routes and banner paths use `~`; if you
move this folder, update `routes.json` and the `logo_animation.frames_path`
entries.

To use the roulette as your default, merge the `config_providers` block from
`config.jsonc` into `~/.config/xfetch/config.jsonc` (back it up first), or run
xfetch with `--config` as shown above.

## Banners

The phrases are in `banners/*.txt` and are loaded through
`logo_animation.frames_path`. They are Xscriptor phrases and titles translated to Japanese:

| # | Japanese | Spanish | Source |
|---|----------|---------|--------|
| 01 | 永遠は朽ち、儚さが記憶を刻む | Lo eterno se marchita y lo efímero marca nuestros recuerdos. | Bio de GitHub |
| 02 | コードの精確さと言葉の感性 | La precisión del código y la sensibilidad de la palabra. | Bio / Info |
| 03 | 経験は文学の素材となる | La experiencia se convierte en materia literaria. | Bio / Info |
| 04 | 状況の重ね合わせ | La superposición de circunstancias. | Blog / concepto |
| 05 | 永遠回帰 | El eterno retorno. | Blog |
| 06 | 秘密の距離 | La distancia del secreto. | Blog / serie |
| 07 | 存在しない権利 | El derecho a no ser. | Blog |
| 08 | 運命の前の儚さ | La fragilidad ante el destino. | Blog |
| 09 | 廃墟の間の超越 | La búsqueda de trascendencia entre ruinas. | Cielos de alquitrán |
| 10 | 芥子の舞 | La danza de las amapolas. | Obra |

Edit or replace those files to change the message. The banner plugin centers
the text under the ASCII logo and counts CJK characters as two columns.

## Images

The configs are strict JSON for roulette, so there is no commented `logo_path`.
When you add artwork, add a normal field to the config:

```json
"logo_path": "images/01-neon-tokyo.png"
```

Note that the `banner` plugin only runs with ASCII logos; if you switch to a
PNG/SVG logo, the Japanese banner will not be appended.

`gauges` needs the plugin binary; `banner` needs a real TTY, so run `xfetch`
directly in the terminal rather than piping its output.

## Tested

All ten configs were rendered with a local release build of xfetch 1.0.0 and
the `gauges`/`banner` plugins. The bars and the Japanese banner appeared in
every layout, with no plugin errors. The files pass `scripts/validate.py` (no
broken glyphs, no emoji).

The `config-roulette` extension was installed and tested with `config.jsonc`;
the routes loaded and different configs were selected across runs. Consecutive
runs in the same second can repeat because the extension seeds from sub-second
time.
