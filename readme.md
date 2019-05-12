# Simulating rpath on Windows

- Start a VS command shell
- Run `python buildrpath.py`
- `cd builddir`
- run `prog.exe`

To see how this works, open `builddir/prog.exe` with a hex editor and
search for `helper.dll`.
