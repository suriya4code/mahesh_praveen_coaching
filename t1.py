class Person():
    def __init__(self, name=None, age=None, hours_worked=None):
        self.name:str = name
        self.age:int = age
        self.hours_worked:int = hours_worked
    
    def calculate_dob_year(self):
        return 2022-self.age


class Employee(Person):
    def calculate_emp_salary(self):
        return self.hours_worked * 40

class Contractor(Person):
    def calculate_cont_salary(self):
        return self.hours_worked * 25





obj1 = Employee("mahesh",32,8)
obj2 = Contractor("Praveen",36, 8)

print(obj1.calculate_emp_salary())
print(obj2.calculate_cont_salary())


