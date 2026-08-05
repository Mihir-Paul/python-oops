class Dog():
    def __init__(self,name,breed,owner): #init method is used to instantiate a  object
        self.name = name #data field
        self.breed = breed #data field
        self.owner = owner 

    def bark(self):
        print(f"{self.name} says hello!")

class Owner():
    def __init__(self,name,address,contact_number):
        self.name = name
        self.address = address
        self.number = contact_number 
    
    def owns(self,Dog):
        print(f"{self.name} owns {Dog.name}")

#Instance of a owner class       
owner1 = Owner("Mihir","Kolkata","900-900-009") #attributes or variables store the data of an object 
dog1 = Dog("Billy","French Bulldog",owner1) #creating an object 
owner1.owns(dog1)
dog1.bark()
print(dog1.breed) #when you call data field dont use () these brackets
print(dog1.name)
print(dog1.owner.name )

dog2 = Dog("Priyanshu","Maltese",owner1) #instance of a dog class
dog2.bark()
owner1.owns(dog2)