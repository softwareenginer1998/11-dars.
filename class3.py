class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id


    def korsatish(self):
        print(f'Student nomi: {self.name}   Student yoshi: {self.age}   Student id raqami: {self.student_id}')


nom = Student('Alimardon', '25', '26911')
nom.korsatish()
