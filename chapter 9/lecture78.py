class animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species
    def makesound(self):
        print("Soud made by the animal!!")
class cat(animal):
    def __init__(self, name, breed):
        animal.__init__(self, name, species="dog")
        self.breed = breed
    def makesound(self):
        print( "Meoww!!")

C = cat("litti","Street")
A = animal("cat","house")
print(C.makesound)
print(A.makesound)
print(C.breed)
print(A.species)
print(C.name)
print(A.name)
print(C)
print(A)