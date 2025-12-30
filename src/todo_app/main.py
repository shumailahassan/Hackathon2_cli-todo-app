import typer
from rich.console import Console
from rich.table import Table
from typing import Optional
from .manager import TodoManager

app = typer.Typer()
console = Console()
manager = TodoManager()

@app.command()
def add(title: str, description: str = ""):
    """Add a new task."""
    try:
        task = manager.add_task(title, description)
        console.print(f"[green]Added task {task.id}: {task.title}[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command(name="list")
def list_tasks():
    """List all tasks."""
    tasks = manager.get_all_tasks()
    if not tasks:
        console.print("[yellow]No tasks found.[/yellow]")
        return

    table = Table(title="Todo List")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Status", justify="center")
    table.add_column("Title", style="magenta")
    table.add_column("Description", style="white")

    for task in tasks:
        status = "✅" if task.completed else "❌"
        table.add_row(str(task.id), status, task.title, task.description)

    console.print(table)

@app.command()
def toggle(task_id: int):
    """Toggle task status by ID."""
    try:
        task = manager.toggle_task(task_id)
        status = "complete" if task.completed else "incomplete"
        console.print(f"[green]Marked task {task.id} as {status}.[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def update(
    task_id: int,
    title: Optional[str] = typer.Option(None, "--title", "-t"),
    description: Optional[str] = typer.Option(None, "--desc", "-d")
):
    """Update task title or description."""
    try:
        manager.update_task(task_id, title, description)
        console.print(f"[green]Updated task {task_id}.[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

@app.command()
def delete(task_id: int):
    """Delete task by ID."""
    try:
        manager.delete_task(task_id)
        console.print(f"[green]Deleted task {task_id}.[/green]")
    except ValueError as e:
        console.print(f"[red]Error: {e}[/red]")

def repl():
    """Interactive REPL loop."""
    console.print("[bold blue]Welcome to the Todo App REPL![/bold blue]")
    console.print("Type 'exit' or 'quit' to leave.")

    while True:
        try:
            command_input = console.input("[bold cyan]todo>[/bold cyan] ").strip()
            if not command_input:
                continue

            if command_input.lower() in ("exit", "quit"):
                console.print("[yellow]Goodbye![/yellow]")
                break

            # Simple command parsing for the REPL
            import shlex
            args = shlex.split(command_input)
            app(args)
        except SystemExit:
            # Typer and Click exit the process on help/error; we need to catch it to keep REPL alive
            continue
        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")

if __name__ == "__main__":
    repl()
