#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

def create_group(n_numbers, m_numbers):
  """ Takes in two numbers (n and m) to form a range and create two groups.
      eg: group a i.e. n : a a b a b
          {'a' : [1, 2, 4],
           'b' : [3, 5]
           }
          group b i.e. m : a b
          ['a', 'b']
      Next, it will check if group b letters are in group a.
      If group b letters exist in group a then it will return the index of those letters.
        eg: group b : a are 1 2 4
            group b : b are 3 5
      Incase a letter from group b is not in group a, then it will return - 1 to indicate that the letter does not exist.       
  """
  group_a = defaultdict(list)
  group_b = []

  for n_words in range(n_numbers):
    group_a[input()].append(n_words + 1)
  for m_words in range(m_numbers):
    group_b = group_b + [input()]
  for character in group_b:
      print(
         " ".join(
                map(str, group_a.get(character, []))
         ) or "-1"
      )


n_num, m_num = map(int, input().split())
create_group(n_num, m_num)