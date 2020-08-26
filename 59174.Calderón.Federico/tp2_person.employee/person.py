class Person:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
    def set_person(self, name, age):
        self.name = name 
        self.age = age 
    def get_person(self):
        arr = [self.name,self.age]
        return arr
    
class Employee: 
    def __init__(self,name,age,salary):
        Person.__init__(self,name,age)
        self.salary = salary 
    def get_employee(self):     
        return [self.name,self.age,self.salary]
    
    def get_pay_tax(self):
        if ((self.age) < 32) and ((self.salary) > 3000):
            return 'Paga impuestos'
        else:
            return 'No paga impuestos'


















