<h1 align="center">
<img src="https://raw.githubusercontent.com/xfetch-cli/assets/main/logo/banner/xfetch.svg" width="30%" alt="XFetch banner" />Configs</h1>

<p>
  <em>
    Presets, layouts and configs, collection for <strong>xfetch</strong> customisation.
  </em>
</p>

<h2>Files</h2>

<ul>
  <li><code>xfetch/</code>: presets that work with the core only.</li>
  <li><code>plugins/</code>: examples that require plugin binaries.</li>
</ul>

<ul>
  <li><code>xfetch/defaults/</code>: default config reference.</li>
  <li><code>xfetch/presets/</code>: reusable presets.</li>
  <li><code>plugins/&lt;plugin-name&gt;/</code>: plugin-specific configs.</li>
</ul>

<h2>Usage</h2>

<pre><code class="language-bash">xfetch --config /path/to/configs/xfetch/presets/layouts/layout_pacman_full.jsonc</code></pre>

<pre><code class="language-bash">cp /path/to/configs/xfetch/defaults/config.jsonc ~/.config/xfetch/config.jsonc</code></pre>

<p>
  Plugin examples depend on binaries from
  <a href="https://github.com/xfetch-cli/plugins">xfetch-cli/plugins</a>.
</p>

<p>
  Showcase presets use descriptive names so contributors can understand their
  intent without opening each file.
</p>
