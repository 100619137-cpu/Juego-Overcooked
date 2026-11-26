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


class Plato:
    # Representa un plato donde vamos juntando ingredientes hasta conseguir una receta acabada
    def __init__(self):
        # Lista privada que guarda los objetos Ingrediente que el chef va echando encima del plato
        self._ingredientes = []
        # Guarda el nombre de la receta terminada (ej. "gazpacho"). Empieza en None porque está sin cocinar
        self._receta_terminada = None

    @property
    def ingredientes(self):
        # Permite consultar desde fuera qué ingredientes lleva el plato sin sobrescribir la lista
        return self._ingredientes

    @property
    def receta_terminada(self):
        # Devuelve el nombre de la receta terminada (o None si todavía no se ha cocinado)
        return self._receta_terminada

    @receta_terminada.setter
    def receta_terminada(self, receta):
        # Permite asignar el nombre de la receta cuando la batidora o la sartén terminan de cocinar
        self._receta_terminada = receta

    def vaciar(self):
        # Limpia el plato dejando la lista vacía y quitando la receta (útil al tirar comida a la basura)
        self._ingredientes = []
        self._receta_terminada = None

class Estacion:
    # Representa cada mueble o casilla con la que puede interactuar el chef (encimera, sartén, tabla, caja...)
    def __init__(self, tipo, x, y, ingrediente_dispensador=None):
        # Tipo de mueble: "encimera", "tabla", "sarten", "batidora", "caja", "basura", "entrega", "platos"
        self._tipo = tipo
        # Posición en píxeles (x, y) donde está colocado este mueble en la pantalla
        self._x = x
        self._y = y
        # Si es una "caja" de comida, guarda qué alimento entrega (ej. "tomate"). En los demás muebles vale None
        self._ingrediente_dispensador = ingrediente_dispensador
        # Guarda el objeto que está apoyado encima del mueble (un Ingrediente o un Plato). Empieza vacío (None)
        self._objeto_encima = None

    @property
    def tipo(self):
        return self._tipo

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def ingrediente_dispensador(self):
        return self._ingrediente_dispensador

    @property
    def objeto_encima(self):
        return self._objeto_encima

    @objeto_encima.setter
    def objeto_encima(self, nuevo_objeto):
        # Permite poner o quitar un ingrediente o un plato encima del mueble
        self._objeto_encima = nuevo_objeto

    def draw(self):
        # Si el mueble tiene un plato o un ingrediente apoyado encima, le pedimos que se dibuje en (self._x, self._y)
        if self._objeto_encima is not None:
            self._objeto_encima.draw(self._x, self._y)


class Chef:
    # Representa a cada uno de los dos jugadores que se mueven y cocinan
    def __init__(self, x, y, numerochef=1, acciones=False, cocina=None, direccion="derecha"):
        # Guardamos posición, número de jugador (1 o 2), dirección hacia la que mira y lo que lleva en la mano
        self._x = x
        self._y = y
        self._numerochef = numerochef
        self._acciones = acciones
        self._cocina = cocina
        self._direccion = direccion
        # Guarda el Ingrediente o Plato que lleva cogido el chef (empieza con las manos vacías: None)
        self._objeto_en_mano = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def direccion(self):
        return self._direccion

    @property
    def acciones(self):
        return self._acciones

    @acciones.setter
    def acciones(self, nuevoestado):
        self._acciones = nuevoestado

    @property
    def objeto_en_mano(self):
        return self._objeto_en_mano

    @objeto_en_mano.setter
    def objeto_en_mano(self, nuevo_objeto):
        # Permite que el chef coja o suelte un ingrediente o un plato
        self._objeto_en_mano = nuevo_objeto

    def actualizaracciones(self):
        # Controles para el Chef 1 (WASD para moverse + Q para interactuar)
        if self._numerochef == 1:
            if pyxel.btn(pyxel.KEY_A):
                self._x -= 2
                self._direccion = "izquierda"
            if pyxel.btn(pyxel.KEY_D):
                self._x += 2
                self._direccion = "derecha"
            if pyxel.btn(pyxel.KEY_W):
                self._y -= 2
                self._direccion = "arriba"
            if pyxel.btn(pyxel.KEY_S):
                self._y += 2
                self._direccion = "abajo"


        # Controles para el Chef 2 (Flechas para moverse + Espacio para interactuar)
        elif self._numerochef == 2:
            if pyxel.btn(pyxel.KEY_LEFT):
                self._x -= 2
                self._direccion = "izquierda"
            if pyxel.btn(pyxel.KEY_RIGHT):
                self._x += 2
                self._direccion = "derecha"
            if pyxel.btn(pyxel.KEY_UP):
                self._y -= 2
                self._direccion = "arriba"
            if pyxel.btn(pyxel.KEY_DOWN):
                self._y += 2
                self._direccion = "abajo"
            if pyxel.btnp(pyxel.KEY_SPACE):
                self._acciones = not self._acciones

    def draw(self):
        # Si mira a la izquierda ponemos ancho negativo (-16) para voltear el dibujo horizontalmente
        ancho = -TAMANO_CASILLA if self._direccion == "izquierda" else TAMANO_CASILLA
        # El Chef 1 saca su dibujo de u=0 y el Chef 2 de u=16 en el editor de Pyxel
        u_sprite = 0 if self._numerochef == 1 else 16
        pyxel.blt(self._x, self._y, 0, u_sprite, 0, ancho, TAMANO_CASILLA, 0)

        # Si el chef lleva un ingrediente o un plato en la mano, lo dibujamos un poco por encima de su cabeza
        if self._objeto_en_mano is not None:
            self._objeto_en_mano.draw(self._x, self._y - 10)