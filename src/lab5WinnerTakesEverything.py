import math
import random


def suma(pattern, prototype, c):
    result = []
    for i in range(len(pattern)):
        result.append(prototype[i] + c * (pattern[i] - prototype[i]))
        # print(result)
    # print(result)
    return result


def model(patterns, p=3, c=0.1, epochs=500):
    list1 = [item[0] for item in patterns]
    list2 = [item[1] for item in patterns]
    minimum_x = min(list1)
    minimum_y = min(list2)
    maximum_x = max(list1)
    maximum_y = max(list2)
    prototypes = []
    for i in range(p):
        prototypes.append([random.randint(minimum_x, maximum_x), random.randint(minimum_y, maximum_y)])
    print(prototypes)
    prototypes = [[187, 41], [70, 58], [160, 54]]
    i = 0
    while i <= epochs:
        # print(f"epoca: {i}")
        i += 1
        patt_len = 0
        while patt_len < len(patterns):
            a = patterns[patt_len][0]
            b = patterns[patt_len][1]
            minimum = float('inf')
            win = -1
            j = 0
            while j < p:
                distance = math.sqrt(((a - prototypes[j][0]) ** 2) + ((b - prototypes[j][1]) ** 2))
                if distance < minimum:
                    minimum = distance
                    win = j
                j += 1
            # print(win)
            # print(f" sum= {suma(patterns[patt_len], prototypes[win], c)}")
            prototypes[win] = suma(patterns[patt_len], prototypes[win], c)
            # print(prototypes)
            patt_len += 1

    print(prototypes)


x = [[45, 85], [50, 43], [40, 80], [55, 42], [200, 43], [48, 40], [195, 41], [43, 87], [190, 40]]
model(x)
