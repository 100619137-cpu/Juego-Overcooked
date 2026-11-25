import pyxel
from constantes import (TAMANO_CASILLA, DIB_INGREDIENTES, DIB_PLATO_VACIO, DIB_PLATOS_TERMINADOS)

class Ingrediente:
    #Representa cada alimento individual
    def __init__(self, nombre: str, estado: str= "entero") -> None:
        self._nombre = nombre
        self._estado = estado
    #Cada alimento tiene su nombre y su estado inicial "entero"

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def estado(self) -> str:
        return self._estado

    #Usamos @property para poder leer los atributos privados para leerlos desde fuera
    #sin modificarlos por error

    @estado.setter
    def estado(self, nuevo_estado: str) -> None:
        self._estado = nuevo_estado

    #El setter nos permite cambiar el estado cuando cortamos o cocinamos el ingrediente

    def draw(self, x: int, y: int):
        #Dibuja el ingrediente en las coordenadas (x, y) usando el sprite de su estado actual

        #Comprobamos si ese estado tiene dibujo propio (cortado/entero) en el diccionario
        if self._estado in DIB_INGREDIENTES[self._nombre]:
            #Sacamos las coordenadas (u, v) del archivo .pyxres y pegamos el recorte de 16x16
            u, v = DIB_INGREDIENTES[self._nombre][self._estado]
            pyxel.blt(x, y, 0, u, v, TAMANO_CASILLA, TAMANO_CASILLA, 0)
            # Pintamos en (x, y) el sprite de 16x16 guardado en (u, v) del archivo de imágenes,
            # usando el negro (0) como fondo transparente
