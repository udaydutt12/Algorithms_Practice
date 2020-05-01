from matplotlib import pyplot as plt
from random import random
import math

'''
    Problem Statement: 
        Given a Circle of radius r, centered at
        (xc, yc), write a function that can retrieve
        a random point inside the circle, with a 
        uniform distribution
'''

# Method 1: Rejection Sampling
'''
    Methodology:
        In an infinite while loop,
        Get a random pair (x, y) of points where:
            -0.5 <= x <= 0.5
            -0.5 <= y <= 0.5
        This is a random point of the unit square.
        if x ^ 2 + y ^ 2 <= 1, then return the
        (x, y) pair, multiplied r, and translated
        by (xc, yc).
        We reject all the samples where x ^ 2 + y ^ 2 > 1,
        and simply try again.
        Probability of a successful sample = 3.14159 / 4  = 78.54 % chance
'''
def getRandPointonCircle1(xc, yc, r):
    while 1:
        x, y = random() - 0.5, random() - 0.5
        if x ** 2 + y ** 2 <= 1:
            return (x * r + xc, y * r + yc)

# Method 2: CDF Inverse Transform Sampling
'''
    Methodology:
        choose a random theta in [0, 2pi]
        Now, if we choose a random X from [0, r], 
        then the probability/ Cumulative Density Function, is:
        P(X <= x) = (pi * r ^ 2) / (pi * x ^ 2) = r ^ 2 / x ^ 2.
        Notice that this is not a uniform distribution. Instead,
        if we sample the probablility from 0 to 1 uniformly, then
        the inverse of the CDF should give an x that is uniformly 
        likely for all x.
        C ^ -1 = r * sqrt(x), where x is in [0, 1].
        Probability of successful sample: 100 %  
'''
def getRandPointonCircle2(xc, yc, r):
    d = math.sqrt(random()) * r
    theta = 2 * math.pi * random()
    return (xc + d * math.cos(theta), yc + d * math.sin(theta))
    

if __name__ == '__main__':
    xc, yc, r = 5, 5, 10
    xcoords, ycoords = [], []
    for _ in range(1000):
        x, y = getRandPointonCircle1(xc, yc, r)
        xcoords.append(x)
        ycoords.append(y)
    plt.scatter(xcoords, ycoords)
    plt.show()
