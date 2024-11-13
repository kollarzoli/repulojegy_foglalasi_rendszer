from abc import ABC, abstractmethod
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, indulasi_ido, max_foglalas):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.indulasi_ido = datetime.strptime(indulasi_ido, "%Y-%m-%d %H:%M")
        self.idopont = self.indulasi_ido
        self.max_foglalas = max_foglalas  
        self.foglalasok = []

    def foglalhato(self):
        return len(self.foglalasok) < self.max_foglalas

    @abstractmethod
    def get_jegyar(self):
        pass

    def __str__(self):
        return f"{self.jaratszam} - {self.celallomas} - {self.jegyar} Ft - {self.idopont.strftime('%Y-%m-%d %H:%M')}"

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, idopont):
        super().__init__(jaratszam, celallomas, jegyar, idopont, max_foglalas=10)

    def get_jegyar(self):
        return self.jegyar * 1.1  

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar, idopont):
        super().__init__(jaratszam, celallomas, jegyar, idopont, max_foglalas=50)

    def get_jegyar(self):
        return self.jegyar * 1.4  

