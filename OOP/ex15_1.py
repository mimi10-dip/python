import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x          
        self.y = y
        self.width = width
        self.height = height
def point_in_circle(circle, point):
    dx = point.x - circle.center.x
    dy = point.y - circle.center.y
    distance = math.sqrt(dx**2 + dy**2)
    return distance <= circle.radius
def rect_in_circle(circle, rect):
    corners = [
        Point(rect.x, rect.y),
        Point(rect.x + rect.width, rect.y),
        Point(rect.x, rect.y + rect.height),
        Point(rect.x + rect.width, rect.y + rect.height)
    ]
    for p in corners:
        if not point_in_circle(circle, p):
            return False
    return True
def rect_circle_overlap(circle, rect):
    corners = [
        Point(rect.x, rect.y),
        Point(rect.x + rect.width, rect.y),
        Point(rect.x, rect.y + rect.height),
        Point(rect.x + rect.width, rect.y + rect.height)
    ]
    for p in corners:
        if point_in_circle(circle, p):
            return True
    return False
center = Point(150, 100)
circle = Circle(center, 75)
rect = Rectangle(140, 90, 20, 20)
print("Point in circle:", point_in_circle(circle, Point(150, 100)))
print("Rectangle in circle:", rect_in_circle(circle, rect))
print("Rectangle overlap circle:", rect_circle_overlap(circle, rect))