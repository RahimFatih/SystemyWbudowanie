
class Ubranie:
    def __init__(self,nazwaUbrania) -> None:
        self.name=nazwaUbrania
        self.stan = "Czyste"
        pass 
    def uzyjUbranie(self):
        print("Zużyto: ",self.name)
        self.stan="Brudne"
    def podajStan(self):
        return self.stan

class Pralka:
    
    def __init__(self) -> None:
        self.beben = []
        pass
    def dodajUbranieDoBebna(self, noweUbranie):
        print("Dodano do bebna: ",noweUbranie.name,' ',noweUbranie.podajStan())
        self.beben.append(noweUbranie)
    def wyjmijWszystko(self):
        wyjete = self.beben.copy()
        self.beben = []
        print("Wyjęto wszystkie ciuchy")
        return wyjete
    def podajZawartoscBebna(self):
        for ubranie in self.beben:
            print(ubranie.name," ", ubranie.podajStan())
    def wypierz(self):
        print(".........\nPiorę ciuszki\n.........")
        for ubranie in self.beben:
            ubranie.stan="Czyste"

garderoba = []
garderoba.append(Ubranie("Koszula w krate"))
garderoba.append(Ubranie("Dzinsy"))
garderoba.append(Ubranie("Spodnie khaki"))
mojaPralka = Pralka()

for ubranie in garderoba:
    ubranie.uzyjUbranie()

for ubranie in garderoba:
    mojaPralka.dodajUbranieDoBebna(ubranie)
garderoba = []

mojaPralka.wypierz()
garderoba = mojaPralka.wyjmijWszystko()

print("\nW garderobie znajduje się:")
for ubranie in garderoba:
    print(ubranie.name,' ',ubranie.podajStan())