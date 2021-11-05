def calcDeriv(default=None):
    if default is None:
        start = [6, -12, 1]
    print("functia data: +(" + str(start[0]) + "x^2)+(" + str(start[1]) + "x)+(" + str(start[2]) + ")")
    deriv = [start[0] * 2, start[1]]
    print("functia derivata: +(" + str(deriv[0]) + "x)+(" + str(deriv[1]) + ")")
    return deriv


while True:
    print("Introduceti constanta de invatare: ")
    c = int(input())
