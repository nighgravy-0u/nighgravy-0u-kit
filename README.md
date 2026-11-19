# nighgravy-0u-kit

Sort a folder of files into per-type subfolders.

Small, dependency-free Python utility package generated for day-to-day file chores.
Standard library only — no third-party imports.

## Install

```bash
pip install -e .
```

## Usage

```bash
python -m nighgravy_0u_kit.cli --help
```

```python
from nighgravy_0u_kit.core import Nighgravy0uTool

tool = Nighgravy0uTool()
print(tool)
```

## Layout

```
nighgravy_0u_kit/
  __init__.py
  core.py
  cli.py
tests/
  test_core.py
```

## License

MIT © 2026 nighgravy-0u
