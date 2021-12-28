import random

n = 50  # Nr de cromozomi generati random
c = 10  # Cartile

list_c = []

# Initializarea popultiei (generearea a 50 de cromozomi random)
for i in range(0, n):
    sir = []
    for j in range(0, c):
        sir.append(float(random.randint(0, 1)))
    list_c.append(sir)


def imperechere(lista1, lista2):
    lista1[0], lista2[5] = lista2[5], lista1[0]
    lista1[1], lista2[6] = lista2[6], lista1[1]
    lista1[2], lista2[7] = lista2[7], lista1[2]
    lista1[3], lista2[8] = lista2[8], lista1[3]
    lista1[4], lista2[9] = lista2[9], lista1[4]
    lista1[5], lista2[0] = lista2[0], lista1[5]
    lista1[6], lista2[1] = lista2[1], lista1[6]
    lista1[7], lista2[2] = lista2[2], lista1[7]
    lista1[8], lista2[3] = lista2[3], lista1[8]
    lista1[9], lista2[4] = lista2[4], lista1[9]


ff = 1000
nr_gen = 1

while nr_gen <= 1000 and ff != 0:
    print("Generatia " + str(nr_gen) + " :")
    if nr_gen > 1:
        for elem in list_c:
            elem.pop()
    for elem in list_c:
        s = 0
        p = 1
        for i in range(0, c):
            if elem[i] == 0:
                s += (i + 1)
            elif elem[i] == 1:
                p *= (i + 1)
        ff = abs(s - 36) / 36 + abs(p - 360) / 360  # Fitness function: Ff=|s1-s|/s+|p2-p|/p        s=36; p=360;
        elem.append(ff)

    sorted_list = sorted(list_c, key=lambda x: x[10])

    sorted_list.pop()

    copie = sorted_list[0]

    sorted_list.append(copie)

    nr1 = random.randint(0, 25)
    nr2 = random.randint(0, 25)

    # Aplicarea op genetice
    imperechere(sorted_list[nr1], sorted_list[nr1 + 1])  # imperecherea cromozomilor vechini
    imperechere(sorted_list[nr2], sorted_list[nr2 + 1])

    # Mutatile
    sorted_list[random.randint(0, 49)][random.randint(0, 9)] = sorted_list[random.randint(0, 49)][random.randint(0, 9)]
    sorted_list[random.randint(0, 49)][random.randint(0, 9)] = sorted_list[random.randint(0, 49)][random.randint(0, 9)]
    sorted_list[random.randint(0, 49)][random.randint(0, 9)] = sorted_list[random.randint(0, 49)][random.randint(0, 9)]
    sorted_list[random.randint(0, 49)][random.randint(0, 9)] = sorted_list[random.randint(0, 49)][random.randint(0, 9)]
    sorted_list[random.randint(0, 49)][random.randint(0, 9)] = sorted_list[random.randint(0, 49)][random.randint(0, 9)]

    for elem in sorted_list:
        print(elem)

    nr_gen += 1

print("\nFitness function = " + str(sorted_list[49][10]))

sum = 0
prod = 1

pachet1 = []
pachet2 = []

for i in range(0, 10):
    if sorted_list[49][i] == 0:
        pachet1.append(i + 1)
        sum = sum + (i + 1)
    elif sorted_list[49][i] == 1:
        pachet2.append(i + 1)
        prod = prod * (i + 1)

print("\nSuma cartilor este: " + str(sum))
print("Primul pachet contine cartile: " + str(pachet1))

print("\nProdusul cartilor este: " + str(prod))
print("Al doilea pachet contine cartile: " + str(pachet2))
