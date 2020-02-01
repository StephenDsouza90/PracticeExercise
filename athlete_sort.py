# https://www.hackerrank.com/challenges/python-sort-sort/problem

def create_records(n):
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    return arr


def sorting(list_of_records):
    k = int(input())
    for i in sorted(list_of_records, key=lambda i: int(i[k])):
        print(*i)


n, m = map(int, input().split())
list_of_records = create_records(n)
sorting(list_of_records)