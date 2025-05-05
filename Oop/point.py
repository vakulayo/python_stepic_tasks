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


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def square(self):
        return 3.14*self.radius**2

    def get_center(self):
        return self.center

    def get_raduis(self):
        return self.radius

    def  do_intersect(self, other_circle):
        if self.center.dist(other_circle.center) > (self.radius + other_circle.radius): return False
        else: return True


print(Circle(Point(0, 0), 0).square())
print(Circle(Point(0, 0), 1).square())
print(Circle(Point(120, -324), 43).square())
print( 3.14 * 43 * 43)

print(Circle(Point(0,0), 1).do_intersect(Circle(Point(3,4), 1)))
print(Circle(Point(0,0), 1).do_intersect(Circle(Point(3,4), 5)))