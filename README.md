Title: Basic Task Manager Documentation

Introduction:
The Basic Task Manager is a simple command-line application built in Python. It allows users to manage tasks by performing CRUD (Create, Read, Update, Delete) operations. Users can add tasks with descriptions and due dates, view existing tasks, mark tasks as complete, and delete tasks.

Functions:
1. add_task(tasks, task_name, due_date):
   - Description: Adds a new task to the task list.
   - Parameters:
     - tasks (list): List of tasks.
     - task_name (str): Name of the task.
     - due_date (str): Due date of the task in "YYYY-MM-DD" format.
   - Returns: None

2. view_tasks(tasks):
   - Description: Displays all tasks along with their details.
   - Parameters:
     - tasks (list): List of tasks.
   - Returns: None

3. mark_complete(tasks, task_index):
   - Description: Marks a task as complete based on its index.
   - Parameters:
     - tasks (list): List of tasks.
     - task_index (int): Index of the task to mark as complete (1-indexed).
   - Returns: None

4. delete_task(tasks, task_index):
   - Description: Deletes a task based on its index.
   - Parameters:
     - tasks (list): List of tasks.
     - task_index (int): Index of the task to delete (1-indexed).
   - Returns: None

5. main():
   - Description: Main function to drive the task manager application.
   - Implements a menu-driven interface allowing users to perform various operations on tasks.
   - Returns: None

Usage:
1. Import the task_manager module.
2. Call the main() function to start the task manager application.
3. Follow the on-screen prompts to add, view, mark as complete, and delete tasks.

Example:
```python
import task_manager

# Start the task manager application
task_manager.main()
Notes:

    Ensure task due dates are provided in "YYYY-MM-DD" format.
    Task indices are 1-indexed (the first task has index 1).
    Invalid inputs are handled gracefully, providing appropriate error messages
