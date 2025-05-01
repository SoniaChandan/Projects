""" Program to view, add and remove 
tasks from a To do list """


# Function to display a menu

def display_menu():
    print("\n=== To do List ===")
    print("1. View all your tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Exit")


# Function to View all tasks
def view_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks in your to do list")
    else:
        print("\n=== Your To Do List ===")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


# Function to add tasks
def add_tasks(tasks):
    task = input("\nEnter the task you want to add: ")
    tasks.append(task)
    print(f"Your new task '{task}' has been added successfully")


def remove_task(tasks):
    if len(tasks) == 0:
        print("\nNo tasks to remove")
    else:
        view_tasks(tasks)
        try:
            task_num = int(
                input("\nEnter the task number you want to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Removed task '{removed_task}' from your To do List")
            else:
                print("\nInvalid Task Number")
        except ValueError:
            print("Please enter a valid number")


# Main Program to run the applications
def main():
    tasks = []  # List to store tasks
    while True:
        display_menu()  # Display Menu
        try:
            choice = int(input("\nSelect an option (1-4): "))
            if choice == 1:
                view_tasks(tasks)
            elif choice == 2:
                add_tasks(tasks)
            elif choice == 3:
                remove_task(tasks)
            elif choice == 4:
                print("\nGoodbye! Have a productive day!")
                break
            else:
                print("\nInvalid option. Please select again.")
        except ValueError:
            print("\n Please enter valid number between 1 and 4")


# Run the Program
if __name__ == "__main__":
    main()
