#https://www.hackerrank.com/challenges/py-if-else/problem

def find_odd_even(input_number):
    """ If a number divided by 2 leaves a remainder 1, then the number is odd,
        if a number divided by 2 leaves a remainder 0, then the number is even.
        The % helps to calculate the remainder.
        eg: number % 2 == 1 >> odd
            number % 2 == 0 >> even
    """
    if input_number % 2 == 1:
        print(input_number, "is an odd number")
    elif input_number % 2 == 0:
        print(input_number, "is an even number")


number = int(input())
find_odd_even(number)
