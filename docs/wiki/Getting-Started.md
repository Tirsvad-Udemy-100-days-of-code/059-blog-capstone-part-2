**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Requirements

- Python 3.13 or newer
- Git
- Doxygen (optional, only for the API documentation)

## Create and use a local virtual environment

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Linux and macOS use `python3 -m venv .venv` and `source .venv/bin/activate`. Leave the environment with `deactivate`.

## Run the site

```bash
python -m blog.main
```

Open <http://127.0.0.1:5000>. The posts come from the endpoint in `src/blog/constants.py`; if it cannot be reached, the copy bundled in the package is used.

## Run the tests

```bash
python -m pytest
```

The tests never use the network. Build the code documentation with `doxygen Doxyfile`.

## What we gained

- A repeatable setup: a virtual environment, `pip` upgraded, the project installed in editable mode.
- One command to run the site and one to run the tests, both written in the README.
