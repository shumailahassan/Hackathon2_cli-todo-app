import typer
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

def show_menu():
    """Displays the stylish main menu."""
    menu_table = Table(box=box.MINIMAL_DOUBLE_HEAD, show_header=False, border_style="bright_blue")
    menu_table.add_row("[bold cyan]1.[/bold cyan] ➕ [bold white]Add new task[/bold white]")
    menu_table.add_row("[bold cyan]2.[/bold cyan] 📋 [bold white]List all tasks[/bold white]")
    menu_table.add_row("[bold cyan]3.[/bold cyan] 🔄 [bold white]Toggle task completion[/bold white]")
    menu_table.add_row("[bold cyan]4.[/bold cyan] ✏️  [bold white]Update task[/bold white]")
    menu_table.add_row("[bold cyan]5.[/bold cyan] 🗑️  [bold white]Delete task[/bold white]")
    menu_table.add_row("[bold cyan]6.[/bold cyan] 🚪 [bold red]Exit[/bold red]")

    console.print(Panel(
        menu_table,
        title="[bold yellow]Main Menu[/bold yellow]",
        border_style="bright_blue",
        padding=(0, 2)
    ))

def repl():
    """Interactive Menu-driven loop."""
    welcome_content = (
        "\n"
        "[bold cyan][u]Welcome to Todo App[/u][/bold cyan]\n"
        "[bold yellow][i]Phase I - Hackathon II Submission[/i][/bold yellow]\n\n"
        "[bold italic green]✨ Organize your day with style! ✨[/bold italic green]\n"
    )

    welcome_panel = Panel(
        welcome_content,
        box=box.ROUNDED,
        border_style="bright_magenta",
        padding=(1, 10),
        title="[bold white]🚀 STATUS: ONLINE[/bold white]",
        subtitle="[bold white]v1.0.0[/bold white]"
    )
    console.print(welcome_panel, justify="center")
    console.print()

    while True:
        show_menu()
        choice = console.input("\n[bold yellow]Select an option by number: [/bold yellow]").strip()

        try:
            if choice == "1":
                title = console.input("[bold cyan]Title: [/bold cyan]").strip()
                desc = console.input("[bold cyan]Description (optional): [/bold cyan]").strip()
                add(title, desc)
            elif choice == "2":
                list_tasks()
            elif choice == "3":
                tid = int(console.input("[bold cyan]Task ID to toggle: [/bold cyan]"))
                toggle(tid)
            elif choice == "4":
                tid = int(console.input("[bold cyan]Task ID to update: [/bold cyan]"))
                title = console.input("[bold cyan]New Title (leave empty to skip): [/bold cyan]").strip() or None
                desc = console.input("[bold cyan]New Description (leave empty to skip): [/bold cyan]").strip() or None
                update(tid, title, desc)
            elif choice == "5":
                tid = int(console.input("[bold cyan]Task ID to delete: [/bold cyan]"))
                delete(tid)
            elif choice == "6":
                console.print("\n👋 [bold yellow]Goodbye! Phase I Submitted![/bold yellow]")
                break
            else:
                console.print("❌ [bold red]Invalid option! Please enter a number between 1 and 6.[/bold red]")
        except ValueError:
            console.print("❌ [bold red]Error: Please enter a valid numerical ID where required.[/bold red]")
        except Exception as e:
            console.print(f"❌ [bold red]Unexpected error: {e}[/bold red]")

        console.print("\n" + "─" * 40 + "\n")

if __name__ == "__main__":
    repl()
