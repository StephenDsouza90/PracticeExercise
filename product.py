#https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
print(*product(list_a, list_b))