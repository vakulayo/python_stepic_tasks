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
        return 3.14 * self.radius ** 2

    def get_center(self):
        return self.center

    def get_raduis(self):
        return self.radius

    def do_intersect(self, other):
        return self.center.dist(other.center) <= (self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ne__(self, other):
        return self.radius != other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __gt__(self, other):
        return self.radius > other.radius


print(Circle(Point(0, 0), 0).square())
print(Circle(Point(0, 0), 1).square())
print(Circle(Point(120, -324), 43).square())
print(3.14 * 43 * 43)

print(Circle(Point(0, 0), 1).do_intersect(Circle(Point(3, 4), 1)))
print(Circle(Point(0, 0), 1).do_intersect(Circle(Point(3, 4), 5)))
circle1 = Circle(Point(0, 0), 1)
circle2 = Circle(Point(3, 4), 5)
print(circle1.__eq__(circle2))
print(circle1.__eq__(circle1))
print(circle1.__gt__(circle2))