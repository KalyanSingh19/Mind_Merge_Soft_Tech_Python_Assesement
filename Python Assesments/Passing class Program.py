class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        print("Employee Name:", self.name)
        print("Employee Age:", self.age)
        print("Employee Salary:", self.salary)


person = Person("Kalyan", 23)

employee = Employee(person.name, person.age, 50000)

# Displaying employee details
employee.display_details()