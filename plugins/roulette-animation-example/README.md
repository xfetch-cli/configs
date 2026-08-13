# Roulette Animation Example

Complete **xfetch** configuration example with animated ASCII logos and
random rotation (roulette) between 6 figures.

This package includes everything needed: the main config that enables the
roulette, the 6 animated figure configs, and the logo files (frames separated
by `===`, consumed by the `animate-logo` plugin).

## Requirements

- [xfetch](https://github.com/xfetch-cli/xfetch) installed.
- The `animate-logo` plugin installed:
  ```bash
  xfetch plugin install animate-logo
  ```
- The `config-roulette` extension installed (needed for random rotation):
  ```bash
  xfetch extension install config-roulette
  ```

## Installation

Copy the contents of the `xfetch/` folder to your configuration directory
(`~/.config/xfetch/` on Linux), **keeping the folder structure**:

```bash
cp -r xfetch/* ~/.config/xfetch/
```

### File map → destination

| File in this package                                | Go to                                  |
| --------------------------------------------------- | -------------------------------------- |
| `xfetch/config.jsonc`                               | `~/.config/xfetch/config.jsonc`        |
| `xfetch/routes-anim.json`                           | `~/.config/xfetch/routes-anim.json`    |
| `xfetch/fetchs/animations/fox/config.jsonc`         | `~/.config/xfetch/fetchs/animations/fox/config.jsonc` |
| `xfetch/fetchs/animations/cat/config.jsonc`         | `~/.config/xfetch/fetchs/animations/cat/config.jsonc` |
| `xfetch/fetchs/animations/kitty/config.jsonc`       | `~/.config/xfetch/fetchs/animations/kitty/config.jsonc` |
| `xfetch/fetchs/animations/blackhole/config.jsonc`   | `~/.config/xfetch/fetchs/animations/blackhole/config.jsonc` |
| `xfetch/fetchs/animations/matrix/config.jsonc`      | `~/.config/xfetch/fetchs/animations/matrix/config.jsonc` |
| `xfetch/fetchs/animations/decrypt/config.jsonc`     | `~/.config/xfetch/fetchs/animations/decrypt/config.jsonc` |
| `xfetch/logos/animations/*.txt`                     | `~/.config/xfetch/logos/animations/`   |

## How it works

### Main config (`config.jsonc`)

Enables the `config-roulette` extension with random strategy. Every time you
run `xfetch`, it picks a random config from `routes-anim.json`:

```jsonc
{
  "config_providers": [
    {
      "extension": "config-roulette",
      "args": {
        "routes": "~/.config/xfetch/routes-anim.json",
        "strategy": "random"
      }
    }
  ]
}
```

### Roulette routes (`routes-anim.json`)

Lists the 6 animated configs that take part in the rotation:

| Name                 | Figure                                |
| -------------------- | ------------------------------------- |
| `001-animate-fox`    | Running fox (converted from GIF)      |
| `002-animate-cat`    | Blinking cat                          |
| `003-animate-kitty`  | Kitty turning its head (GIF)          |
| `004-animate-blackhole` | Black hole (GIF)                  |
| `005-animate-matrix` | Matrix rain                           |
| `006-animate-decrypt`| "DECRYPTING" panel                    |

### Figure configs

Each config in `fetchs/animations/<figure>/config.jsonc` points to its
animation file via the `logo_animation` block (`frame` style) and uses a
different layout:

| Figure    | Layout       | OS icon   |
| --------- | ------------ | --------- |
| fox       | `pacman`     | `` (terminal) |
| cat       | `box`        | `` (terminal) |
| kitty     | `section`    | `` (linux)    |
| blackhole | `tree`       | ``             |
| matrix    | `compact`    | `` (arch)     |
| decrypt   | `side-block` | `` (terminal) |

All configs carry `"daemon": true`, so running `xfetch` (with the roulette or
with `--config` pointing to any of them) pins the animation at the top and
loops it **without blocking the prompt**: the process forks to the background,
the shell prompt returns immediately, and the animation keeps looping pinned at
the top of the terminal.

To stop it:

```bash
xfetch --daemon-stop
```

No extra shell configuration is required — everything activates from the JSON.

**Note on height**: tall figures (`cat` ~29 rows, `matrix` ~24 rows) take up
almost a whole 30-row terminal and leave little room for command output. The
daemon reserves the top rows for the logo; command output stays below it in
the remaining terminal height. Medium-height figures (`fox`, `kitty`,
`blackhole`, `decrypt` ~13-17 rows) are the recommended ones for standard
terminals.

### Logo files

In `logos/animations/`, each figure has two files:

- `<figure>.txt` — the **animation**: frames separated by a `===` line.
- `<figure>_static.txt` — **static frame** (fallback when there is no TTY).

The `.txt` files are consumed by the `animate-logo` plugin via `frames_path`
(animation) and `ascii` (static).

## Test

After copying the files:

```bash
xfetch
```

The animation only runs in TTY (interactive) terminals. On redirects or pipes
the static logo is shown.

## Customization

- **Add a new figure**: create its `.txt` (frames separated by `===`), its
  `_static.txt`, a config in `fetchs/animations/<name>/` and add the entry to
  `routes-anim.json`.
- **Adjust speed**: change `fps` in the `logo_animation` block of each config.
- **Limited duration**: with `"daemon": true` the animation loops forever and
  `duration_ms`/`loop` are ignored; to make it run for a few seconds and stop
  on its own, use `"daemon": false` (the animation plays once, without being
  pinned).
- **Disable the roulette**: point `routes` in `config.jsonc` to a file with a
  single config, or use `xfetch --config <path>` directly.
