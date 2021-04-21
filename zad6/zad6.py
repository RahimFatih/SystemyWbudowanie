zapisONP = input("Podaj wyrazenia arytmetyczne w ONP\nDostępne operatory: +,-,*,/,%,^\n")
rozdzieloneONP = zapisONP.split()


def Oblicz(tablicaONP, stos):
    for znak in tablicaONP:
        stos.append(znak) if znak.isnumeric() else stos.append(
            SprDzialanie(int(stos.pop(-1)), int(stos.pop(-1)), znak))
    return stos[-1]


def SprDzialanie(p, l, znak):
    return {'+': l + p, '-': l - p, '*': l * p, '/': l / p, '%': l % p, '^': l ** p}.get(znak)


print(Oblicz(rozdzieloneONP, []))
