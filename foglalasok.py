from datetime import datetime
from jaratok import BelfoldiJarat, NemzetkoziJarat, Jarat

class Foglalas:
    def __init__(self, nev, jarat, idopont):
        self.nev = nev
        self.jarat = jarat
        self.idopont = idopont


    def __str__(self):
#        print(f"Debug: {type(self.jarat)}")
        return f"{self.nev} - {self.jarat.celallomas} - {self.jarat.jegyar} Ft - {self.idopont.strftime('%Y-%m-%d %H:%M')}"

class FoglalasiRendszer:
    def __init__(self):
        self.jaratok = [
            BelfoldiJarat("BUD123", "Debrecen", 8000, "2024-12-01 10:00"),
            BelfoldiJarat("BUD456", "Pécs", 7000, "2024-12-01 12:00"),
            NemzetkoziJarat("BUD789", "London", 25000, "2024-12-01 14:00")
        ]
        self.foglalasok = []


    
        self.betolt_foglalasok()

    def betolt_foglalasok(self):
        
        foglalasok = [
            ("hsz", "BUD123", "2024-12-01 10:00"),
            ("kjanos", "BUD456", "2024-12-01 12:00"),
            ("peter", "BUD789", "2024-12-01 14:00"),
            ("anna", "BUD123", "2024-12-01 10:00"),
            ("mark", "BUD456", "2024-12-01 12:00"),
            ("eva", "BUD789", "2024-12-01 14:00")
        ]
        
        for nev, jaratszam, ido in foglalasok:
            self.jegy_foglalas(jaratszam, nev, ido)

    def jegy_foglalas(self, jaratszam, nev, idopont):
        
        
        try:
            idopont = datetime.strptime(idopont, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Hibás időpont formátum!")
            return

        """Foglalás kezelése"""
       
        jarat = self.find_jarat(jaratszam, idopont)
        if not jarat:
            print("Járat nem található!")
            return
        

        if self.is_foglalhato(jarat, idopont):
            foglalas = Foglalas(nev, jarat, idopont)
            self.foglalasok.append(foglalas)
            print(f"Sikeres foglalás: {foglalas}")
        else:
            print("Ez az időpont már foglalt vagy érvénytelen.")

    def find_jarat(self, jaratszam, idopont):
        """ Járat keresése a listában """
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam and jarat.idopont == idopont:
                return jarat
        return None

    def is_foglalhato(self, jarat, idopont):
        
        
        if jarat.foglalhato():
            return True
        return False


    def foglalas_lemondasa(self, nev):
        for foglalas in self.foglalasok:
            if foglalas.nev == nev:
                self.foglalasok.remove(foglalas)
                print(f"Foglalás törölve: {foglalas}")
                return
        print("Nem található foglalás a megadott névvel.")

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            print("Nincsenek aktív foglalások.")
        for foglalas in self.foglalasok:
            if isinstance(foglalas.jarat, Jarat):
                print(foglalas)
            else:
                print("Hiba: A jarat attribútum nem Jarat típusú.")
