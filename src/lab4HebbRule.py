import math

import numpy as np

w = [1, -1, 0, 0.5]
x1 = [1, -2, 1.5, 0]
x2 = [1, -0.5, -2, -1.5]
x3 = [0, 1, -1, 1.5]
x = [x1, x2, x3]


def sgn(net):
    if net >= 0:
        return 1
    else:
        return -1


def suma(xx, y, net):
    ww = []
    for i in range(len(xx)):
        ww.append(xx[i] + net * y[i])
    return ww


def bipolara(net):
    return round(2 / (1 + math.exp(-net)) - 1, 3)


def hebb(dataset, ponderi, bipol=False):
    net = float(np.dot(ponderi, dataset[0]))
    net = round(net, 2)
    if not bipol:
        ponderi = suma(ponderi, dataset[0], sgn(net))
    else:
        ponderi = suma(ponderi, dataset[0], bipolara(net))
    dataset.remove(dataset[0])
    print(f"Net: {net}")
    print(f" Noile ponderi: {ponderi}")
    if len(dataset) < 1:
        return
    else:
        if not bipol:
            hebb(dataset, ponderi)
        else:
            hebb(dataset, ponderi, True)


print("Functie de activare sgn: ")
hebb(x, w)
w = [1, -1, 0, 0.5]
x1 = [1, -2, 1.5, 0]
x2 = [1, -0.5, -2, -1.5]
x3 = [0, 1, -1, 1.5]
x = [x1, x2, x3]
print()
print("Functie de activare continua bipolara: ")
hebb(x, w, True)
x1 = [1, -2]
x2 = [0, 1]
x3 = [2, 3]
x4 = [1, -1]
w = [1, -1]
x = [x1, x2, x3, x4]

print("\n###################################################################\nExercitiul 2:")
print("Functie de activare sgn: ")
hebb(x, w)
x1 = [1, -2]
x2 = [0, 1]
x3 = [2, 3]
x4 = [1, -1]
w = [1, -1]
x = [x1, x2, x3, x4]
print("Functie de activare continua bipolara: ")
hebb(x, w, True)
