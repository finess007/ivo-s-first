// Import the file system module to read/write files
const fs = require('fs');
const path = require('path');

// Path to our tasks database file
const TASKS_FILE = path.join(__dirname, 'tasks.json');

/**
 * Load tasks from the JSON file
 * If the file doesn't exist, return an empty array
 */
function loadTasks() {
  try {
    // Check if file exists
    if (!fs.existsSync(TASKS_FILE)) {
      return []; // No tasks yet
    }

    // Read the file and parse JSON
    const data = fs.readFileSync(TASKS_FILE, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error loading tasks:', error.message);
    return [];
  }
}

/**
 * Save tasks to the JSON file
 */
function saveTasks(tasks) {
  try {
    // Convert tasks array to JSON string (with pretty formatting)
    const data = JSON.stringify(tasks, null, 2);

    // Write to file
    fs.writeFileSync(TASKS_FILE, data, 'utf8');
  } catch (error) {
    console.error('Error saving tasks:', error.message);
  }
}

/**
 * Add a new task
 */
function addTask(description) {
  const tasks = loadTasks();

  // Create new task object
  const newTask = {
    id: tasks.length + 1, // Simple ID system
    description: description,
    completed: false,
    createdAt: new Date().toISOString()
  };

  // Add to array and save
  tasks.push(newTask);
  saveTasks(tasks);

  console.log(`✅ Task added: "${description}"`);
}

/**
 * List all tasks
 */
function listTasks() {
  const tasks = loadTasks();

  if (tasks.length === 0) {
    console.log('📋 No tasks yet! Add one with: node index.js add "Your task"');
    return;
  }

  console.log('\n📋 Your Tasks:\n');
  tasks.forEach(task => {
    const status = task.completed ? '✔️' : '⭕';
    const strikethrough = task.completed ? '\x1b[9m' : ''; // Strikethrough for completed
    const reset = '\x1b[0m'; // Reset formatting

    console.log(`${status} [${task.id}] ${strikethrough}${task.description}${reset}`);
  });
  console.log(''); // Empty line for readability
}

/**
 * Mark a task as completed
 */
function completeTask(taskId) {
  const tasks = loadTasks();
  const task = tasks.find(t => t.id === parseInt(taskId));

  if (!task) {
    console.log(`❌ Task #${taskId} not found`);
    return;
  }

  if (task.completed) {
    console.log(`ℹ️  Task #${taskId} is already completed`);
    return;
  }

  task.completed = true;
  saveTasks(tasks);

  console.log(`✔️  Completed: "${task.description}"`);
}

/**
 * Delete a task
 */
function deleteTask(taskId) {
  const tasks = loadTasks();
  const taskIndex = tasks.findIndex(t => t.id === parseInt(taskId));

  if (taskIndex === -1) {
    console.log(`❌ Task #${taskId} not found`);
    return;
  }

  const deletedTask = tasks[taskIndex];
  tasks.splice(taskIndex, 1);
  saveTasks(tasks);

  console.log(`🗑️  Deleted: "${deletedTask.description}"`);
}

// Export functions so index.js can use them
module.exports = {
  addTask,
  listTasks,
  completeTask,
  deleteTask
};
