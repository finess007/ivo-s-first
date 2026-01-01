#!/usr/bin/env python3
"""
Task Manager CLI - Main Entry Point

This is the entry point for the task manager application.
It handles command-line arguments and calls the appropriate functions.
"""

import sys
from task_manager import add_task, list_tasks, complete_task, delete_task


def show_help():
    """Display help message with available commands."""
    print('📋 Task Manager CLI\n')
    print('Available commands:')
    print('  python3 main.py add "task description"  - Add a new task')
    print('  python3 main.py list                    - List all tasks')
    print('  python3 main.py complete <id>           - Mark task as completed')
    print('  python3 main.py delete <id>             - Delete a task')
    print('\nExample:')
    print('  python3 main.py add "Buy groceries"')


def main():
    """
    Main function - handles command-line arguments.

    sys.argv is a list containing:
    [0] - path to this script
    [1] - first argument (command)
    [2] - second argument (task description or ID)
    """

    # Get command-line arguments (skip the first one which is the script name)
    args = sys.argv[1:]

    # Check if we have at least one argument (the command)
    if len(args) == 0:
        show_help()
        return

    command = args[0]  # First argument is the command

    # Handle different commands
    if command == 'add':
        if len(args) < 2:
            print('❌ Please provide a task description')
            print('Usage: python3 main.py add "Your task here"')
        else:
            # Join all remaining arguments as the task description
            # This allows tasks with spaces even without quotes
            description = ' '.join(args[1:])
            add_task(description)

    elif command == 'list':
        list_tasks()

    elif command == 'complete':
        if len(args) < 2:
            print('❌ Please provide a task ID')
            print('Usage: python3 main.py complete 1')
        else:
            complete_task(args[1])

    elif command == 'delete':
        if len(args) < 2:
            print('❌ Please provide a task ID')
            print('Usage: python3 main.py delete 1')
        else:
            delete_task(args[1])

    else:
        # Unknown command - show help
        print(f'❌ Unknown command: {command}\n')
        show_help()


# This is the Python equivalent of "if this file is run directly"
# (not imported as a module)
if __name__ == '__main__':
    main()
