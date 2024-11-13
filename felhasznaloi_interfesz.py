from datetime import datetime
from foglalasok import FoglalasiRendszer, Foglalas

class FelhasznaloiInterfesz:
    def __init__(self, rendszer):
        self.rendszer = rendszer

    def megjelenit_menu(self):
        while True:
            print("\n=== Repülőjegy Foglalás Rendszer ===")
            print("1. Jegy foglalása")
            print("2. Foglalás lemondása")
            print("3. Foglalások listázása")
            print("4. Kilépés")

            valasztas = input("Válassz egy lehetőséget (1-4): ")

            if valasztas == "1":
                self.jegy_foglalas()
            elif valasztas == "2":
                self.foglalas_lemondasa()
            elif valasztas == "3":
                self.foglalasok_listazasa()
            elif valasztas == "4":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás! Kérlek válassz egy számot 1 és 4 között.")

    def jegy_foglalas(self):
        jaratszam = input("Add meg a járatszámot: ")
        nev = input("Add meg a neved: ")
        foglalasi_ido = input("Add meg a foglalás időpontját (YYYY-MM-DD HH:MM): ")

        self.rendszer.jegy_foglalas(jaratszam, nev, foglalasi_ido)

      

        
        for jarat in self.rendszer.jaratok:
            if jarat.jaratszam == jaratszam and jarat.idopont == foglalasi_ido:
                foglalas = Foglalas(jarat, nev, foglalasi_ido)
                self.rendszer.foglalasok.append(foglalas)
                print(f"Foglalás sikeresen rögzítve! Név: {nev}, Járatszám: {jaratszam}, Időpont: {idopont_str}")
                return


    def foglalas_lemondasa(self):
        nev = input("Add meg a lemondani kívánt foglalás nevet: ")
        self.rendszer.foglalas_lemondasa(nev)

    def foglalasok_listazasa(self):
        self.rendszer.foglalasok_listazasa()

