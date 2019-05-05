class Rectangle:
    def __init__(self,length,height):
        try:
            length = float(length)
            height = float(height)
        except ValueError:
            raise InvalidData("To nie jest liczba!")
        else:
            if length <= 0 or height <= 0:
                raise InvalidData("Wartość nie może być ujemna!")
            self.length = length
            self.height = height
    
    def __str__(self):
        return f"length: {self.length} | height: {self.height} | area: {self.area()}"

    def __repr__(self):
        return f"{__name__}.{self.__class__.__name__}({self.length},{self.height})"

    def area(self):
        return self.length * self.height


class Cuboid(Rectangle):
    def __init__(self,length,height,width):

        super().__init__(length,height)

        try:
            width = float(width)
        except ValueError:
            raise InvalidData("To nie jest liczba!")
        else:
            if width <= 0:
                raise InvalidData("Wartość nie może być ujemna!")
            self.width = width

    def __str__(self):
        string = super().__str__()
        index = string.find("area")
        return string[:index] + f"width: {self.width} | area: {self.area()} | volume: {self.volume()}"

    def __repr__(self):
        return f"{__name__}.{self.__class__.__name__}({self.length},{self.height},{self.width})"
    
    def area(self):
        base = super().area()
        side1 = self.height * self.width
        side2 = self.length * self.width
        return 2 * (base + side1 + side2)

    def volume(self):
        return super().area() * self.width

class InvalidData(Exception):
    pass