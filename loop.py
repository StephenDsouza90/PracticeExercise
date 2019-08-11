#https://www.hackerrank.com/challenges/python-loops/problem


def print_squares(n):
    """The function will run i ** 2.
    i is within 0 to 4 as n is = 5
    A loop will be created using the "for" loop."""
    for i in range(n):
        print(i ** 2)


n = int(input())
print_squares(n)