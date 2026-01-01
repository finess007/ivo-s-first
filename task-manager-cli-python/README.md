# Task Manager CLI (Python Version)

A simple command-line task manager to help you organize your todos.

## Features

- ✅ Add new tasks
- 📋 List all tasks
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks

## Requirements

- Python 3.6 or higher (no external dependencies needed!)

## Installation

1. Make sure you have Python installed: `python3 --version`
2. Navigate to this folder in your terminal
3. You're ready to go! (No pip install needed)

## Usage

### Add a task
```bash
python3 main.py add "Buy groceries"
```

### List all tasks
```bash
python3 main.py list
```

### Complete a task (use the task number from list)
```bash
python3 main.py complete 1
```

### Delete a task
```bash
python3 main.py delete 1
```

## How It Works

- Tasks are stored in `tasks.json` file
- Each task has an ID, description, and completion status
- The file is created automatically when you add your first task

## Comparison with Node.js Version

Both versions do the same thing! Compare the code to see:
- **Python**: More concise, uses `import sys`, `import json`
- **Node.js**: Uses `require()`, `module.exports`, `process.argv`

## Learning Goals

This project teaches:
- Command-line argument parsing (`sys.argv`)
- File operations (JSON read/write)
- List and dictionary manipulation
- Basic CRUD operations
- Exception handling with try/except
