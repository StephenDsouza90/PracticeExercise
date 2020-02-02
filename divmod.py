# https://www.hackerrank.com/challenges/python-mod-divmod/problem

def somefunc(a, b):
    mod = divmod(a, b)
    print(mod[0])
    print(mod[1])
    print(mod)


a = int(input())
b = int(input())
somefunc(a, b)