"""way to constructors """
class person:
    # def __init__(self, name="aditya", role="SDE"):
    def __init__(self,name,role):
        self.naam = name
        self.kaam = role
        # def info(self):
        #     print(f"employee is {self.naam} and job is {self.kaam}")
        # info(self)
        self.info()
    
    def info(self):
        print(f"employee is {self.naam} and job is {self.kaam}")
        

a = person("harry","dev")
b = person("aditya","ds")
