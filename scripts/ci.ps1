# Local CI: run before committing (Windows PowerShell).
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "==> validate JSON/JSONC"
python validate.py ..
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host "==> CI OK"
