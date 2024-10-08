def calculate_time(h, g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)

# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# try:
#     number = waiting_list.index(name)
#     print(f"{name}'s turn is {number}")
# except ValueError:
#     print(f"{name} is not on the list")

# date = input("Enter today's date: ")
# mood = input("Rate your mood today from 1 to 10: ")
# thoughts = input("Let your thoughts flow: \n")
#
# with open(f"{date}.txt", 'w') as file:
#     file.writelines(f"Date: {date}\n")
#     file.writelines(f"Mood: {mood}\n")
#     file.writelines(f"Thoughts: \n{thoughts.capitalize()}")
