import pytest
from src.todo_app.manager import TodoManager

@pytest.fixture
def manager():
    return TodoManager()

def test_add_task(manager):
    task = manager.add_task("Test Title", "Test Description")
    assert task.id == 1
    assert task.title == "Test Title"
    assert len(manager.tasks) == 1

def test_add_task_empty_title(manager):
    with pytest.raises(ValueError, match="Title is required"):
        manager.add_task("")

def test_get_all_tasks(manager):
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    assert len(manager.get_all_tasks()) == 2

def test_update_task(manager):
    task = manager.add_task("Old Title")
    updated = manager.update_task(task.id, title="New Title", description="New Desc")
    assert updated.title == "New Title"
    assert updated.description == "New Desc"

def test_delete_task(manager):
    task = manager.add_task("Delete me")
    manager.delete_task(task.id)
    assert len(manager.tasks) == 0

def test_toggle_task(manager):
    task = manager.add_task("Toggle me")
    manager.toggle_task(task.id)
    assert task.completed is True
    manager.toggle_task(task.id)
    assert task.completed is False
