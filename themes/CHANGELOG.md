# Changelog

Changes to the theme registry (`themes/`): colors, presets, index and schema.

## 2026-08-19

### Theme Format Simplified

- All registry themes (`themes/colors/*.jsonc`) dropped the `icons` block — icons are a per-user font choice, not theme identity (the core fills them from defaults; backward compatible).
- Each theme now ships `logo_color` (its primary accent) so the ASCII logo is colored to match the palette.

## 2026-08-13

### Initial Theme Registry

- Added the theme registry with `index.json` (metadata: name, author, version, description, layout, palette_style, tags, source), `schema.json` and the `colors/` directory.
