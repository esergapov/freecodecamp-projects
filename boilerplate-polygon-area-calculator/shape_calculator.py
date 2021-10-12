class Rectangle:
    def __init__(self, width, height, **kwargs):
        self.width = width
        self.height = height
        super().__init__(**kwargs)

    def get_area(self):
         return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture."
        picture = ''
        for i in range(self.height):
            for j in range(self.width):
                picture += '*'
            picture += '\n'
        return picture
    
    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_height(self, new_height):
        self.height = new_height

    def set_width(self, new_width):
        self.width = new_width
        

class Square(Rectangle):
    def __init__(self, side, **kwargs):
        super().__init__(side, side, **kwargs)
    
    def set_side(self, new_side):
        super().set_height(new_side)
        super().set_width(new_side)
    
    def set_width(self, new_width):
        self.set_side(new_width)
    
    def set_height(self, new_height):
        self.set_side(new_height)
        
    def __str__(self):
        return f"Square(side={self.height})"