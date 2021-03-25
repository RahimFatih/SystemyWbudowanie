def czyPalindrom(tekst):
    tekst=tekst.lower()
    for i in range(len(tekst)):
        if tekst[i]!=tekst[-i-1]:
            return False
    return True

wyraz="Owocowo"
print(wyraz)
print(czyPalindrom(wyraz))
wyraz="Warzywnie"
print(wyraz)
print(czyPalindrom(wyraz))
