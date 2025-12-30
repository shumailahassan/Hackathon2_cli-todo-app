# Hackathon II Phase I: Todo Console App Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-31

## Active Technologies

- Python 3.13+
- uv (Package Manager)
- Typer (CLI/REPL)
- Rich (Formatting)
- Dataclasses

## Project Structure

```text
src/todo_app/
├── __init__.py
├── task.py          # Task dataclass
├── manager.py       # TodoManager class
└── main.py          # Typer REPL interface

tests/
├── unit/            # Logic tests
└── integration/     # CLI integration tests
```

## Commands

- `uv sync`: Install dependencies
- `uv run src/todo_app/main.py`: Run application
- `pytest`: Run tests

## Code Style

- Strict type hinting
- Docstrings for public methods
- Functional approach to state toggle
- Modular separation (CLI vs Logic)

## Recent Changes

- **001-phase1-basic-todo**: Initial implementation of CRUD + REPL logic.

<!-- MANUAL ADDITIONS START -->
- Use `rich.console.Console` for all printing.
- Use `rich.table.Table` for the list command.
<!-- MANUAL ADDITIONS END -->
