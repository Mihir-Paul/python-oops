#Inheritence 

class Vehicle():
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model 
        self.year = year 
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")
        
class Car(Vehicle):
    def __init__(self,brand,model,year,top_speed):
        super().__init__(brand,model,year)
        self.top_speed = top_speed
        
class Bike(Vehicle):
    def __init__(self,brand,model,year,top_speed):
        super().__init__(brand,model,year)
        self.top_speed = top_speed
        
vehicles = [Car("Ford","Mustang",1964,325), Bike("Kawasaki","Ninja H2R",2015,400)]

for vehicle in vehicles:
    if isinstance(vehicle,Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
        vehicle.start()
        vehicle.stop()
