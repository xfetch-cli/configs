# Changelog

Changes to the example xfetch configurations (`plugins/`): ready-to-use configs that combine core features with plugins and extensions.

## 2026-08-13 — roulette-animation-example

### Roulette Animation Example

- Added `roulette-animation-example/` — complete xfetch configuration with 6 animated ASCII logos (fox, cat, kitty, blackhole, matrix, decrypt) rotating randomly via the `config-roulette` extension
- Each figure config carries `"daemon": true`, so running `xfetch` pins the animation at the top of the terminal and loops it in the background without blocking the prompt — everything activates from the JSON, no extra shell configuration required
- Command output stays below the pinned fetch via the core's scroll-region handling; documented figure heights (tall figures like cat/matrix need a taller terminal)
- Added bilingual READMEs (`README.md` EN, `README_es.md` ES) with file → destination map, requirements (`animate-logo` plugin + `config-roulette` extension), and customization notes
