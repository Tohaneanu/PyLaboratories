from decimal import Decimal
from random import randint

from scipy.spatial import distance

x = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]]


def makeAsign(x, k):
    assign = {tuple(i): [] for i in k}
    for i in x:
        dist = Decimal('Infinity')
        centr = 0
        for count in range(len(k)):
            if distance.euclidean(i, k[count]) < dist:
                dist = distance.euclidean(i, k[count])
                centr = count
        for key in assign:
            if tuple(key) == tuple(k[centr]):
                assign[key].append(i)
    return assign


def weightFunction(vect):
    x = 0
    y = 0
    for i in vect:
        x += i[0]
        y += i[1]
    try:
        return [round(x / len(vect), 3), round(y / len(vect), 3)]
    except ZeroDivisionError:
        return [0, 0]


def model(x, k=3):
    centroid = []
    for j in range(k):
        centroid.append([randint(50 * j, 50 * (j + 1)), int(randint(50 * j, 50 * (j + 1)) / randint(1, 2))])
    # centroid = [[49, 13.0], [93, 45.5], [134, 65.0]]
    print(f"Centroizi initiali: {centroid}")
    assign = makeAsign(x, centroid)
    print(f"initaial assign: {assign}")
    while True:

        e = 0
        i = 0
        while i < k:
            val = list(assign.values())[i]
            print(val)
            weight = weightFunction(list(assign.values())[i])
            print(f"weight= {weight}")
            key = list(assign.keys())[list(assign.values()).index(val)]
            print(key)
            if tuple(weight) != tuple(key):
                e += 1
                assign[tuple(weight)] = assign.pop(tuple(key))
            i += 1
        if e == 0:
            return assign
        else:
            centroid = []
            for key in assign:
                centroid.append(tuple(key))
            assign = makeAsign(x, centroid)
            print(f"new assign: {assign}")


print(f"final assign: {model(x, 3)}")

# [[49, 13.0], [93, 45.5], [134, 65.0]]
