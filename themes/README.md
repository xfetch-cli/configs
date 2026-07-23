# xfetch Themes

Theme files define the visual appearance of xfetch: colors, icons, layout, and logo.
They contain no module configuration -- that belongs in your main `config.jsonc`.

## Repository Structure

```
themes/
  README.md              # This file
  index.json             # Registry manifest for theme downloader
  schema.json            # JSON Schema for index validation
  colors/                # Theme definitions
    dracula.jsonc
    nord.jsonc
    catppuccin-mocha.jsonc
    retro-pacman.jsonc
    berlin.jsonc
    tree-compact.jsonc
```

## Available Themes

| Theme | Layout | Style |
|-------|--------|-------|
| `dracula` | section | Dark magenta/red/cyan palette |
| `nord` | section | Cool blue/cyan arctic palette |
| `catppuccin-mocha` | section | Warm mocha pastel palette |
| `retro-pacman` | pacman | Classic Pac-Man arcade style |
| `berlin` | default | No colors, no icons |
| `tree-compact` | tree | Hierarchical tree layout |

## Usage

In your `~/.config/xfetch/config.jsonc`:

```jsonc
{
    "theme": "dracula",
    "modules": ["os", "kernel", "cpu", "memory", "disk"]
}
```

Or with a custom path:

```jsonc
{
    "theme": "~/.config/xfetch/themes/custom.jsonc",
    "modules": [...]
}
```

## Theme File Format

A theme file can contain any of these fields:

| Field | Type | Description |
|-------|------|-------------|
| `layout` | string | Layout style name |
| `colors` | object | Per-module color mappings |
| `icons` | object | Per-module icon mappings |
| `palette_style` | string | Palette display style |
| `show_colors` | boolean | Enable ANSI colors |
| `logo_path` | string | Path to logo file |
| `header_icons` | string[] | Pac-Man header icons |
| `footer_text` | string | Pac-Man footer text |

## Creating a Theme

Create a `.jsonc` file in `~/.config/xfetch/themes/` with any subset of the above fields.
Values from your `config.jsonc` always override theme values.
