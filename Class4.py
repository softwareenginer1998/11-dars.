class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self):
        self.salary *= 1.10

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary:.2f}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


employee = Employee("John", 50000)
employee.display_info()


manager = Manager("Alice", 70000, "Sales")
manager.display_info()


developer = Developer("Bob", 60000, "Python")
developer.display_info()


employee.give_raise()
manager.give_raise()
developer.give_raise()

print("\nAfter salary raise:")
employee.display_info()
manager.display_info()
developer.display_info()
