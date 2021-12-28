import random


#

def calcF(x):
    return 6 * (x ** 2) - 12 * x + 1


def calcDeriv(x):
    return 12 * x - 12


def grad(c=0.01, prag=0.00001, x0=None, pas=None):
    global val
    if x0 is None:
        x0 = random.randint(-10, 10)
        print(f"Valoarea initiala pentru x : {x0}")
    if pas is None:
        pas = 0
    if pas == 0:
        val = input(f" c initial={c} \n Doriti rulare fara schimbarea constantei?(Y/N)?").upper()
    if val == "N":
        value = input("Modificati constanta de invartare pe parcursul rularii?(Y/N)").upper()
        if value == "Y":
            c = float(input())
            print(f"Constanta este acum: {c}")
    x = x0 - c * calcDeriv(x0)
    print(f"Diferenta: {abs(x0 - x)}")
    print(f"f(x) la pasul {pas + 1} este:  {calcF(x)}")
    if abs(x0 - x) < prag:
        return
    else:
        grad(x0=x, pas=pas + 1)



# # grad()
# print("###############################################################################")
# grad(c=0.15)
# print("###############################################################################")
# grad(c=0.01)
#
#



def calcG(x, y):
    return (x ** 2) + 2 * (y ** 2)


def calcXDerivG(x):
    return 2 * x


def calcYDerivG(y):
    return 4 * y


def gradientGrad2(c=0.1, prag=0.00001, x0=None, y0=None, pas=None):
    if x0 is None:
        x0 = random.randint(-10, 10)
        print(f"Valoarea initiala pentru x : {x0}")
    if y0 is None:
        y0 = random.randint(-10, 10)
        print(f"Valoarea initiala pentru y : {y0}")
    if pas is None:
        pas = 0
    x = x0 - c * calcXDerivG(x0)
    y = y0 - c * calcYDerivG(y0)
    print(f"Diferenta pt x => {abs(x0 - x)}         Diferenta pt y => {abs(y0 - y)}")
    print(f"g(x) la pasul {pas + 1} este:  {round(calcG(x, y),9)}")
    if abs(x0 - x) < prag and abs(y0 - y) < prag:
        return
    else:
        gradientGrad2(x0=x, y0=y, pas=pas + 1)


gradientGrad2()
    #                          H







def calcH(x, y):
    return round((1 - x) ** 2 + 100 * pow((x - y ** 2), 2), 9)


def calcXDerivH(x, y):
    return 202 * x - 200 * pow(y, 2) - 2


def calcYDerivH(x, y):
    return 400 * y * (pow(y, 2) - x)


def gradientGrad2H(c=0.01, prag=0.00001, x0=None, y0=None, pas=None):
    while True:
        if x0 is None:
            x0 = random.randint(-1, 1)
            print(f"Valoarea initiala pentru x : {x0}")
        if y0 is None:
            y0 = random.randint(-1, 1)
            print(f"Valoarea initiala pentru y : {y0}")
        if pas is None:
            pas = 0
        x = x0 - c * calcXDerivH(x0, y0)
        y = y0 - c * calcYDerivH(x0, y0)
        print(
            f"##################################################################3{x}#################################3{y}")
        print(f"Diferenta pt x => {abs(x0 - x)}         Diferenta pt y => {abs(y0 - y)}")
        print(f"g(x) la pasul {pas + 1} este:  {round(calcH(x, y), 9)}")
        if abs(x0 - x) < prag and abs(y0 - y) < prag:
            return
        pas += 1
        x0 = x
        y0 = y


# gradientGrad2H()
