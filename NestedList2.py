#https://www.hackerrank.com/challenges/nested-list/problem

from collections import defaultdict


def grades_nested_list(number_of_students):
    """ Takes in a range to input number of students with their names and grades,
        names and grades are stored in a nested list.
        eg: Nested list = [
                        ['Stephen', 50],
                        ['Rachel', 70]
                        ['Leticia', 60],
                        ['Jude', 60]
                    ]
    """
    nested_list = []

    for name_and_grade in range(number_of_students):
        sublist = []
        name_of_student = str(input())
        grade_of_student = float(input())
        sublist.insert(0, name_of_student) 
        sublist.insert(1, grade_of_student)
        nested_list.append(sublist)
    return nested_list


def convert_list_into_dict(main_nested_list):
    """ From the nested list, create a default dict to store the marks as keys and names as values.
        All students with the same marks will be grouped together.
        eg: {
            50 : ['Stephen']
            70 : ['Rachel']
            60 : ['Leticia', 'Jude']
        }
    """
    convert_dict = defaultdict(list)

    for sublist in main_nested_list:
        names = sublist[0]
        grade = sublist[1]
        convert_dict[grade].append(names)
    return convert_dict


def find_second_lowest_grade(main_nested_dict):
    """ In order to find the second lowest grade and print the name of the student,
        we can store the grades together.
        eg: [50, 70, 60]
        Next sort the grades in an ascending order and extract the second lowest score (here: [1])
        eg: [50, 60, 70]
            [60]
        From the second lowest score, get the name of the students, sort their names and print it in two lines
        eg: ['Jude', 'Leticia']
            Jude
            Leticia
    """
    grades = [grade for grade in main_nested_dict.keys()]
    print(grades)
    sorted_grades = sorted(grades)
    print(sorted_grades)
    get_second_lowest_grade = sorted_grades[1]
    print(get_second_lowest_grade)
    name_of_students = main_nested_dict[get_second_lowest_grade]
    name_of_students.sort()
    print(name_of_students)
    for name in name_of_students:
        print(name)
    return grades, sorted_grades, get_second_lowest_grade, name_of_students


number_of_students = int(input())

main_nested_list = grades_nested_list(number_of_students)
main_nested_dict = convert_list_into_dict(main_nested_list)
grades, sorted_grades, get_second_lowest_grade, name_of_students = find_second_lowest_grade(main_nested_dict)