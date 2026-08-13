# Roulette Animation Example

Ejemplo completo de configuración de **xfetch** con logos animados en ASCII
y rotación aleatoria (roulette) entre 6 figuras.

Este paquete incluye todo lo necesario: la config principal que activa la
roulette, las 6 configs de figuras animadas y los archivos de logos
(frames separados por `===`, consumidos por el plugin `animate-logo`).

## Requisitos

- [xfetch](https://github.com/xfetch-cli/xfetch) instalado.
- El plugin `animate-logo` instalado:
  ```bash
  xfetch plugin install animate-logo
  ```
- La extensión `config-roulette` instalada (necesaria para la rotación
  aleatoria):
  ```bash
  xfetch extension install config-roulette
  ```

## Instalación

Copiá el contenido de la carpeta `xfetch/` a tu directorio de configuración
(`~/.config/xfetch/` en Linux), **respetando la estructura de carpetas**:

```bash
cp -r xfetch/* ~/.config/xfetch/
```

### Mapa de archivos → destino

| Archivo en este paquete                              | Debe ir en                                |
| ---------------------------------------------------- | ----------------------------------------- |
| `xfetch/config.jsonc`                                | `~/.config/xfetch/config.jsonc`           |
| `xfetch/routes-anim.json`                            | `~/.config/xfetch/routes-anim.json`       |
| `xfetch/fetchs/animations/fox/config.jsonc`          | `~/.config/xfetch/fetchs/animations/fox/config.jsonc` |
| `xfetch/fetchs/animations/cat/config.jsonc`          | `~/.config/xfetch/fetchs/animations/cat/config.jsonc` |
| `xfetch/fetchs/animations/kitty/config.jsonc`        | `~/.config/xfetch/fetchs/animations/kitty/config.jsonc` |
| `xfetch/fetchs/animations/blackhole/config.jsonc`    | `~/.config/xfetch/fetchs/animations/blackhole/config.jsonc` |
| `xfetch/fetchs/animations/matrix/config.jsonc`       | `~/.config/xfetch/fetchs/animations/matrix/config.jsonc` |
| `xfetch/fetchs/animations/decrypt/config.jsonc`      | `~/.config/xfetch/fetchs/animations/decrypt/config.jsonc` |
| `xfetch/logos/animations/*.txt`                      | `~/.config/xfetch/logos/animations/`      |

## Cómo funciona

### Config principal (`config.jsonc`)

Activa la extensión `config-roulette` con estrategia aleatoria. Cada vez que
corrés `xfetch`, elige una config al azar de `routes-anim.json`:

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

### Rutas de la roulette (`routes-anim.json`)

Lista las 6 configs animadas que participan en la rotación:

| Nombre             | Figura                              |
| ------------------ | ----------------------------------- |
| `001-animate-fox`  | Zorro corriendo (convertido de GIF) |
| `002-animate-cat`  | Gato parpadeando                    |
| `003-animate-kitty`| Kitty girando la cabeza (GIF)       |
| `004-animate-blackhole` | Agujero negro (GIF)            |
| `005-animate-matrix`    | Lluvia Matrix                  |
| `006-animate-decrypt`   | Panel "DECRYPTING"             |

### Configs de figuras

Cada config en `fetchs/animations/<figura>/config.jsonc` apunta a su archivo
de animación con el bloque `logo_animation` (estilo `frame`) y usa un layout
distinto:

| Figura     | Layout      | Ícono de OS |
| ---------- | ----------- | ----------- |
| fox        | `pacman`    | `` (terminal) |
| cat        | `box`       | `` (terminal) |
| kitty      | `section`   | `` (linux)    |
| blackhole  | `tree`      | ``             |
| matrix     | `compact`   | `` (arch)     |
| decrypt    | `side-block`| `` (terminal) |

### Archivos de logos

En `logos/animations/`, cada figura tiene dos archivos:

- `<figura>.txt` — la **animación**: frames separados por una línea `===`.
- `<figura>_static.txt` — **frame estático** (fallback cuando no hay TTY).

Los `.txt` son consumidos por el plugin `animate-logo` vía `frames_path`
(animación) y `ascii` (estático).

## Probar

Después de copiar los archivos:

```bash
xfetch
```

La animación solo corre en terminales TTY (interactivas). En redirecciones o
pipes se muestra el logo estático.

## Personalizar

- **Agregar una figura nueva**: creá su `.txt` (frames separados por `===`),
  su `_static.txt`, una config en `fetchs/animations/<nombre>/` y agregá la
  entrada en `routes-anim.json`.
- **Ajustar velocidad**: cambiá `fps` en el bloque `logo_animation` de cada
  config.
- **Quitar la roulette**: apuntá `routes` en `config.jsonc` a un archivo con
  una sola config, o usá `xfetch --config <ruta>` directamente.
