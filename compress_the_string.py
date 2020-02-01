from itertools import groupby

input_string = str(input())
print(*[(len(list(occurance)), int(string)) for string, occurance in groupby(input_string)])