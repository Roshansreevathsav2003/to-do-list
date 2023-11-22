class Task:
    def _init_(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def _init_(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Completed: {task.completed}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            task.completed = True
            self.completed_tasks.append(task)
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def update_task(self, task_index, description, due_date, priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description
            task.due_date = due_date
            task.priority = priority
            print("Task updated.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task removed: {removed_task.description}")
        else:
            print("Invalid task index.")

    def view_completed_tasks(self):
        if not self.completed_tasks:
            print("No completed tasks.")
        else:
            print("Completed Tasks:")
            for i, task in enumerate(self.completed_tasks, 1):
                print(f"{i}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}")

# Main program loop
todo_list = ToDoList()

while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Update a task")
    print("5. Remove a task")
    print("6. View completed tasks")
    print("7. Quit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        due_date = input("Enter due date: ")
        priority = input("Enter priority: ")
        todo_list.add_task(description, due_date, priority)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        todo_list.view_tasks()
        task_index = int(input("Enter the task index to mark as completed: "))
        todo_list.mark_task_completed(task_index)
    elif choice == "4":
        todo_list.view_tasks()
        task_index = int(input("Enter the task index to update: "))
        description = input("Enter updated description: ")
        due_date = input("Enter updated due date: ")
        priority = input("Enter updated priority: ")
        todo_list.update_task(task_index, description, due_date, priority)
    elif choice == "5":
        todo_list.view_tasks()
        task_index = int(input("Enter the task index to remove: "))
        todo_list.remove_task(task_index)
    elif choice == "6":
        todo_list.view_completed_tasks()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
