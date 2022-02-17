class Point():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show(self):
        print('('+str(self.x1), str(self.y1)+')', '('+str(self.x2), str(self.y2)+')')

    def move(self):
        self.x1 += 1
        self.y1 += 1
        self.x2 += 1
        self.y2 += 1
    
    def dist(self):
        print(((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5)

p = Point(15, 25, 4, 7)
p.show()
p.move()
p.dist()