# Specification 001: In-Memory Console Todo App - Phase I Basic Features

## Objective
Implement a fully functional command-line Todo application with in-memory storage supporting exactly the 5 basic features required for Hackathon II Phase I.

## Required Features
1. Add task – provide title and description
2. List all tasks – display with ID, status (✅ for complete, ❌ for incomplete), title, and description
3. Update task – modify title and/or description by ID
4. Delete task – remove by ID
5. Mark as complete/incomplete – toggle status by ID

## Task Model
Use @dataclass for Task:
- id: int (auto-increment starting from 1)
- title: str
- description: str
- completed: bool = False
- created_at: datetime (import from datetime)

## Project Structure
src/todo_app/
├── __init__.py
├── task.py          # Contains Task dataclass
├── manager.py       # TodoManager class with all CRUD operations and in-memory list
└── main.py          # Typer-based interactive REPL console app

## Dependencies
- typer
- rich

## User Experience Requirements
- Interactive command loop with clear prompt
- Pretty output using Rich (colors, emojis, simple tables if possible)
- Clear success and error messages
- Graceful handling of invalid inputs (e.g., task ID not found)
- Command to quit/exit the app