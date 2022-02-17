class Shape():
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        print(0)
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        super().__init__(lenght, width)

    def area(self):
        print(self.lenght*self.width)

figure = Rectangle(7, 8)
figure.area()