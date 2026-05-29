import os
import ctypes
import sys

root = os.path.abspath(os.path.dirname(__file__))
paths = [
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'bin'),
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'gtk3', 'bin'),
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'glib', 'bin'),
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'gdk-pixbuf', 'bin'),
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'pango', 'bin'),
    os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'gobject-introspection', 'bin'),
]

for p in paths:
    print('DLL path:', p)
    if os.path.isdir(p):
        os.add_dll_directory(p)
    else:
        print('MISSING DIR:', p)

path = os.path.join(root, 'vcpkg_installed', 'x86-windows', 'tools', 'python3', 'intl-8.dll')
print('Load:', path)
try:
    ctypes.WinDLL(path)
    print('intl loaded OK')
except Exception as e:
    print('intl load failed:', e)
    sys.exit(1)

try:
    import gi
    print('gi import OK')
except Exception as e:
    print('gi import failed:', e)
    sys.exit(1)
