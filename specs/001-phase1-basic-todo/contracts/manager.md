# Internal API Contracts: TodoManager

The `TodoManager` class handles all business logic and in-memory state.

## Methods

### `add_task(title: str, description: str = "") -> Task`
- **Input**: Title and optional description.
- **Output**: The newly created `Task` object.
- **Behavior**: Increments inner ID counter, sets `created_at`, adds to internal list.

### `get_all_tasks() -> List[Task]`
- **Output**: List of all `Task` objects.

### `update_task(task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task`
- **Input**: ID and optional update fields.
- **Output**: The updated `Task` object.
- **Errors**: `ValueError` if task ID not found.

### `delete_task(task_id: int) -> None`
- **Input**: ID of the task to remove.
- **Errors**: `ValueError` if task ID not found.

### `toggle_task(task_id: int) -> Task`
- **Input**: ID of the task to toggle.
- **Output**: The updated `Task` object with flipped `completed` status.
- **Errors**: `ValueError` if task ID not found.
