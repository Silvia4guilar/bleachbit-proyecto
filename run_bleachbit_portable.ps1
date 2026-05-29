$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$gtkPaths = @(
    "$root\vcpkg_installed\x86-windows\bin",
    "$root\vcpkg_installed\x86-windows\tools\gtk3\bin",
    "$root\vcpkg_installed\x86-windows\tools\glib\bin",
    "$root\vcpkg_installed\x86-windows\tools\gdk-pixbuf\bin",
    "$root\vcpkg_installed\x86-windows\tools\pango\bin",
    "$root\vcpkg_installed\x86-windows\tools\gobject-introspection\bin"
)
$env:PATH = ($gtkPaths -join ';') + ';' + $env:PATH
$python = Join-Path $root 'vcpkg_installed\x86-windows\tools\python3\python.exe'
$script = Join-Path $root 'bleachbit.py'
& $python $script --help
