from course import Course
from students import Student
from datetime import datetime

class Enroll:
    def __init__(self,course,student):
        if not isinstance(student, Student):
            raise KeyError("Invalid student...")
        if not isinstance(course, Course):
            raise KeyError("Invalide course...")
        self.student = student
        self.course = course
        self.grade = None
        self.date = datetime.now()

    def set_grade(self,grade):
        self.grade = grade
