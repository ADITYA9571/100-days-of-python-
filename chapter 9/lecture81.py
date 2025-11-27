class vehicle:
    def __init__(self, type, engine):
        self.type = type 
        self.engine = engine 
    def vehiclemethod(self):
        print("This is vehicle method")

class bike(vehicle):
    def __init__(self,type, name):
        self.type = type 
        self.name = name 
        vehicle.__init__(self,type,engine="Petrol")
    def showdetails(self):
        vehicle.vehiclemethod(self)
        print(f"type: {self.type} name: {self.name}")

class cars(vehicle):
    def __init__(self,type, name):
        self.type = type 
        self.name = name 
        vehicle.__init__(self,type, engine="Diesel")
    def vehiclemethod(self):
        vehicle.vehiclemethod(self)
        print(f"type: {self.type} name: {self.name}")

class travel(bike, cars):
    def __init__(self,type, name):
        self.type = type
        self.name = name
    def modemethod(self):
        print(f"Mode of transport is {self.type} {self.name }")
        return f"done"

obj1 = travel("bike", "duke")
obj2 = cars("SUV","Duster")

print(obj1.modemethod())
print(obj2.vehiclemethod())