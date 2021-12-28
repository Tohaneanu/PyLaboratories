import numpy as np


def sgn(a):
    if a < 0:
        return -1
    else:
        return 1


def suma(pond, patt, c):
    rez = []
    # print(f"c={c}")
    for i in range(len(pond)):
        rez.append(pond[i] + c * patt[i])
    # print(result)
    return rez


def model(patterns, final, c=0.1):
    w = [1, -1, 0, 0.5]
    for i in range(0, len(patterns)):
        net = float(np.dot(patterns[i], w))
        print(net)
        if final[i] != sgn(net):
            w = suma(w, patterns[i], c * (final[i] - sgn(net)))
            print(w)

#
# x1 = [1, -2, 0, -1]
# x2 = [0, 1.5, -0.5, -1]
# x3 = [-1, 1, 0.5, -1]
#
# result = [-1, -1, 1]
# x = [x1, x2, x3]
# model(x, result)


#                                        Homework:
def model1(patterns, final, w, c=0.1):
    while True:
        check = True
        for i in range(0, len(patterns)):
            net = float(np.dot(patterns[i], w))
            print(f" wanted: {final[i]}  - obtained: {net}")
            if final[i] != sgn(net):
                w = suma(w, patterns[i], c * (final[i] - sgn(net)))
                print(f" New pond: {w}")
                check = False
        if check:
            break


w = [0, 1, 0]
x1 = [2, 1, -1]
x2 = [0, -1, -1]
x = [x1, x2]
result = [-1, 1]

model1(x, result, w)
