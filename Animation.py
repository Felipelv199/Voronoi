import pygame as pg
import random as rand
import Vertex as Vt
import Circle
import math


def randomPoints(n):
    arr = []
    for i in range(n):
        vt = Vt.Vertex(rand.randrange(0, 100), rand.randrange(0, 100))
        vt.x = vt.x * 10
        vt.y = vt.y * 7.2
        arr.append(vt)
    return arr


def generateCircles(origins, r):
    arr = []
    for i in range(len(origins)):
        element = Circle.Circle("c" + str(i + 1), origins[i], r)
        arr.append(element)
    return arr


def algorithm(cls, ep, vts, r):
    for cl in cls:
        for other in cls:
            if cl.intersections(other) is not None:
                intersection = cl.intersections(other)
                distance = intersection.distance(other.origin)
                min_d = True
                is_vt = False
                for c in cls:
                    if c != cl and c != other:
                        cur_d = intersection.distance(c.origin)
                        if cur_d < distance:
                            min_d = False
                        if abs(cur_d-distance) < delta:
                            is_vt = True
                if min_d is True:
                    ep.append(intersection)
                if is_vt is True and min_d is True:
                    vts.append(intersection)
    for cl in cls:
        cl.radius += r


points = randomPoints(10)

radius = 1
circles = generateCircles(points, radius)
delta = math.sqrt((radius * radius) + (radius * radius))

pg.init()
screen = pg.display.set_mode((1000, 720))
pg.display.set_caption('Graphics')
animationTimer = pg.time.Clock()
endProgram = False
edges_points = []
vertexes = []

while not endProgram:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            endProgram = True

    screen.fill((255, 255, 255))

    for point in points:
        x = point.x
        y = point.y
        pg.draw.circle(screen, (0, 0, 0), (x, int(y)), 5)

    for circle in circles:
        x = int(circle.origin.x)
        y = int(circle.origin.y)
        pg.draw.circle(screen, (0, 0, 0), (x, y), circle.radius, 1)

    for point in edges_points:
        x = int(point.x)
        y = int(point.y)
        pg.draw.circle(screen, (0, 0, 255), (x, y), 2)

    for vertex in vertexes:
        x = int(vertex.x)
        y = int(vertex.y)
        pg.draw.circle(screen, (0, 255, 0), (x, y), 5)

    algorithm(circles, edges_points, vertexes, radius)

    animationTimer.tick(100)
    pg.display.update()
