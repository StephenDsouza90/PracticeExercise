arr = []

number_of_command = int(input())

for i in range(number_of_command):
    input_which_command = str(input())
    x = input_which_command.split(" ")
    command = x[0]

    if command == "insert":
        index = int(x[1])
        value = int(x[2])
        arr.insert(index, value)

    if command == "print":
        print(arr)

    if command == "remove":
        value = int(x[1])
        arr.remove(value)

    if command == "append":
        value = int(x[1])
        arr.append(value)

    if command == "sort":
        arr.sort()

    if command == "pop":
        arr.pop()

    if command == "reverse":
        arr.reverse()