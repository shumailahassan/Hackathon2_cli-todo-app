# Research: Phase I Basic Todo Console App

## Technical Choices

### CLI Framework: Typer
- **Decision**: Use `typer` for building the CLI and REPL.
- **Rationale**: Built on top of `click`, it provides excellent type hint integration and is modern and easy to use.
- **Alternatives considered**: `argparse` (too low-level), `click` (not as type-safe as Typer).

### Output Formatting: Rich
- **Decision**: Use `rich` for all console output.
- **Rationale**: Required by constitution; provides easy ways to create tables, use colors, and display emojis.
- **Alternatives considered**: `colorama` (limited features).

### Project Management: uv
- **Decision**: Use `uv` for dependency management.
- **Rationale**: Extremely fast, reliable, and compliant with modern Python standards (`pyproject.toml`).
- **Alternatives considered**: `pip` (slower), `poetry` (heavier).

## Research Findings

### REPL Implementation with Typer
- Typer is primarily designed for command-based CLI. To implement a REPL loop, we will use a while loop in `main.py` that parses input and dispatches to Typer commands or handles them directly using a simple command parser.

### In-Memory Storage
- A simple `List[Task]` inside a `TodoManager` class will suffice for storage, ensuring thread safety is not a concern for this single-user console app.

### Auto-Increment ID
- The `TodoManager` will track a `last_id` counter to ensure consistent ID generation.
