#Static Attribute 

# A static attribute (sometimes a class attribute) is a attribute that belongs to 
# class itself andf not to any instance of the class

class User:
    user_count = 1 
    
    def __init__(self,name,email,password):
        self.name = name 
        self.email = email
        self.password = password  
        User.user_count+=1 
        
    def display(self):
        print(f"Username:{self.name}\nEmail:{self.email}")  
        
user1 = User("Jane","jaune@gmail.com","1234")
user2 = User("Diablo","diablo123@gmail.com","999")

print(User.user_count)
print(user1.user_count)
print(user2.user_count)

print(user1.display())