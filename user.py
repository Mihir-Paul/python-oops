#Accessing and Modifying Data
# 1.The traditional way: make the data private and user getters and setters:

# Name Mangled 



class User:
    def __init__(self,username,email,password):
        self.name = username
        self._email = email #internal attribute 
        self.__password = password  
    
    def clean_email(self):
        return self._email.lower().strip()  
     
    def say_hi_to_user(self,user):
        print(f"Message to {user.name}: Hi {user.name}, I am {self.name}")
        print(f"Message from {self.name}: Hi {user.name}, I am {self.name}") 
        
    def get_email(self):
        return self._email 
    
    def set_email(self,new_email):
        if "@" in new_email:
            self._email = new_email
        
user1 = User("Bob","bob@gmail.com","567")
user2 = User ("Charlie","charlie@@gmail.com","1234")  

print(user1.get_email())

user2.set_email("charlie@gmail.com")  
print(user2.get_email())   

#The "Consenting Adults Philosophy"
