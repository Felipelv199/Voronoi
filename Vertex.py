import math


class Vertex:

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.d = 0.0

    def __lt__(self, other):
        if self.y > other.y:
            return True
        if self.y < other.y:
            return False
        if self.x < other.x:
            return True
        return False

    def __repr__(self):
        return f"({self.x},{self.y})"

    def __hash__(self):
        return self.d

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def distance(self, other):
        return math.sqrt(((other.x - self.x)*(other.x - self.x)) + ((other.y - self.y)*(other.y - self.y)))
