from random import *

def vahetus(a, b):
    # vahetab kahe muutuja väärtused
    return b, a

def generaator(n, loend, a, b):
    # genereerib n juhuslikku täisarvu
    for i in range(n):
        loend.append(randint(a, b))

def jagamine(loend, p, n, nol):
    # jagab arvud positiivseteks, negatiivseteks ja nullideks
    for el in loend:
        if el > 0:
            p.append(el)
        elif el < 0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    # leiab loendi keskmise väärtuse
    if len(loend) == 0:
        return 0
    return round(sum(loend) / len(loend), 2)

def lisamine(loend, el):
    # lisab elemendi loendisse ja sorteerib selle
    loend.append(el)
    loend.sort()


# loendite loomine
s = []
pos = []
neg = []
null = []


# põhifunktsioon
def arvud_loendis():
    print("Andmed:")
    
    n = abs(int(input("Mitu täisarvu genereerime loendisse? => ")))
    mini = int(input("Sisesta vahemiku minimaalne arv => "))
    maxi = int(input("Sisesta vahemiku maksimaalne arv => "))

    # kui kasutaja ajas min ja max segamini
    if mini > maxi:
        mini, maxi = vahetus(mini, maxi)

    generaator(n, s, mini, maxi)
    
    print("\nTulemused:")
    print(f"Saadud loend vahemikus {mini} kuni {maxi} :", s)

    s.sort()
    print("Sorteeritud loend:", s)

    jagamine(s, pos, neg, null)

    print("Positiivsed arvud:", pos)
    print("Negatiivsed arvud:", neg)
    print("Nullid:", null)

    # positiivsete keskmine
    kesk_pos = keskmine(pos)
    print("Positiivsete keskmine:", kesk_pos)
    lisamine(s, kesk_pos)

    # negatiivsete keskmine
    kesk_neg = keskmine(neg)
    print("Negatiivsete keskmine:", kesk_neg)
    lisamine(s, kesk_neg)

    print("\nLisame keskmised algsesse loendisse ja sordime:")
    print(s)


# programmi käivitamine
arvud_loendis()

