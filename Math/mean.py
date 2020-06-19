import math, random, statistics

def randPoint():
    x = random.random()
    y = random.random()
    return (x,y)

def getDist(a,b):
    x_gap = (a[0] - b[0])**2
    y_gap = (a[1] - b[1])**2
    return math.sqrt(x_gap+y_gap)

distances = []
i = 0
while i<10000:
    distances.append(getDist(randPoint(),randPoint()))
    i += 1

print("Mean distance is",statistics.mean(distances))
print("Median distance is",statistics.median(distances))