class Person():
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
    def greet(self):
        print(f"My name is {self.name} and I am {self.age} years old")
        
person1 = Person("Mihir",19) #Creating a Object from Person class
person1.greet()

person2 = Person("Priyanshu",20)
person2.greet()

person3 = Person("Shalini",18)
person3.greet()