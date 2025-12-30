# Project Constitution - Hackathon II Phase I: In-Memory Todo Console App

1. Strictly Spec-Driven Development using Spec-Kit Plus and Claude Code
2. No manual coding allowed – all code must be generated via /specify or /sp slash commands
3. In-memory storage only (no files, no database, no persistence)
4. Use Python 3.13+ with UV as package manager
5. Clean code principles: type hints, docstrings, modular design
6. Console application using Typer for CLI and Rich for pretty output (colors, emojis)
7. Implement exactly the 5 basic features:
   - Add task with title and description
   - List all tasks with ID, status (✅/❌), title, description
   - Update task title/description by ID
   - Delete task by ID
   - Mark task as complete/incomplete by ID
8. Interactive REPL loop with clear command prompt and feedback
9. All artifacts (specs, plans, tasks, prompt history) must be preserved in .specify/ folder
10. Use dataclass for Task model with auto-increment ID