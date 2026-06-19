# BatCave AI Agent Instructions

**BatCave** is a Python 3.14+ toolkit providing cross-platform utilities for system automation, cloud management, and file operations. This guide helps AI coding agents be productive immediately.

## Quick Start

- **Test**: `vjer test` (static analysis: flake8, pylint, mypy)
- **Build**: `vjer build` (creates wheel via setuptools)
- **Unit tests**: `python -m unittest -v` or `python -m unittest tests.test_module[.test_class[.test_case]]`
- **Setup dev env**: `util\Update-Env.ps1` (Windows) or `util/update-env.sh` (Unix)

See [README.md](README.md) for details on releasing.

## Architecture Overview

BatCave is organized into functional modules in `batcave/`:

### Core Infrastructure

- **`sysutil.py`** — Subprocess wrapper (`SysCmdRunner`), file ops, lock coordination
- **`lang.py`** — Type aliases, YAML↔DotMap conversion, platform detection (`WIN32` constant)
- **`fileutil.py`** — Compression (zip/gz/bz2/xz), EOL handling, pruning

### Cloud & Kubernetes

- **`cloudmgr.py`** — Multi-cloud abstraction (local/gcloud/dockerhub via `CloudType` enum)
- **`k8s.py`** — Kubernetes ops (pods, deployments, exec/copy streams) using TypeVar polymorphism
- **`servermgr.py`** — OS-independent server management

### Git/CI & Build

- **`cms.py`** — Git/Perforce abstractions (~2000+ lines, large module)
- **`tcpy.py`** — TeamCity CI integration
- **`qbpy.py`** — QuickBuild integration
- **`automation.py`** — Build automation wrapper around `SysCmdRunner`

### Configuration & State

- **`configmgr.py`** — Config file management with inheritance
- **`data.py`** — Data sources (XML/CSV/INI/pickle/URLs)
- **`statemachine.py`** — Persistent state machine with lockfile recovery
- **`expander.py`** — String/file template expansion

### CLI & UI

- **`commander.py`** — argparse wrapper with subparser support
- **`gui.py`** — PyQt5 wrapper (Windows/Linux only; excluded on ARM)

### Utilities

- **`time.py`**, **`reporter.py`**, **`version.py`**, **`netutil.py`**, **`menu.py`**, **`platarch.py`**, **`iispy.py`** (Windows IIS management)

## Code Conventions

### Type Hints (Required)

- Use modern union syntax: `str | Path` (not `Union[]`)
- Type alias pattern: `PathName = str | Path | PurePath` (defined in `lang.py`)
- Return type on all functions: `-> None`, `-> str`, etc.
- Positional-only args: `def __init__(self, required: Type, /, *, kwarg: Type = default)`

### Error Handling

All modules define custom error classes:

```python
class XxxError(BatCaveException):
    SPECIFIC_ERROR = BatCaveError(code=1, msg=Template('Error $action: $err'))
    # BatCaveError has .code (int) and .msg (Template) for variable substitution
```

Error codes are unique per module; use `Template()` for variable substitution.

### Subprocess Execution

Always use `SysCmdRunner` (never `subprocess.run` directly):

```python
from batcave.sysutil import SysCmdRunner

runner = SysCmdRunner('kubectl', quiet=True, syscmd_args={'use_shell': WIN32})
result = runner.run('get pods')  # Returns str | List[str]
```

For one-liners: `kubectl = SysCmdRunner('kubectl').run; kubectl('version')`

### Paths (Always Use `pathlib.Path`)

```python
from pathlib import Path

# Good
config_file = Path.home() / '.config' / 'myapp' / 'config.yml'
if config_file.exists():
    content = config_file.read_text()

# Bad: string paths
# config_file = f"{os.path.expanduser('~')}/.config/myapp/config.yml"
```

### Docstrings (Google Style)

```python
def process_file(path: PathName, *, format: str = 'auto') -> str:
    """Compress or decompress a file.

    Args:
        path: File path (str, Path, or PurePath)
        format (optional, default='auto'): Compression format (auto/zip/gz/bz2/xz)

    Returns:
        Path to output file

    Raises:
        FileUtilError: If compression format unsupported
    """
```

### Platform-Specific Code

Use the `WIN32` constant from `lang.py`:

```python
from batcave.lang import WIN32

if WIN32:
    import msvcrt
else:
    import fcntl
```

Deferred imports for large deps: Place after module docstring with `# noqa:E402`.

### Linting Configuration

- **flake8** max-line-length: 200 (annotation warnings: ANN002, ANN003, ANN101, ANN204, ANN401)
- **pylint** max-line-length: 200, max-attributes: 10, max-args: 10
- **mypy** ignores: docker.*, dotmap.*
- Suppress violations inline: `# type: ignore[error]` or `# pylint: disable=...`

## Testing Conventions

- **File structure**: `tests/test_<module>.py` mirrors `batcave/<module>.py`
- **Class naming**: `Test<Feature>` (e.g., `TestLockFile`, `TestAppDirs`)
- **Method naming**: `test_<scenario>` (e.g., `test_chmod_recursive`, `test_prune_old_files`)
- **Base class**: `unittest.TestCase`
- **Output**: JUnit XML to `test_results/junit-TEST-*.xml`

Example test:

```python
from unittest import TestCase
from batcave.sysutil import get_app_data_dir
from pathlib import Path

class TestAppDirs(TestCase):
    APP_NAME = 'MyTestApp'

    def test_data_dir_returns_path(self):
        result = get_app_data_dir(self.APP_NAME)
        self.assertIsInstance(result, Path)
```

Platform-specific tests use `match` statements:

```python
from platform import system
from unittest import TestCase

class TestPlatformOps(TestCase):
    def test_platform_behavior(self):
        match system():
            case 'Windows':
                # Windows-specific assertions
            case 'Darwin':
                # macOS-specific assertions
```

## Common Patterns

### Message Enums (Domain-Specific Strings)

Use `MsgStr` for reusable message definitions with variable substitution:

```python
class Messages(MsgStr):
    BUILDING = 'Building ${target} with ${compiler}...'
    SUCCESS = 'Build completed in ${duration}s'

msg = Messages()
print(msg.BUILDING)  # Accesses _messages dict
```

### Enum Runtime Creation

For simple enums, use runtime creation instead of class:

```python
from enum import Enum
CloudType = Enum('CloudType', ('local', 'gcloud', 'dockerhub'))
# Instead of: class CloudType(Enum): local = 1; gcloud = 2; dockerhub = 3
```

### YAML Config as DotMap

Convert YAML configs to attribute-accessible objects:

```python
from batcave.lang import yaml_to_dotmap

config = yaml_to_dotmap('config.yml')
value = config.database.host  # Instead of config['database']['host']
```

### State Machine Persistence

Use `statemachine.py` for crash-recoverable workflows with lockfile coordination.

### Type Aliases in Module Scope

Define reusable types at module level (see `lang.py`):

```python
from pathlib import Path, PurePath
from typing import TypeAlias

PathName: TypeAlias = str | Path | PurePath
CommandResult: TypeAlias = str | list[str]
```

## File Organization Checklist

When adding new features:

- ✅ Add module docstring with purpose
- ✅ Group imports: stdlib → third-party → internal (with comments)
- ✅ Define module-level custom `XxxError` exception(s)
- ✅ Use type hints on all functions
- ✅ Add docstrings (Args/Returns/Raises)
- ✅ Create corresponding `tests/test_xxx.py` with unit tests
- ✅ Keep lines ≤ 200 characters
- ✅ Use `@override` decorator for method overrides (Python 3.12+)
- ✅ Use `Path` from `pathlib`, never string paths
- ✅ Wrap subprocess calls with `SysCmdRunner`

## Build & Release Workflow

The `vjer` build tool orchestrates the workflow via `vjer.yml`:

### Development

- **Run tests**: `vjer test` (flake8 → pylint → mypy → unittest)
- **Build wheel**: `vjer build` (setuptools backend)
- **Manual unittest**: `python -m unittest -v tests.test_module`

### Release (Automated via GitHub Actions)

1. Validate milestone issues
2. Update [CHANGELOG.md](CHANGELOG.md)
3. Push to `release/x.y.z` branch → triggers "Publish" workflow
4. Workflow: test PyPI → increment version → build → GitHub release → final PyPI upload

Version sourced from `batcave.__version__` (in `__init__.py`), bumped by `bumpver`.

## Dependencies & Constraints

- **Python**: 3.14+ (modern syntax: `|` unions, `match` statements, `@override`)
- **Core deps**: docker, kubernetes, GitPython, requests, PyYAML, DotMap
- **Optional**: PyQt5 (excluded on ARM64), WMI/pywin32 (Windows only)
- **Dev deps**: bumpver, vjer
- **Test deps**: flake8, pylint, mypy, unittest-xml-reporting

See `pyproject.toml` for exact versions.

## Useful References

- [README.md](README.md) — Project overview and release procedure
- [DOCUMENTATION.md](DOCUMENTATION.md) — User-facing documentation
- [CHANGELOG.md](CHANGELOG.md) — Release history
- [cliff.toml](cliff.toml) — Changelog generator config
- [vjer.yml](vjer.yml) — Build orchestration (test/build/release steps)
- `pyproject.toml` — Dependencies, metadata, tool configs (flake8, etc.)

## Troubleshooting

**Issue**: Mypy complains about docker.* or dotmap imports
**Fix**: These are in the mypy ignore list; suppress with `# type: ignore[import]` if needed.

**Issue**: Tests fail with permission errors on Windows
**Fix**: Use `LockFile` from `sysutil.py` for mutex coordination; check `WIN32` constant for platform-specific logic.

**Issue**: subprocess command fails silently
**Fix**: Check `SysCmdRunner` is used (not `subprocess.run`); enable `verbose=True` for debugging.

**Issue**: Path operations fail
**Fix**: Ensure using `pathlib.Path`, not string paths; type hints should use `PathName` alias.

<!-- cSpell:ignore cloudmgr dockerhub servermgr tcpy qbpy configmgr statemachine subparser netutil
cSpell:ignore platarch iispy kwarg syscmd pathlib myapp expanduser docstrings stdlib pywin pyproject -->
