class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    
    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    def get_amount_inside(self, shape):
        return (self.width * self.height) // (shape.width * shape.height)
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
           


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, value):
        self.width = value
        self.height = value

    def set_height(self, value):
        self.width = value
        self.height = value
    
    def set_side(self, value):
        self.width = value
        self.height = value
    
    def __str__(self):
        return f"Square(side={self.width})"
    

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))    
