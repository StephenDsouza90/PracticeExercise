#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple


def avg_marks(num_of_students):
  """ Give an integer that represent the number of students,
      we input student details of each student under a heading,
      and then return the average marks for all students.
      eg: Input         : number_of_students
          Header        : ["ID", "MARKS", "NAME", "CLASS"]
          1st iteration : 1, 25, Stephen, 12
          2nd iteration : 2, 50, Jude, 12
          Output        : unpack the student details and returns average marks for all students.
      Compute the average, i.e. (25 + 50) / 2 = 37.50
      Return this average.        
  """  
  categories = input().split()
  Header = namedtuple('Header', categories) 
  marks_list = []
  
  for num in range(num_of_students):
    student_details = Header(*input().split())
    marks_list.append(int(student_details.MARKS))

  average_marks = sum(marks_list) / len(marks_list)   
  print(f'{average_marks:.2f}')
  

students_range = int(input())
avg_marks(students_range)