# https://www.hackerrank.com/challenges/any-or-all/problem

def somefunc(list_of_nums):
    list_1 = []
    list_2 = []

    for num in list_of_nums:
        list_1.append(int(num) > 0)
        list_2.append(num == str(num)[::-1])

    if all(list_1) and any(list_2) == True:
        print(True)
    else:
        print(False)


total_num = input()
list_of_nums = list(input().split())
somefunc(list_of_nums)