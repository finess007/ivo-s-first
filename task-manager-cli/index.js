// Import our task manager functions
const { addTask, listTasks, completeTask, deleteTask } = require('./taskManager');

/**
 * Main entry point - handles command-line arguments
 *
 * process.argv is an array containing:
 * [0] - path to node
 * [1] - path to this file
 * [2] - first argument (command)
 * [3] - second argument (task description or ID)
 */

// Get command-line arguments
const args = process.argv.slice(2); // Remove first 2 elements
const command = args[0]; // First argument is the command
const value = args[1];   // Second argument is the value

// Handle different commands
switch (command) {
  case 'add':
    if (!value) {
      console.log('❌ Please provide a task description');
      console.log('Usage: node index.js add "Your task here"');
    } else {
      addTask(value);
    }
    break;

  case 'list':
    listTasks();
    break;

  case 'complete':
    if (!value) {
      console.log('❌ Please provide a task ID');
      console.log('Usage: node index.js complete 1');
    } else {
      completeTask(value);
    }
    break;

  case 'delete':
    if (!value) {
      console.log('❌ Please provide a task ID');
      console.log('Usage: node index.js delete 1');
    } else {
      deleteTask(value);
    }
    break;

  default:
    // Show help message if command is not recognized
    console.log('📋 Task Manager CLI\n');
    console.log('Available commands:');
    console.log('  node index.js add "task description"  - Add a new task');
    console.log('  node index.js list                    - List all tasks');
    console.log('  node index.js complete <id>           - Mark task as completed');
    console.log('  node index.js delete <id>             - Delete a task');
    console.log('\nExample:');
    console.log('  node index.js add "Buy groceries"');
}
