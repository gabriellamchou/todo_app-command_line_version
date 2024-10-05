possible_orders = ["add", "edit", "complete", "show", "exit", "help"]

print("Type 'help' to see list of possible orders")

while True:
    user_order = input("Enter an order: ").strip().lower()
    match user_order:
        case "add":
            # Prompt user to enter new task
            task = input("Enter a task: ") + "\n"
            # Store items in todos.txt in a variable
            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            # Store new task in todos variable
            todos.append(task)
            # Overwrite todos.txt with new task included
            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print("Task added!")
        case "edit":
            old_task = input("Enter the number of the task you want to edit: ")
            old_task = int(old_task) - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            todos[old_task] = input("Enter the new task: ") + '\n'

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print("The task has been edited successfully!")
        case "complete":
            completed_idx = input("Enter the number of the completed task: ")
            completed_idx = int(completed_idx) - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()
            completed_todo = todos.pop(completed_idx)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
            print("The task has been completed!")
        case "show":
            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{index + 1}. {item.capitalize()}")
        case "exit":
            break
        case "help":
            print("Possible orders:")
            for order in possible_orders:
                print(f"  {order}")
        case _:
            print("Order not found. Please try again")

print("Program Terminated!")
