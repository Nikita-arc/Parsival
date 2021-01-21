class Teacher:
 
    def __init__(self, name, cours):
        self.name = name 
        self.cours = cours
 
    def python_guru (self, cours):
        if cours == 'Python Start' or cours == 'Python Pro':
            return True
        return False
 
    def __str__(self):
        return self.name
 
list_teacher = []
 
n = int(input('Введите количество преподавателей'))
for i in range(n):
    name = input("Введите имя преподавателя")
    cours = input('Введите список курсов через запятую').split(',')
    teacher = Teacher(name, cours)
    list_teacher.append(teacher)
 
for teacher in list_teacher:
    if teacher.python_guru():
        print ("Гуру python", teacher)
