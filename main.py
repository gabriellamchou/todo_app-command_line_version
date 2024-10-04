possible_orders = ["add", "edit", "complete", "show", "exit", "help"]

print("Type 'help' to see list of possible orders")

while True:
    user_order = input("Enter an order: ").strip().lower()
    match user_order:
        case "add":
            # We ask user for input
            task = input("Enter a task: ") + "\n"
            # We read the file of todos
            file = open("todos.txt", 'r')
            # Store its content in a list
            todos = file.readlines()
            file.close()
            # Add the user input to that list
            todos.append(task)
            # Write the list on the file
            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()

            print("Task added!")
        case "edit":
            old_task = input("Enter the number of the task you want to edit: ")
            old_task = int(old_task) - 1

            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            todos[old_task] = input("Enter the new task: ")

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()

            print("The task has been edited successfully!")
        case "complete":
            completed_idx = input("Enter the number of the completed task: ")
            completed_idx = int(completed_idx) - 1

            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            completed_todo = todos.pop(completed_idx)

            file = open("todos.txt", 'w')
            file.writelines(todos)
            file.close()

            print("The task has been completed!")
        case "show":
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
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
