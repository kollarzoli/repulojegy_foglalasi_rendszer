from foglalasok import FoglalasiRendszer
from felhasznaloi_interfesz import FelhasznaloiInterfesz

if __name__ == "__main__":
    
    rendszer = FoglalasiRendszer()
    
    print("A következő járatok érhetők el foglalásra:")
    for jarat in rendszer.jaratok:
        print(jarat)

    interfesz = FelhasznaloiInterfesz(rendszer)
    interfesz.megjelenit_menu()

