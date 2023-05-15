from professors import Professor
from enroll import Enroll
class Course:
    def __init__(self, name, code, min_, max_, professor):
        self.name = name
        self.code = code
        self.min = min_
        self.max = max_
        self.professores = []
        self.enrollments = []
        
        if isinstance(professor, Professor):
            self.professores.append (professor)
        elif isinstance(professor, list):
           for entry in professor:
               if not isinstance(entry, Professor):
                  raise KeyError ("Invalid address..")
               self.professores = professor
        else:
            raise KeyError ("Invalid address...")
    def add_professor (self, professor):
        if not isinstance(professor, Professor):
            raise KeyError("invalid professor")
        self.professores.append(professor)
    
    def add_enrollment(self, enroll):
        if not isinstance(enroll, Enroll):
            raise KeyError("Invalid enroll...")
        if len(self.enrollments) == self.max:
            raise KeyError("Cannot emroll, course is full")
    
    def is_cancelled(self):
        return len(self.entrollments) < self.min

            

