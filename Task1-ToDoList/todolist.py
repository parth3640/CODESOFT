tasks = []

def view_tasks():
    if not tasks:
        print("\nNo tasks found.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def update_task():
    view_tasks()
    try:
        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(tasks):
            new_title = input("Enter new task title: ")
            tasks[idx]["title"] = new_title
            print("Task updated.")
    except:
        print("Invalid input.")

def mark_done():
    view_tasks()
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Task marked as done.")
    except:
        print("Invalid input.")

def main():
    while True:
        print("\n1. View\n2. Add\n3. Update\n4. Mark Done\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()