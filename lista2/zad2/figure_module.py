import math

class Figure:
    def __init__(self):
        self.colour = "red"
        self.is_filled = False

    def __str__(self):
        return f"colour = {self.colour}\nfilled = {self.is_filled}"
    
    def __repr__(self):
        return f"Figure(colour={self.colour},is_filled={self.is_filled})"


class Circle(Figure):
    def __init__(self):
        super().__init__()
        self.__radius = 10

    def __str__(self):
        return super().__str__() + f"\nradius = {self.radius}"
    
    def __repr__(self):
        return f"Figure(colour={self.colour},is_filled={self.is_filled},Circle(radius={self.radius}))"

    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self,radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Niepoprawana wartość")

    @property
    def area(self):
        return self.radius ** 2 * math.pi

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return self.diameter * math.pi

class Rectangle(Figure):
    def __init__(self):
        super().__init__()
        self.__width = 11
        self.__height = 4

    def __str__(self):
        return super().__str__() + f"\nwidth = {self.width}\nheight = {self.height}"
        
    def __repr__(self):
        return f"Figure(colour={self.colour},is_filled={self.is_filled},Rectangle(width={self.width},height={self.height}))"
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @width.setter
    def width(self,width):
        if width > 0:
            self.__width = width
        else:
            print("Niepoprawna wartość")

    @height.setter
    def height(self,height):
        if height > 0:
            self.__height = height
        else:
            print("Niepoprawna wartość")

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * self.width + (2 * self.height)

    @property
    def diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)


if __name__ == "__main__":
    ob1 = Figure()
    print(ob1)
    print(repr(ob1))

    print()

    ob2 = Circle()
    print(ob2)
    print(repr(ob2))

    print()

    ob3 = Rectangle()
    print(ob3)
    print(repr(ob3))