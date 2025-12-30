# Data Model: Phase I Basic Todo Console App

## Entities

### Task (Dataclass)
- Represents a single todo item.
- **Fields**:
  - `id`: `int` (Auto-increment, starts at 1)
  - `title`: `str` (Required, non-empty)
  - `description`: `str` (Optional, defaults to empty string)
  - `completed`: `bool` (Defaults to `False`)
  - `created_at`: `datetime` (Auto-set on creation)

## State Transitions
- **Created**: `completed=False`
- **Toggled**: `completed` value is flipped (`True` -> `False` or `False` -> `True`)
- **Deleted**: Task is removed from the in-memory list.
