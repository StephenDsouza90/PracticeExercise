#https://www.hackerrank.com/challenges/zipped/problem

class Marksheet:
    def __init__(self, student, subject):
        self.student_ids = student
        self.subjects = subject
    
    def avg_marks(self):
        sheet = []
        
        for mark in range(self.subjects):
            sheet.append(map(float, input().split()))
        
        for marks_list in zip(*sheet):
            print(f'{sum(marks_list) / len(marks_list):.1f}')


students, subjects = map(int, input().split())
uni_marksheet = Marksheet(students, subjects)

uni_marksheet.avg_marks()