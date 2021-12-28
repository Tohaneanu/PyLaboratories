import numpy as np

y = [[45, 85, -1],
     [50, 43, -1],
     [40, 80, -1],
     [55, 42, -1],
     [200, 43, -1],
     [48, 40, -1],
     [195, 41, -1],
     [43, 87, -1],
     [190, 40, -1]]

d = [[1, -1, -1],
     [-1, 1, -1],
     [1, -1, -1],
     [-1, 1, -1],
     [-1, -1, 1],
     [-1, 1, -1],
     [-1, -1, 1],
     [1, -1, -1],
     [-1, -1, 1]]


# print(y)
def normalizare(y):
    aux = np.array(y)
    min1 = min(aux[:, 0])
    max1 = max(aux[:, 0])
    min2 = min(aux[:, 1])
    max2 = max(aux[:, 1])
    # print(min1, max1)

    for e in y:
        e[0] = round((e[0] - min1) / (max1 - min1), 5)
        e[1] = round((e[1] - min2) / (max2 - min2), 5)
    return np.array(y)


# print(y)


# print(w)
def bipolara(net):
    return 2 / (1 + np.exp(-net)) - 1


def model(y, d, k=3, eMax=0.001, c=1):
    d = np.array(d)
    y = normalizare(y)

    m = len(y[0])
    E = 0
    w = 2 * np.random.random((m, k)) - 1

    while True:
        o = []
        for i in range(9):
            o.append(bipolara(np.dot(w, y[i])))
        for p in range(len(y)):
            for j in range(len(o[0])):
                for i in range(len(y[0])):
                    w[j, i] = w[j, i] + c * (d[p, j] - o[p][j]) * (1 - o[p][j] ** 2) * y[p, i]
        E = 0
        for p in range(len(y)):
            E = E + (d[p, 0] - o[p][0]) ** 2 + (d[p, 1] - o[p][1]) ** 2 + (d[p, 2] - o[p][2]) ** 2
        # print(E)
        if E < eMax:
            return w


w = model(y, d)
result = []
for i in range(9):
    result.append(bipolara(np.dot(w, y[i])))

for i in range(len(result)):
    if np.sign(result[i][0]) == -1:
        if np.sign(result[i][1]) == -1:
            print("\nIesirea: ", y[i], "PAT")
        else:
            print("\nIesirea: ", y[i], "MASA")
    else:
        print("\nIesirea: ", y[i], "SCAUN")
