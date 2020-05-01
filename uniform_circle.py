from matplotlib import pyplot
from random import random
from math import sqrt, pi, cos, sin

def getRandPointonCircle(xc, yc, r):
    d = sqrt(random()) * r
    theta = 2 * pi * random()
    return (xc + d * cos(theta), yc + d * sin(theta))
    

if __name__ == '__main__':
    xc, yc, r = 5, 5, 10
    xcoords, ycoords = [], []
    for _ in range(1000):
        x, y = getRandPointonCircle(xc, yc, r)
        xcoords.append(x)
        ycoords.append(y)
    pyplot.scatter(xcoords, ycoords)
    pyplot.show()