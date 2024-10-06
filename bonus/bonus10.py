password = input("Enter new password: ")
assessment = {}

if len(password) >= 8:
    assessment["length"] = True
else:
    assessment["length"] = False

digit = False
upper = False

for i in password:
    if i.isdigit():
        digit = True
    if i.isupper():
        upper = True

assessment["digits"] = digit
assessment["uppercase"] = upper

if all(assessment.values()):
    print("Strong Password!")
else:
    print("Weak Password :(")
