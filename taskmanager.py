# Define a function to add a task to the task list
def add_task(tasks, task_name, due_date):
    tasks.append({'name': task_name, 'due_date': due_date, 'completed': False})

# Define a function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Incomplete"
            print(f"{i+1}. Task: {task['name']} | Due Date: {task['due_date']} | Status: {status}")

# Define a function to mark a task as complete
def mark_complete(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

# Define a function to delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task deleted successfully.")
    else:
        print("Invalid task index.")

# Main function to drive the task manager application
def main():
    tasks = []  # List to store tasks
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, task_name, due_date)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            mark_complete(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '5':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
