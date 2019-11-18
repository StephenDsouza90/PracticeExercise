# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

def find_probability():
    list_length = int(input())
    list_elements = input().split()
    comb_limit = int(input())
    comb = list(combinations(list_elements, comb_limit))

    count = 0
    for i in comb:
        if 'a' in i:
            count += 1

    probability = count/len(comb)    
    return probability


results = find_probability()
print(results)