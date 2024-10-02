class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def greet(self):
        print(f'Salom, mening ismim {self.name} va mening yoshim {self.age}')


natija = Person('Ali', '25')
natija.greet()