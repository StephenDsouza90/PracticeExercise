#https://www.hackerrank.com/challenges/python-print/problem

def print_withoutstring(n):
    """Print 123...N without using string method.
    Read an integer N.
    Without using any string methods, try to print the following:
    123...N
    Note that "..." represents the values in between."""
    for i in range(1, n+1):
        print(i, end = "")

n = int(input())
print_withoutstring(n)