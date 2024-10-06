possible_orders = ["add [task]", "edit", "complete", "show", "exit", "help"]

print("Type 'help' to see list of possible orders")

while True:
    user_order = input("Enter an order: ").strip().lower()
    if "add" == user_order[:3]:
        # Use list slicing to get the new task
        task = user_order[4:] + '\n'
        # Store items in todos.txt in a variable
        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        # Store new task in todos variable
        todos.append(task)
        # Overwrite todos.txt with new task included
        with open("todos.txt", 'w') as file:
            file.writelines(todos)
        print("Task added!")
    elif "edit" == user_order[:4]:
        old_task = user_order[5:]
        old_task = int(old_task) - 1

        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        todos[old_task] = input("Enter the new task: ") + '\n'

        with open("todos.txt", 'w') as file:
            file.writelines(todos)
        print("The task has been edited successfully!")
    elif "complete" == user_order[:8]:
        completed_idx = user_order[9:]
        completed_idx = int(completed_idx) - 1

        with open("todos.txt", 'r') as file:
            todos = file.readlines()
        completed_todo = todos.pop(completed_idx)

        with open("todos.txt", 'w') as file:
            file.writelines(todos)
        print("The task has been completed!")
    elif "show" == user_order:
        with open("todos.txt", 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}. {item.capitalize()}")
    elif "exit" == user_order:
        break
    elif "help" == user_order:
        print("Possible orders:")
        for order in possible_orders:
            print(f"  {order}")
    else:
        print("Order not found. Please try again")

print("Program Terminated!")
