#https://www.hackerrank.com/challenges/exceptions/problem

def find_error(test_cases):

    for cases in range(test_cases):
        input_values = input().split()
        try:
            print(int(input_values[0]) // int(input_values[1]))
        except BaseException as e:
            print("Error Code:", e)


input_test_cases = int(input())
find_error(input_test_cases)