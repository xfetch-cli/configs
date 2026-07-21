# Animate Logo Example

<p>
  This example combines a Pac-Man style layout with the official
  <code>animate-logo</code> plugin from
  <a href="https://github.com/xfetch-cli/plugins">xfetch-cli/plugins</a>.
</p>

<h2>Files</h2>

<ul>
  <li><code>presets/xfetch_pacman_animate.jsonc</code>: example config file.</li>
</ul>

<h2>Requirements</h2>

<ol>
  <li>Install <code>xfetch</code>.</li>
  <li>Install the official plugin: <code>xfetch plugin install animate-logo</code>.</li>
  <li>Place the logo file referenced by the config under your local xfetch logos directory.</li>
</ol>

<h2>Run</h2>

<pre><code class="language-bash">xfetch --config /path/to/configs/plugins/animate-logo/presets/xfetch_pacman_animate.jsonc</code></pre>

<p>
  The animation runs only in TTY terminals.
</p>
