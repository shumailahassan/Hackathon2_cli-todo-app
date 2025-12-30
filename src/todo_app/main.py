import typer
import shlex
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from typing import Optional
from .manager import TodoManager

app = typer.Typer()
console = Console()
manager = TodoManager()

@app.command()
def add(title: str, description: str = ""):
    """Add a new task."""
    try:
        manager.add_task(title, description)
        console.print("✅ [bold green]Task added![/bold green]")
    except ValueError as e:
        console.print(f"❌ [bold red]{e}[/bold red]")

@app.command(name="list")
def list_tasks():
    """List all tasks."""
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(
        title="[bold blue]Current Tasks[/bold blue]",
        box=box.ROUNDED,
        header_style="bold magenta",
        title_style="bold blue"
    )
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center")
    table.add_column("Title", style="bold white")
    table.add_column("Description", style="italic white")

    for task in tasks:
        status = "✅" if task.completed else "❌"
        table.add_row(str(task.id), status, task.title, task.description)

    console.print(table)

@app.command()
def toggle(task_id: int):
    """Toggle task status by ID."""
    try:
        manager.toggle_task(task_id)
        console.print("🔄 [bold green]Status toggled![/bold green]")
    except ValueError:
        console.print("❌ [bold red]Task not found![/bold red]")

@app.command()
def update(
    task_id: int,
    title: Optional[str] = typer.Option(None, "--title", "-t"),
    description: Optional[str] = typer.Option(None, "--desc", "-d")
):
    """Update task title or description."""
    try:
        manager.update_task(task_id, title, description)
        console.print("✏️ [bold green]Task updated![/bold green]")
    except ValueError:
        console.print("❌ [bold red]Task not found![/bold red]")

@app.command()
def delete(task_id: int):
    """Delete task by ID."""
    try:
        manager.delete_task(task_id)
        console.print("🗑️ [bold green]Task deleted![/bold green]")
    except ValueError:
        console.print("❌ [bold red]Task not found![/bold red]")

def repl():
    """Interactive REPL loop."""
    welcome_panel = Panel.fit(
        "[bold blue]Hackathon II Phase I[/bold blue]\n"
        "[bold cyan]Todo Console App[/bold cyan]\n\n"
        "✨ [green]Ready to organize your day![/green]",
        box=box.DOUBLE,
        border_style="bright_blue",
        padding=(1, 2)
    )
    console.print(welcome_panel)
    console.print("[italic]Type 'exit' or 'quit' to leave.[/italic]\n")

    while True:
        try:
            command_input = console.input("[bold cyan]todo>[/bold cyan] ").strip()
            if not command_input:
                continue

            if command_input.lower() in ("exit", "quit"):
                console.print("\n👋 [bold yellow]Goodbye! Phase I Submitted![/bold yellow]")
                break

            args = shlex.split(command_input)
            app(args)
        except SystemExit:
            continue
        except Exception as e:
            console.print(f"❌ [bold red]Unexpected error: {e}[/bold red]")

if __name__ == "__main__":
    repl()
