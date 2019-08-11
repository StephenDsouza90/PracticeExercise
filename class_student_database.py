class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


class Database:
    """ Objective is to create a database to record students and marks of a particular subject.
    The database can add new students, update records, delete records and search for a particular student.
    """
    def __init__(self):
        self.storage = { }
    
    def add(self, student):
        self.storage[student.name] = student

    def print_records(self):
        for x, y in self.storage.items():
            print(x, y.marks)

    def update_records(self, student):
        self.storage.update({student.name: student})
        print(student.name, "record has been updated with ", student.marks, "marks.")
    
    def delete_records(self, name):
        if name in self.storage:
            student = self.storage.pop(name)
            print(student.name, "record has been deleted.")

    def search_records(self, name):
        if name in self.storage:
            student = self.storage[name]
            print(name, "exist and mark is", student.marks)
        else:
            print(name, "record does not exist.")


student_1 = Student('Stephen', 30)
student_2 = Student('Jude', 40)
student_3 = Student('Rachel', 50)

database = Database()
database.add(student_1)
database.add(student_2)
database.add(student_3)

student_4 = Student('Leticia', 60)
database.add(student_4)

enter_name = input("Enter student name: ")
database.search_records(enter_name)

enter_name_marks = input("Enter student name and marks: ").split()
student_5 = Student(str(enter_name_marks[0]), int(enter_name_marks[1]))
database.update_records(student_5)

delete_record = input("Enter record to be deleted: ")
database.delete_records(delete_record)

database.print_records()