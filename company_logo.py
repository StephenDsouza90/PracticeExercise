# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

def count_string(string):
    count = Counter(string).most_common(3)
    for i in count:
        print(*i)

string = list(sorted(input()))
count_string(string)