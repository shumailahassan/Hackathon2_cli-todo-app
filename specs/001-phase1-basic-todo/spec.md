# Feature Specification: Phase I Basic Todo Console App

**Feature Branch**: `001-phase1-basic-todo`
**Created**: 2025-12-31
**Status**: Draft
**Input**: User description: "Implement a fully functional command-line Todo application with in-memory storage supporting exactly the 5 basic features required for Hackathon II Phase I."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Task Creation (Priority: P1)

As a user, I want to add a new task with a title and description so that I can keep track of what I need to do.

**Why this priority**: Core functionality needed to populate the app.

**Independent Test**: Can be tested by adding a task and then listing it to confirm its presence.

**Acceptance Scenarios**:

1. **Given** the app is started, **When** I add a task with title "Buy groceries" and description "Milk, eggs, bread", **Then** I should see a success message and the task should be saved to the in-memory list.
2. **Given** the app is started, **When** I add a task with an empty title, **Then** I should see an error message indicating that the title is required.

---

### User Story 2 - Listing Tasks (Priority: P1)

As a user, I want to list all my tasks so that I can see my current workload at a glance.

**Why this priority**: Essential for reviewing state and identifying tasks for other operations (Update/Delete).

**Independent Test**: Can be tested by adding multiple tasks and then listing them, ensuring all are displayed with correct details.

**Acceptance Scenarios**:

1. **Given** tasks exist in the list, **When** I trigger the list command, **Then** I should see a table/list showing ID, status (✅/❌), title, and description for each task.
2. **Given** no tasks exist, **When** I trigger the list command, **Then** I should see a message indicating the list is empty.

---

### User Story 3 - Updating Tasks (Priority: P2)

As a user, I want to update the title or description of an existing task so that I can keep the information accurate.

**Why this priority**: Necessary for maintaining tasks as details change.

**Independent Test**: Can be tested by adding a task, updating it, and then listing it to verify the changes.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** I update task 1 with a new title "Get milk", **Then** the title should be updated while the description and status remain unchanged.
2. **Given** a task with ID 1 exists, **When** I update task 1 with a new description "2% milk", **Then** the description should be updated while the title and status remain unchanged.

---

### User Story 4 - Task Completion (Priority: P1)

As a user, I want to mark a task as complete or incomplete so that I can track my progress.

**Why this priority**: Critical for the core "todo" lifecycle.

**Independent Test**: Can be tested by marking a task as complete and verifying its status icon changes in the list.

**Acceptance Scenarios**:

1. **Given** an incomplete task with ID 1, **When** I mark task 1 as complete, **Then** its status should change to ✅.
2. **Given** a complete task with ID 1, **When** I mark task 1 as incomplete, **Then** its status should change to ❌.

---

### User Story 5 - Deleting Tasks (Priority: P2)

As a user, I want to delete a task so that I can remove items I no longer need to track.

**Why this priority**: Important for list maintenance.

**Independent Test**: Can be tested by deleting a task and verifying it no longer appears in the list.

**Acceptance Scenarios**:

1. **Given** a task with ID 1 exists, **When** I delete task 1, **Then** it should be removed from the list and a success message should be shown.
2. **Given** a task with ID 1 exists, **When** I try to delete a non-existent task ID (e.g., 99), **Then** I should see an error message.

---

### Edge Cases

- **Invalid ID**: What happens when an operation (Update, Delete, Complete) refers to a non-existent task ID? System MUST display a clear "Task not found" error.
- **Empty Description**: How does the system handle an empty description? System SHOULD allow tasks with empty descriptions if a title is provided.
- **App Exit**: How does the user exit the REPL? System MUST provide a 'quit' or 'exit' command that terminates the loop gracefully.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a command-line interface with an interactive REPL loop.
- **FR-002**: System MUST use in-memory storage for tasks; all data is lost when the app exits.
- **FR-003**: System MUST auto-increment Task IDs starting from 1 for every new task added.
- **FR-004**: System MUST allow adding a task with a required title and an optional description.
- **FR-005**: System MUST display tasks in a formatted table/list showing ID, status icon (✅/❌), title, and description.
- **FR-006**: System MUST allow updating an existing task's title or description individually or together.
- **FR-007**: System MUST allow marking a task as complete (✅) or incomplete (❌).
- **FR-008**: System MUST allow deleting a task by its ID.
- **FR-009**: System MUST provide a way to exit the application.

### Key Entities

- **Task**: Represents a single item to be done.
  - Attributes: `id` (int), `title` (str), `description` (str), `completed` (bool), `created_at` (datetime).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can add a new task in under 5 seconds (single command entry).
- **SC-002**: Listing all tasks (up to 100) takes less than 1 second to render on screen.
- **SC-003**: 100% of invalid task ID lookups result in a clear "Task not found" error message rather than a crash.
- **SC-004**: Task status icons (✅/❌) correctly reflect the `completed` boolean state in todos list output.
- **SC-005**: The application exits immediately upon receiving the 'exit' or 'quit' command.
