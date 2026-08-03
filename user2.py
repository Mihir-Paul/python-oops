class User:
    def __init__(self,name,email,password):
        self.name = name 
        self._email = email
        self.password = password 
        
    @property
    def email(self):
        print("Email Accessed!")
        return self._email 
    
    @email.setter
    def email(self,new_email):
        if "@" in new_email:
            self._email = new_email 
    
    
user1 = User("Katie","kat@gmail.com","888@345")
print(user1.email)