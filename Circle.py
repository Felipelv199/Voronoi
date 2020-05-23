import Vertex as Vt
import math


class Circle:

    def __init__(self, name="", origin=Vt.Vertex(0, 0), radius=0.0):
        self.name = name
        self.origin = origin
        self.radius = radius
        self.intersection_circles = {}

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if self.name == other:
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def intersections(self, other):
        d = math.sqrt(math.pow((other.origin.x-self.origin.x), 2) + math.pow((other.origin.y-self.origin.y), 2))
        if d > self.radius + other.radius:
            return None
        if d < math.fabs(self.radius - other.radius):
            return None
        if d == 0 and self.radius == other.radius:
            return None

        a = (math.pow(self.radius, 2) - math.pow(other.radius, 2) + math.pow(d, 2)) / (2*d)
        h = math.sqrt(math.pow(self.radius, 2) - math.pow(a, 2))

        x2 = self.origin.x + ((a * (other.origin.x-self.origin.x)) / d)
        y2 = self.origin.y + ((a * (other.origin.y-self.origin.y)) / d)

        x3 = x2 + (h * (other.origin.y-self.origin.y) / d)
        y3 = y2 - (h * (other.origin.x-self.origin.x) / d)
        return Vt.Vertex(x3, y3)
