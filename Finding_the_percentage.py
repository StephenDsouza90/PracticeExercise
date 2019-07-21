#https://www.hackerrank.com/challenges/finding-the-percentage/problem

def marks_of_students_dict(input_number_of_students):
    """ Takes in N number of students to store their names and marks of certain subjects in a dict.
        eg: lets suppose N is 2, marks dict will return as
            Step 1: Store in a list.
                    ['Stephen', '40', '50', '60']
                    ['Jude', '50', '60', '70']
            Step 2: Seperate name and marks, name as key and marks as value
                    {'Stephen': [40, 50, 60],
                     'Jude' : [50, 60, 70]
                    }
    """
    marks_dict = {}
    for i in range(input_number_of_students):
        student_name_and_marks = input().split()
        student_name = student_name_and_marks[0]
        student_marks = [float(j) for j in student_name_and_marks[1:]]
        marks_dict[student_name] = student_marks
    return marks_dict


def average_marks_of_a_student(name_of_student, marks_of_all_students_dict):
    """ To find the average marks of a particular student,
        extract the marks by using the key in the marks dict.
        Lets suppose we want to find the marks of Stephen, {'Stephen': [40, 50, 60]},
        where Stephen is the key and 40, 50, 60 are the values.
        eg: marks of Stephen are [40, 50, 60]
        therefore, average marks are 40 + 50 + 60 / 3 = 50
    """
    marks_of_student = marks_of_all_students_dict[name_of_student]
    average_marks = sum(marks_of_student) / len(marks_of_student)
    return average_marks


number_of_students = int(input())
name_and_marks_of_students_dict = marks_of_students_dict(number_of_students)

name_of_student = input()
avg_marks_of_a_student = average_marks_of_a_student(name_of_student, name_and_marks_of_students_dict)

print(f'{avg_marks_of_a_student:.2f}')