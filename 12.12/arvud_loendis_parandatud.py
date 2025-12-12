from random import *

def vahetus(a, b):
    return b, a  # parandatud: nüüd tagastab õigesti b,a


def generaator(n, loend, a, b):
    for i in range(n):  # parandatud: range n → range(n)
        loend.append(randint(a, b))  # parandatud: loend.append, mitte loend(append)


def jagamine(loend, p, n, nol):
    for el in loend:
        if el > 0:
            p.append(el)
        elif el < 0:  # parandatud: vigane "elif::" parandatud õigeks
            n.append(el)
        else:
            nol.append(el)


def keskmine(loend):
    if len(loend) == 0:
        return 0  # parandatud: tühja loendi keskmine = 0
    return round(sum(loend) / len(loend), 2)  # parandatud: lihtsam ja korrektne arvutus


def lisamine(loend, el):
    loend.append(el)  # parandatud: loend.append
    loend.sort()      # parandatud: loend.sort(), mitte loend(sort())


# loendid
s = []     # muudetud: algsed nimed parandatud
pos = []
neg = []
null = []


def arvud_loendis():
    print("Andmed:")

    n = abs(int(input("Mitu täisarvu genereerime loendisse? => ")))  # parandatud: abs lisatud
    mini = int(input("Sisesta vahemiku minimaalne arv => "))
    maxi = int(input("Sisesta vahemiku maksimaalne arv => "))

    if mini > maxi:  # parandatud: >= asemel >
        mini, maxi = vahetus(mini, maxi)  # parandatud: õiged argumendid

    generaator(n, s, mini, maxi)  # parandatud: vale funktsiooni nimi

    print("\nTulemused:")
    print(f"Saadud loend vahemikus {mini} kuni {maxi} :", s)

    s.sort()  # parandatud: sort(s) → s.sort()
    print("Sorteeritud loend:", s)  # parandatud: koma lisatud

    jagamine(s, pos, neg, null)  # parandatud: neljas nimekiri lisatud

    print("Positiivsed arvud:", pos)
    print("Negatiivsed arvud:", neg)
    print("Nullid:", null)

    kesk_pos = keskmine(pos)  # parandatud: eemaldatud vigane lisaparameeter
    print("Positiivsete keskmine:", kesk_pos)
    lisamine(s, kesk_pos)

    kesk_neg = keskmine(neg)  # parandatud: sama viga parandatud
    print("Negatiivsete keskmine:", kesk_neg)
    lisamine(s, kesk_neg)

    print("\nLisame keskmised algsesse loendisse ja sordime:")
    print(s)


arvud_loendis()  # parandatud: funktsioonile lisatud sulud


