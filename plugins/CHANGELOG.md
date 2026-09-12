# Changelog

Changes to the example xfetch configurations (`plugins/`): ready-to-use configs that combine core features with plugins and extensions.

## 2026-09-12 — glyph fixes

- `xfetch/defaults/config.jsonc` and the layout presets now use valid Nerd Font glyphs: the swap icon no longer carries U+FFFD and the palette icon is no longer an emoji.

## 2026-09-12 — wasm-guests

### WebAssembly Guests Example

- Added `wasm-guests/` with two presets: `wasm_showcase.jsonc` (crypto prices via HTTP, IP geolocation via component, pacman package counts via exec, `/proc` stats via fs, plus both wasm effects) and `wasm_minimal.jsonc` (the C `/proc` guest plus the matrix effect)
- Documents the install commands for every guest and the toolchains needed to build them from source (wasm32-wasip1, componentize-py, Go, clang)

## 2026-08-13 — roulette-animation-example

### Roulette Animation Example

- Added `roulette-animation-example/` — complete xfetch configuration with 6 animated ASCII logos (fox, cat, kitty, blackhole, matrix, decrypt) rotating randomly via the `config-roulette` extension
- Each figure config carries `"daemon": true`, so running `xfetch` pins the animation at the top of the terminal and loops it in the background without blocking the prompt — everything activates from the JSON, no extra shell configuration required
- Command output stays below the pinned fetch via the core's scroll-region handling; documented figure heights (tall figures like cat/matrix need a taller terminal)
- Added bilingual READMEs (`README.md` EN, `README_es.md` ES) with file → destination map, requirements (`animate-logo` plugin + `config-roulette` extension), and customization notes
