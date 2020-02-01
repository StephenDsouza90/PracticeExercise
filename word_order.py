# https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter


def word_count(lis):
    cnt = Counter()
    for words in lis:
        cnt[words] += 1
    print(len(cnt.values()))
    print(*cnt.values())


lis = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
word_count(lis)