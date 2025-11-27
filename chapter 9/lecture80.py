class animal:
    def __init__(self,name,species):
        self.name = name 
        self.species = species
    def showdetails(self):
        print(f"Name: {self.name} and Species: {self.species}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name, species="Dog")
        self.breed = breed
    def showdetails(self):
        animal.showdetails(self)
        print(f"breed: {self.breed}")

class GoldenRetriever(dog):
    def __init__(self,name,colour):
        dog.__init__(self,name, breed="Golden Retriever")
        self.colour = colour
    def showdetails(self):
        dog.showdetails(self)
        print(f"colour: {self.colour}")

obj1 = GoldenRetriever("Shera","Black")    
obj1.showdetails()
print(GoldenRetriever.mro())