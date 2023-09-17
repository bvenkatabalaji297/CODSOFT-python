class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.title} ({status}): {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def mark_task_completed(self, task_index):
        if task_index >= 1 and task_index <= len(self.tasks):
            self.tasks[task_index - 1].mark_completed()
        else:
            print("Invalid task index")

def main():
    to_do_list = ToDoList()
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "4":
            break
        elif choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            to_do_list.add_task(task)
            print("Task added successfully.")
        elif choice == "2":
            to_do_list.view_tasks()
        elif choice == "3":
            to_do_list.view_tasks()
            task_index = int(input("Enter the task number to mark as completed: "))
            to_do_list.mark_task_completed(task_index)
            print("Task marked as completed.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
