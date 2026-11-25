import pyxel
class Chef:
    SPAWN_1 = (32,  32)
    SPAWN_2 = (128,   64)
    def __init__(self, coordenadas_iniciales = None, numerochef = int,   ):

        self.numerochef = numerochef
        self.__coordenadas_iniciales = coordenadas_iniciales
        self.__coordenadas = coordenadas_iniciales




    @property
    def coordenadas(self):
        return self.__coordenadas
    @property
    def numerochef(self, valor, int):
        if valor not in (1,2):
            raise ValueError("Valor invalido")
        self.__numerochef = valor

