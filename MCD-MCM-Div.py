def divisores(b):
    a = 2
    m = b
    lista = []
    while (m != 1):
        if (m % a == 0):
            lista += [a]
            m /= a

        else:
            a += 1
    return lista


def cuenta(lista):
    conj = set(lista)
    sol = []
    for i in conj:
        sol += [(i, lista.count(i))]
    return sol


def mcd(m, n):
    a = 1
    listam = cuenta(divisores(m))
    listan = cuenta(divisores(n))
    for i in listam:
        (c, b) = i
        for j in listan:
            (d, e) = j
            if (c == d and b < e):
                a *= (c ** b)
            elif (c == d):
                a *= (c ** e)
    return a


def mcm(m, n):
    a = 1
    listam = (divisores(m))
    listan = (divisores(n))
    for i in listam:
        if (i in listan):
            listan.remove(i)
            a *= i
        else:
            a *= i
    for j in listan:
        a *= j
    return a
