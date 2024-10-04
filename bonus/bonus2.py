waiting_list = ["sen", "ben", "john"]

waiting_list.sort()

for idx, client in enumerate(waiting_list):
    print(f"{idx + 1}.{client.capitalize()}")
