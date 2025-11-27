"""Method Overriding"""
class shape:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)
    def area(self):
        # return 3.14 * self.radius * self.radius
        return 3.14 * super().area()
    
rect = shape(4,5)
circle = circle(5)
print(rect.area())
print(circle.area())