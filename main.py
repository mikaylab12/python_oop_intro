
class Shapes:
    def __init__(self, name, sides):
        self.name=name
        self.sides=sides
    def Area(self):
        print("I am a: " + self.name + "\n" +
              "I have " + self.sides + " sides")
obj_shape=Shapes("shape", "so many")
obj_shape.Area()

class Rectangle(Shapes):
    def __init__(self, len1,wid1):
        self.length=len1
        self.width=wid1
    def Area(self):
        result = self.length * self.width
        return result
obj_rect=Rectangle(10,7)
obj_screen=Rectangle(5, 7)
print("The area of a Rectangle is: " + str(obj_rect.Area()))
print("The area of a Screen is: " + str(obj_screen.Area()))

class Circle(Shapes):
    def __init__(self, rad):
        self.radius=rad
    def Area(self):
        import math
        result = (((self.radius)*(self.radius)) * math.pi)
        return result
obj_circle = Circle(10)
print("The area of a Circle is %.2f: " % (obj_circle.Area()))

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base=base
        self.height=height
    def Area(self):
        result = (0.5 * (self.base * self.height))
        return result
obj_tri = Triangle(5, 8)
print("The area of a Triangle is: " + str(obj_tri.Area()))
