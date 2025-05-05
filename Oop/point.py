class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5



p1 = Point(1.5, 1)
p2 = Point(1.5, 2)
print(p1.dist(p2))