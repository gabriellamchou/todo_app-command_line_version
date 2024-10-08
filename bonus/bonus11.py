def strength(password):
    assessment = {}
    uppercase = False
    digit = False
    if len(password) >= 8:
        assessment["length"] = True
    else:
        assessment["length"] = False
    for char in password:
        if char.isupper():
            uppercase = True
    assessment["uppercase"] = uppercase
    for char in password:
        if char.isdigit():
            digit = True
    assessment["digit"] = digit

    if all(assessment.values()):
        return True
    else:
        return False


userpass = input("Enter a new password: ")
if strength(userpass):
    print("Strong Password!")
else:
    print("Weak Password :(")
