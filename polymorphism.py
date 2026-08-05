#Polymorphism

class Car():
    def __init__(self,brand,model,year,top_speed):
        self.brand = brand
        self.model = model 
        self.year = year 
        self.top_speed = top_speed 
        
    def start(self):
        print("Vehicle is starting")
        
    def stop(self):
        print("Vehicle is stopping")
        
class Bike():
    def __init__(self,brand,model,year,top_speed):
        self.brand = brand
        self.model = model 
        self.year = year 
        self.top_speed = top_speed 
    
    def start_bike(self):
        print("Vehicle is starting")
    
    def stop_bike(self):
        print("Vehicle is stopping")
        
#Creating a list of Vehicles to inspect
vehicles = [Car("Ford","Mustang",1964,355),Bike("Kawasaki","Ninja H2R",2004,400)]

#Traversing through the vehicles
for vehicle in vehicles:
    if isinstance(vehicle,Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}") 
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle,Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not a Vehicle")
    