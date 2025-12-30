# Tasks: Phase I Basic Todo Console App

**Input**: Design documents from `/specs/001-phase1-basic-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: `src/todo_app/`, `tests/unit/`, `tests/integration/`
- [ ] T002 [P] Initialize Python project with `uv init` and add dependencies: `typer`, `rich`, `pytest`
- [ ] T003 [P] Configure `pyproject.toml` for Python 3.13+

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T004 Implement `Task` dataclass in `src/todo_app/task.py` per `data-model.md`
- [ ] T005 Implement `TodoManager` class in `src/todo_app/manager.py` with in-memory storage list
- [ ] T006 [P] Add unit tests for `Task` initialization in `tests/unit/test_task.py`
- [ ] T007 [P] Add unit tests for `TodoManager` basic operations in `tests/unit/test_manager.py`

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Task Creation (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks with title and description

- [ ] T008 [US1] Implement `TodoManager.add_task()` method in `src/todo_app/manager.py`
- [ ] T009 [US1] Add basic `add` command logic in `src/todo_app/main.py`
- [ ] T010 [US1] Verify T008 with unit tests in `tests/unit/test_manager.py`

---

## Phase 4: User Story 2 - Listing Tasks (Priority: P1)

**Goal**: Display all tasks with ID, status icon, title, and description

- [ ] T011 [US2] Implement `TodoManager.get_all_tasks()` method in `src/todo_app/manager.py`
- [ ] T012 [US2] Implement `list` command with Rich table output in `src/todo_app/main.py`
- [ ] T013 [US2] Verify T011 with unit tests in `tests/unit/test_manager.py`

---

## Phase 5: User Story 4 - Task Completion (Priority: P1)

**Goal**: Toggle task status between complete (✅) and incomplete (❌)

- [ ] T014 [US4] Implement `TodoManager.toggle_task()` method in `src/todo_app/manager.py`
- [ ] T015 [US4] Implement `toggle` command in `src/todo_app/main.py`
- [ ] T016 [US4] Verify T014 with unit tests in `tests/unit/test_manager.py`

---

## Phase 6: User Story 3 - Updating Tasks (Priority: P2)

**Goal**: Modify title or description of an existing task by ID

- [ ] T017 [US3] Implement `TodoManager.update_task()` method in `src/todo_app/manager.py`
- [ ] T018 [US3] Implement `update` command in `src/todo_app/main.py`
- [ ] T019 [US3] Verify T017 with unit tests in `tests/unit/test_manager.py`

---

## Phase 7: User Story 5 - Deleting Tasks (Priority: P2)

**Goal**: Remove a task from the list by ID

- [ ] T020 [US5] Implement `TodoManager.delete_task()` method in `src/todo_app/manager.py`
- [ ] T021 [US5] Implement `delete` command in `src/todo_app/main.py`
- [ ] T022 [US5] Verify T020 with unit tests in `tests/unit/test_manager.py`

---

## Phase 8: Polish & REPL Loop

**Purpose**: Finalize interactive loop and handle edge cases

- [ ] T023 Implement main REPL loop with `Typer` in `src/todo_app/main.py`
- [ ] T024 Add `exit`/`quit` command to the loop
- [ ] T025 Add error handling for "Task not found" (invalid ID)
- [ ] T026 Final verification of `quickstart.md` steps

---

## Dependencies & Execution Order

1. **Phase 1 & 2** are blocking.
2. **Phase 3 (Add)** should be completed before other CRUD operations to facilitate testing.
3. **Phase 4 (List)** is helpful for visual verification.
4. **Phase 8 (REPL)** wraps everything into the final interactive experience.
