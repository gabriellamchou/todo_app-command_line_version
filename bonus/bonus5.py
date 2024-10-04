new_member = input("Enter a new member: ")

file = open("files/members.txt", 'r')
file_content = file.readlines()
file.close()

file_content.append(new_member + "\n")

file = open("files/members.txt", 'w')
file_content = file.writelines(file_content)
file.close()
