class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus 

    def annual_salary(self):
        return (self.pay*12)+self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name 
        self.age = age 
        self.salary = Salary(pay,bonus)

    def total_salary(self):
        return self.salary.annual_salary()

employee1 = Employee("Michael",30,12000,6000)
print(employee1.total_salary())