from abc import ABC, abstractmethod

class Szoba(ABC):

    def __init__(self,Ar,Szobaszam):
        self.Ar = Ar
        self.Szobaszam = Szobaszam

class Egyagyasszoba(Szoba):

    def __init__(self,Ar,Szobaszam,Furdoszoba,Internet,Minibar):
        super().__init__(Ar,Szobaszam)
        self.Furdoszoba = Furdoszoba
        self.Internet = Internet
        self.Minibar = Minibar
        self.Tipus = "egyágyas"

class Ketagyasszoba(Szoba):

    def __init__(self, Ar, Szobaszam,Erkely,Szobaszerviz):
        super().__init__(Ar, Szobaszam)
        self.Erkely = Erkely
        self.Szobaszerviz = Szobaszerviz
        self.Tipus = "kétágyas"

class Szalloda():

    def __init__(self,Szallodanev,Szobak):
        self.Szallodanev = Szallodanev
        self.Szobak = Szobak


class Foglalas():
     def __init__(self, szalloda):
        self.Szobafoglalasok = []
        self.Szalloda = szalloda

     def Foglal(self, datum, szobaszam) -> int:
         for foglalas in self.Szobafoglalasok:
            if foglalas[1] == szobaszam and foglalas[0] == datum:
                return "Ez már foglalt."
         for szoba in self.Szalloda.Szobak:
            if szoba.Szobaszam == szobaszam:
                self.Szobafoglalasok.append([datum, szobaszam])
                return "\nÖn sikeresen lefoglalta a " + szobaszam + ".számú szobánkat " + datum + "-ra,  a szoba ára: " + str(szoba.Ar) + "Ft\n"
         
         return "Hiba a foglalásnál\n"

     def Lemond(self, datum, szobaszam):
         for foglalas in self.Szobafoglalasok:
            if foglalas[1] == szobaszam and foglalas[0] == datum:
                self.Szobafoglalasok.remove(foglalas) 
                return "Sikeresen lemondta a szobát.\n"
         return "Nincs ilyen lefoglalt szoba.\n"
    
     def ListazOsszesFoglalast(self):
          for foglalas in self.Szobafoglalasok:
            print("Dátum: " + foglalas[0] + "\t Szobaszám: " +foglalas[1])
          print("\n")  
          
        

# szálloda létrehozása
szalloda = Szalloda("Üdvözlet a WGM szállodájában", [])

# szállodafeltöltése szobákkal
egyagyas1 = Egyagyasszoba(1000, "1", True, True, True)
szalloda.Szobak.append(egyagyas1)
egyagyas2 = Egyagyasszoba(1000, "2", True, True, True)
szalloda.Szobak.append(egyagyas2)
ketagyas1 = Ketagyasszoba(15000, "3", True, True)
szalloda.Szobak.append(ketagyas1)

# előre definiált foglalások
foglalas = Foglalas(szalloda)
foglalas.Szobafoglalasok.append(["2024-06-12", "1"])
foglalas.Szobafoglalasok.append(["2024-07-12", "1"])
foglalas.Szobafoglalasok.append(["2024-08-12", "1"])
foglalas.Szobafoglalasok.append(["2024-07-13", "2"])
foglalas.Szobafoglalasok.append(["2024-08-12", "3"])

while True:
        print("A. Szoba foglalás")
        print("B. Szoba lemondása")
        print("C. Foglalások listája")
        print("D. A program elhagyása")
        valaszt = input("\nKérem válasszon egy opciót (A-D): ")

        if valaszt == "A":
            datum = input("Mikorra szeretne foglalni (év-hónap-nap): ")
            szobaszama = input("Adja meg a szoba számát (1-3): ")
            print(foglalas.Foglal(datum, szobaszama))
        elif valaszt == "B":
            datum = input("Adja meg a lemondás dátumát (év-hónap-nap): ")
            szobaszama = input("Adja meg a lemondani kívánt szoba számát (1-3): ")            
            print(foglalas.Lemond(datum, szobaszama) + "\n")
        elif valaszt == "C":
            print("\nFoglalások listája:\n")
            foglalas.ListazOsszesFoglalast()
        elif valaszt == "D":
            print("A viszont látásra")
            break
        else:
            print("\nNincs ilyen opció, próbálja újra.\n")


