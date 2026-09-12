<h1>WebAssembly Guests Example</h1>

<p>
  These presets exercise the WebAssembly runtime end to end with real,
  user-facing information: crypto spot prices, IP geolocation, package counts
  and system load, plus both wasm effects.
</p>

<h2>Requirements</h2>

<p>
  Install the wasm guests once (from your xfetch-cli checkout):
</p>

<pre><code class="language-bash">xfetch plugin install ./plugins/plugins/wasm-crypto
xfetch plugin install ./plugins/plugins/wasm-ip-geo
xfetch plugin install ./plugins/plugins/wasm-pacman
xfetch plugin install ./plugins/plugins/wasm-proc
xfetch effects install ./effects/effects/wasm-matrix
xfetch effects install ./effects/effects/wasm-python-pulse</code></pre>

<p>
  Optional webassembly config providers used by the roulette example live in
  the extensions repository: <code>wasm-night-mode</code>,
  <code>wasm-updates-footer</code> and <code>wasm-lang-labels</code>.
</p>

<p>
  Building the Rust guest needs <code>wasm32-wasip1</code>
  (<code>rustup target add wasm32-wasip1</code>), the Python component needs
  <code>componentize-py</code>, the Go guest needs Go 1.24+ and the C guest
  needs clang with <code>wasm-ld</code>. See
  <a href="https://github.com/xfetch-cli/xfetch/blob/main/docs/WASM.md">xfetch/docs/WASM.md</a>.
</p>

<h2>Files</h2>

<ul>
  <li><code>presets/wasm_showcase.jsonc</code>: all four guests plus both effects.</li>
  <li><code>presets/wasm_minimal.jsonc</code>: the C <code>/proc</code> guest plus the matrix effect.</li>
</ul>

<h2>Usage</h2>

<pre><code class="language-bash">xfetch --config presets/wasm_showcase.jsonc</code></pre>
