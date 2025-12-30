from typing import List, Optional
from .task import Task

class TodoManager:
    def __init__(self):
        self.tasks: List[Task] = []
        self._last_id: int = 0

    def add_task(self, title: str, description: str = "") -> Task:
        if not title:
            raise ValueError("Title is required")
        self._last_id += 1
        task = Task(id=self._last_id, title=title, description=description)
        self.tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")

        if title is not None:
            if not title:
                raise ValueError("Title cannot be empty")
            task.title = title
        if description is not None:
            task.description = description
        return task

    def delete_task(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        self.tasks.remove(task)

    def toggle_task(self, task_id: int) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        task.completed = not task.completed
        return task
