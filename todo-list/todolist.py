def display():
    print("Menu:")
    print("1. Add a task")
    print("2. View the tasks")
    print("3. Mark as done")
    print("4. Exit")

def add_tasks(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks entered.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def mark_as_done(tasks):
    view_tasks(tasks)
    if not tasks:
        print("No tasks marked as done")
    else:
        try:
            task_number = int(input("Enter the task number to mark as done: "))
            if 1 <= task_number <= len(tasks):
                done_task = tasks.pop(task_number - 1)
                print(f"Task '{done_task}' marked as done")
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a valid number")

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        display()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_as_done(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

    

