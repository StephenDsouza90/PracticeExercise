#https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

def count_shoe_sizes(number_of_shoes):
  """ The number of shoes in the shop are 10.
      These 10 shoes have different sizes that are [2, 3, 4, 5, 6, 8, 7, 6, 18]
      The count is {(2: 1), (3: 1), (4: 2), (5: 1), (6: 2), (7: 1), (18: 1)} key : value
  """    
  input_shoe_sizes = map(int, input().split())
  count_shoes = Counter(input_shoe_sizes)
  return count_shoes

def find_earnings(number_of_customers, dict_shoe_sizes):
  """ There are 6 who want the shoe sizes 
      6 (pay 55), 6 (pay 45), 6 (pay 55), 4 (pay 40), 18 (pay 60), 10 (pay 50).
      If the shoe size exist in the shop, see how many of the shoes are available.
      Sum the values to get the total sales
      we have shoe sizes 30, 20 and 30 therefore we get paid 55 + 45 + 40 + 60 = 200
  """
  sale = 0
  for i in range(number_of_customers):
    input_size, input_value = map(int, input().split())
    if input_size in dict_shoe_sizes.keys():
      if dict_shoe_sizes[input_size] > 0:
        dict_shoe_sizes[input_size] -= 1
        sale += input_value
  return sale


num_of_shoes = str(input())
dict_shoe_sizes = count_shoe_sizes(num_of_shoes)

num_of_customers = int(input())
earnings = find_earnings(num_of_customers, dict_shoe_sizes)
print(earnings)