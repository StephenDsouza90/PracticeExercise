#https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
""" Takes in characters and an integer.
    Characters will be used for the distribution of the permutation,
    and the integer will determine the number of characters in the permutation.
    eg: hack 2, 
        where hack are the characters and 2 is the number.
    The characters will be sorted in a lexicographic order and printed one under the other.
"""
character, integer = map(str, input().split())
permutation_sorted = list(permutations(sorted(character), int(integer)))
for permutation_character in permutation_sorted:
  print(''.join(permutation_character))
