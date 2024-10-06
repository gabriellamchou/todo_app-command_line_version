date = input("Enter today's date: ")
mood = input("Rate your mood today from 1 to 10: ")
thoughts = input("Let your thoughts flow: \n")

with open(f"{date}.txt", 'w') as file:
    file.writelines(f"Date: {date}\n")
    file.writelines(f"Mood: {mood}\n")
    file.writelines(f"Thoughts: \n{thoughts.capitalize()}")
