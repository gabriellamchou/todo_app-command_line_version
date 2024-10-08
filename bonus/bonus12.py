def parse(feet_inches_arg):
    parts = feet_inches_arg.split(' ')
    feet_local = parts[0]
    inches_local = parts[1]
    return {'feet': feet_local, 'inches': inches_local}


def convert(feet_arg, inches_arg):
    meters_local = feet_arg * 0.3048 + inches_arg * 0.0254
    return meters_local


feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
feet = float(parsed['feet'])
inches = float(parsed['inches'])

meters = convert(feet, inches)

print(f"They're {meters}m tall")

if meters > 1:
    print("They can use the slide")
else:
    print("They can't use the slide")
