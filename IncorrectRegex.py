#https://www.hackerrank.com/challenges/incorrect-regex/problem

import re

for i in range(int(input())):
    try:
        re.compile(str(input()))
        print("True")
    except re.error:
        print("False")