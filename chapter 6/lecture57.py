class person:
    name = "aditya"
    package = 6
    occupation = "SDE"
    def info(self):
        print(f"{self.name} is a {self.occupation} with package {self.package}")

a = person()
b = person()
c = person()

b.name = "chetan"
b.package = 15
b.occupation = "ML"

c.name = "guddu"
c.package = 15
c.occupation = "ML"

a.info()
b.info()
c.info()
