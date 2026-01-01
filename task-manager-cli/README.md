# Task Manager CLI

A simple command-line task manager to help you organize your todos.

## Features

- ✅ Add new tasks
- 📋 List all tasks
- ✔️ Mark tasks as completed
- 🗑️ Delete tasks

## Installation

1. Make sure you have Node.js installed (version 14 or higher)
2. Navigate to this folder in your terminal
3. Run: `npm install` (currently no dependencies needed)

## Usage

### Add a task
```bash
node index.js add "Buy groceries"
```

### List all tasks
```bash
node index.js list
```

### Complete a task (use the task number from list)
```bash
node index.js complete 1
```

### Delete a task
```bash
node index.js delete 1
```

## How It Works

- Tasks are stored in `tasks.json` file
- Each task has an ID, description, and completion status
- The file is created automatically when you add your first task

## Learning Goals

This project teaches:
- Command-line argument parsing
- File operations (read/write JSON)
- Array manipulation
- Basic CRUD operations
