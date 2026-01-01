"""
Task Manager Core Logic

This module contains all the functions to manage tasks:
- Load and save tasks from/to JSON file
- Add, list, complete, and delete tasks
"""

import json
import os
from datetime import datetime

# Path to our tasks database file
TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')


def load_tasks():
    """
    Load tasks from the JSON file.
    If the file doesn't exist, return an empty list.

    Returns:
        list: List of task dictionaries
    """
    try:
        # Check if file exists
        if not os.path.exists(TASKS_FILE):
            return []  # No tasks yet

        # Read the file and parse JSON
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as error:
        print(f'Error loading tasks: {error}')
        return []


def save_tasks(tasks):
    """
    Save tasks to the JSON file.

    Args:
        tasks (list): List of task dictionaries to save
    """
    try:
        # Convert tasks list to JSON string (with pretty formatting)
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
    except Exception as error:
        print(f'Error saving tasks: {error}')


def add_task(description):
    """
    Add a new task.

    Args:
        description (str): The task description
    """
    tasks = load_tasks()

    # Create new task dictionary
    new_task = {
        'id': len(tasks) + 1,  # Simple ID system
        'description': description,
        'completed': False,
        'createdAt': datetime.now().isoformat()
    }

    # Add to list and save
    tasks.append(new_task)
    save_tasks(tasks)

    print(f'✅ Task added: "{description}"')


def list_tasks():
    """
    List all tasks with their status.
    """
    tasks = load_tasks()

    if len(tasks) == 0:
        print('📋 No tasks yet! Add one with: python3 main.py add "Your task"')
        return

    print('\n📋 Your Tasks:\n')
    for task in tasks:
        status = '✔️' if task['completed'] else '⭕'

        # Strikethrough for completed tasks (using ANSI escape codes)
        if task['completed']:
            description = f"\033[9m{task['description']}\033[0m"
        else:
            description = task['description']

        print(f"{status} [{task['id']}] {description}")

    print()  # Empty line for readability


def complete_task(task_id):
    """
    Mark a task as completed.

    Args:
        task_id (str): The ID of the task to complete
    """
    tasks = load_tasks()

    # Convert task_id to integer
    try:
        task_id = int(task_id)
    except ValueError:
        print(f'❌ Invalid task ID: {task_id}')
        return

    # Find the task
    task = next((t for t in tasks if t['id'] == task_id), None)

    if task is None:
        print(f'❌ Task #{task_id} not found')
        return

    if task['completed']:
        print(f'ℹ️  Task #{task_id} is already completed')
        return

    task['completed'] = True
    save_tasks(tasks)

    print(f'✔️  Completed: "{task["description"]}"')


def delete_task(task_id):
    """
    Delete a task.

    Args:
        task_id (str): The ID of the task to delete
    """
    tasks = load_tasks()

    # Convert task_id to integer
    try:
        task_id = int(task_id)
    except ValueError:
        print(f'❌ Invalid task ID: {task_id}')
        return

    # Find the task index
    task_index = next((i for i, t in enumerate(tasks) if t['id'] == task_id), None)

    if task_index is None:
        print(f'❌ Task #{task_id} not found')
        return

    deleted_task = tasks[task_index]
    tasks.pop(task_index)
    save_tasks(tasks)

    print(f'🗑️  Deleted: "{deleted_task["description"]}"')
