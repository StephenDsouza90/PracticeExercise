#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

def run_command(elements):
    num_command = int(input())

    for i in range(num_command):
        input_command = str(input())
        x = input_command.split(" ")
        command = x[0]  
    
        if command == "remove":
            value = int(x[1])
            elements.remove(value)

        if command == "discard":
            value = int(x[1])
            elements.discard(value)

        if command == "pop":
            elements.pop()

    print(sum(elements))

num_elements = int(input())
input_elements = set(map(int, input().split()))
run_command(input_elements)