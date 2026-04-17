# Neetcode coding

![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

[Neeetcode](https://neetcode.io/roadmap)

## Setup with uv

Create the virtual environment and install dependencies:

```bash
uv venv
source .venv/bin/activate
uv sync --dev
```

## Test coverage

Run the test suite with coverage locally:

```bash
uv run pytest
```

Coverage is configured for the Leetcode package and reported in the terminal and in coverage.xml during GitHub Actions runs.
