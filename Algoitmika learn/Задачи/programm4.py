class Teacher(teacher):
    
    def teacher(self, teacher_name, teacher_courses):
        self.teacher_name = teacher_name
        self.teacher_courses = teacher_courses
    
def Python_guru(python):
    if python == "python_start" or python == "python_pro":
        return True
    else:
        return False
