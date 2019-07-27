#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement

char = input().split()
x = combinations_with_replacement(sorted(char[0]), int(char[1]))
for i in x:
  print("".join(i))