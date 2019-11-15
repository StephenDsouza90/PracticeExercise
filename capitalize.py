#https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys


def solve(full_name):
    capitalize_name = ' '.join(name.capitalize() for name in full_name.split(' '))
    return capitalize_name

s = input()
result = solve(s)
print(result)