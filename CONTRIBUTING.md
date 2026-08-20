<h1>Contributing Configs</h1>

<p>
  Thanks for contributing to the <strong>xfetch</strong> config collection.
  This repository holds presets, layouts and example configs for the core
  (<code>xfetch/</code>) and for plugins (<code>plugins/</code>).
</p>

<h2>Workflow</h2>

<ol>
  <li>Fork the repository and create a feature branch.</li>
  <li>Add or update your config in the right folder:</li>
  <li>
    <ul>
      <li><code>xfetch/defaults/</code> — the default config reference.</li>
      <li><code>xfetch/presets/layouts/</code> — layout presets (<code>layout_&lt;name&gt;[_full].jsonc</code>).</li>
      <li><code>xfetch/presets/showcase/</code> — showcase configs demonstrating modules, colors and options.</li>
      <li><code>plugins/&lt;plugin-name&gt;/</code> — configs that require a plugin binary.</li>
    </ul>
  </li>
  <li>
    Run the validation CI locally before opening the PR:
    <code>bash scripts/ci.sh</code> (Linux/macOS) or <code>./scripts/ci.ps1</code>
    (Windows). It parses every <code>.jsonc</code>/<code>.json</code> file.
  </li>
  <li>Test the config end-to-end: <code>xfetch --config &lt;path&gt;</code>.</li>
  <li>Add an entry to <a href="./CHANGELOG.md">CHANGELOG.md</a>.</li>
  <li>Open a pull request. PRs that fail validation are rejected.</li>
</ol>

<h2>Config Rules</h2>

<ul>
  <li>Files are <strong>JSONC</strong>: valid JSON plus <code>//</code> and <code>/* */</code> comments and trailing commas. They must parse cleanly.</li>
  <li>Only reference config keys the installed xfetch version supports (see the <a href="https://github.com/xfetch-cli/xfetch/blob/main/docs/CONFIGURATION.md">configuration guide</a>).</li>
  <li>Layout presets must use a valid layout name and follow the existing <code>layout_&lt;name&gt;.jsonc</code> naming.</li>
  <li>Plugin configs live under <code>plugins/&lt;plugin-name&gt;/</code> and must declare the plugin in <code>info_plugins</code> with its binary name.</li>
  <li>Keep the collection portable: no machine-specific paths, usernames or absolute paths in committed files.</li>
  <li>Prefer colors and icons from the supported names (colors: <code>Black</code>–<code>White</code> plus dark variants; icons: any text, including Nerd Font glyphs).</li>
</ul>

<h2>Code of Conduct</h2>

<p>
  Be respectful, constructive, and collaborative. Harassment, trolling, and
  personal attacks are not tolerated.
</p>
