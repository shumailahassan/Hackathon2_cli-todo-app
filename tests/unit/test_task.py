import pytest
from src.todo_app.task import Task
from datetime import datetime

def test_task_creation():
    task = Task(id=1, title="Test Task", description="Description")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Description"
    assert task.completed is False
    assert isinstance(task.created_at, datetime)

def test_task_default_description():
    task = Task(id=1, title="Test Task")
    assert task.description == ""
