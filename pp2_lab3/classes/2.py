class Shape():
    def __init__(self, lenght):
        self.lenght = lenght

    def area(self):
        print(0)
    
class Square(Shape):
    def __init__(self, lenght):
        super().__init__(lenght)

    def area(self):
        print(self.lenght**2)

figure = Square(5)
figure.area()