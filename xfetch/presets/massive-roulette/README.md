# massive-roulette

A large collection of **149 xfetch configs** intended to be rotated with the
`config-roulette` extension, so every `xfetch` run can look completely
different (layout, theme colours, logo, modules, icons, effects).

- 100 standard configs across every layout (4–12 modules).
- 30 complex `custom-x` configs with intro effects (`decrypt`, `glitch`).
- 50 configs using the `gauges` plugin with Chinese/Japanese icons
  (`存 换 盘 电` / `存 換 盤 電`) and a CJK proverb banner under the logo.
- 9 configs using the `langs` plugin (repository / org language breakdown).

All colour palettes are inlined in each config, so **themes are optional**:
if a `theme` name is not installed, xfetch simply ignores it and the inline
colours are used.

## Requirements

- xfetch **1.0.0** or newer.
- The `config-roulette` extension.
- The plugins listed below.
- The `decrypt` and `glitch` effects (used by the custom-x configs).
- A CJK font for the 50 configs with Chinese/Japanese icons and the banner.

## Install

### 1. Copy the preset

```bash
mkdir -p ~/.config/xfetch/fetchs
cp -r presets/massive-roulette ~/.config/xfetch/fetchs/massive-roulette
```

### 2. Copy the logos

The configs reference logos from `~/.config/xfetch/logos/`. Copy every file in
`logos/` there:

```bash
mkdir -p ~/.config/xfetch/logos
cp logos/*.txt ~/.config/xfetch/logos/
```

These are the logo files that must be present:

```
alma.txt          alpine.txt        antix.txt         arch.txt
archbang.txt      arcolinux.txt     artix.txt         bedrock.txt
blackarch.txt     bodhi.txt         cachyos.txt       garuda.txt
gentoo.txt        mx-linux.txt      nitrux.txt        nixos.txt
opensuse-leap.txt raspberrypi.txt   rhel.txt          serpent.txt
x.txt
```

### 3. Extension, plugins and effects

```bash
# Roulette extension
xfetch extension install config-roulette

# Official native plugins used by the configs
xfetch plugin install user-info docker temperature timezone github-stats \
    display-resolution theme-detection music-player animate-logo

# Intro effects (custom-x configs)
xfetch effects install decrypt
xfetch effects install glitch
```

The following plugins live in the
[xfetch-cli/plugins](https://github.com/xfetch-cli/plugins) repository and may
need to be built until they are published:

```bash
# from a clone of xfetch-cli/plugins
cargo build --release -p xfetch-plugin-gauges -p xfetch-plugin-langs -p xfetch-plugin-banner
cp target/release/xfetch-plugin-{gauges,langs,banner} ~/.config/xfetch/plugins/
```

| Plugin | Used by | Notes |
|---|---|---|
| `config-roulette` (extension) | all | Picks a random config on every run. |
| `gauges` | 50 configs | Memory/swap/disk/battery bars; CJK glyphs. |
| `langs` | 9 configs | GitHub languages + repo/org info. |
| `banner` | 50 configs | CJK proverb banner under the logo. |
| `animate-logo` | 6 configs | Animated ASCII logo. |
| `docker`, `github-stats`, `music-player`, `temperature`, `timezone`, `user-info`, `display-resolution`, `theme-detection` | various | Optional info providers. |

### 4. Fonts (CJK)

The 50 gauge configs print Chinese/Japanese characters; install a CJK font so
they are not rendered as tofu:

```bash
# Arch Linux
sudo pacman -S --needed noto-fonts-cjk adobe-source-han-sans-otc-fonts
# optional, a CJK programming font
yay -S ttf-sarasa-gothic
fc-cache -f
```

Any terminal with automatic font fallback (e.g. kitty) picks them up after a
restart.

### 5. Enable the roulette

Merge `config_providers` from the bundled `config.jsonc` into your
`~/.config/xfetch/config.jsonc` (or copy the file if you do not have one):

```jsonc
{
    "config_providers": [
        {
            "extension": "config-roulette",
            "args": {
                "routes": "~/.config/xfetch/fetchs/massive-roulette/routes.json",
                "strategy": "random"
            },
            "timeout_secs": 5
        }
    ]
}
```

Then just run:

```bash
xfetch
```

Use `"strategy": "daily"` to keep the same config all day, or run a specific
one directly:

```bash
xfetch --config ~/.config/xfetch/fetchs/massive-roulette/configs/009-espresso-section.jsonc
```

## Notes

- `langs` calls the GitHub API. Authenticated requests get 5000 req/h instead
  of 60; the plugin reads `GITHUB_TOKEN`, `GH_TOKEN` or `gh auth token`
  automatically, so a machine logged in with `gh` needs no extra setup.
- The banner and logo animations only play in a real TTY (not when piping).
- No config displays the public IP address; only `local_ip` is shown.
- Paths use `~`, so the preset works for any user.
