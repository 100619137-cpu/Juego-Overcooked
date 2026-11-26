import pyxel
from constantes import (ANCHO_PANTALLA, ALTO_TABLERO, FPS, DURACION_SERVICIO, POS_INICIAL_CHEF_1, POS_INICIAL_CHEF_2,
                        DIB_SUELO, DIB_SARTEN, DIB_BASURA, DIB_PLATOS, DIB_BATIDORA, DIB_TABLA, DIB_ENTREGA, DIB_PASO,
                        MAPA_COCINA, TAMANO_CASILLA)
from entidades import Estacion, Chef


class Cocina:
    # Esta clase controla toda la partida: el tablero, el reloj, los puntos, los fallos y a los dos cocineros
    def __init__(self):
        # Tupla vacía donde guardaremos todos los muebles del mapa (encimeras, sartenes, cajas...)
        self.__estaciones = ()
        # Lista donde iremos metiendo las comandas que pidan los clientes
        self.__pedidos = []
        # Contador de puntos ganados y de platos fallados (si llega a 3 fallos se pierde)
        self.__puntuacion = 0
        self.__fallos = 0
        # Calculamos cuántos fotogramas dura la partida (ej: 180 segundos * 30 FPS = 5400 frames)
        self.__frames_restantes = DURACION_SERVICIO * FPS
        # Creamos a los dos jugadores en sus casillas iniciales, pasándoles (x, y) y su número (1 o 2)
        self.__chef1 = Chef(POS_INICIAL_CHEF_1[0], POS_INICIAL_CHEF_1[1], 1)
        self.__chef2 = Chef(POS_INICIAL_CHEF_2[0], POS_INICIAL_CHEF_2[1], 2)
        # Leemos el mapa nada más empezar para colocar todos los muebles en su sitio
        self.cargar_mapa()

    # --- PROPIEDADES PARA LEER LOS DATOS DE LA COCINA DESDE OTROS ARCHIVOS ---
    @property
    def estaciones(self):
        return self.__estaciones

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def puntuacion(self):
        return self.__puntuacion

    @property
    def fallos(self):
        return self.__fallos

    @property
    def chef1(self):
        return self.__chef1

    @property
    def chef2(self):
        return self.__chef2

    def cargar_mapa(self):
        # Recorremos el mapa letra por letra para crear los muebles de la cocina
        filas_mapa = []
        for fila in range(len(MAPA_COCINA)):
            for col in range(len(MAPA_COCINA[fila])):
                casilla = MAPA_COCINA[fila][col]
                # Si NO es un punto "." (suelo libre), creamos una Estacion en esa casilla
                if casilla != ".":
                    x = col * TAMANO_CASILLA
                    y = ALTO_TABLERO + fila * TAMANO_CASILLA
                    filas_mapa.append(Estacion(casilla, x, y))
        # Convertimos la lista en tupla fija
        self.__estaciones = tuple(filas_mapa)

    def tiempo(self):
        # Restamos un fotograma al tiempo restante en cada frame
        if self.__frames_restantes > 0:
            self.__frames_restantes -= 1

    def dibujar(self):
        # Borramos toda la pantalla pintándola de negro antes de dibujar el nuevo fotograma
        pyxel.cls(0)

        # --- 1. CÁLCULO Y DIBUJO DEL MARCADOR SUPERIOR ---
        segundos_totales = self.__frames_restantes // FPS
        minutos = segundos_totales // 60
        segundos = segundos_totales % 60

        # Pintamos la franja azul oscura de arriba y las dos líneas separadoras
        pyxel.rect(0, 0, ANCHO_PANTALLA, ALTO_TABLERO, 1)
        pyxel.line(64, 0, 64, ALTO_TABLERO - 1, 7)
        pyxel.line(128, 0, 128, ALTO_TABLERO - 1, 7)

        # Escribimos errores, puntuación y reloj
        pyxel.text(16, 5, f"ERR:{self.__fallos}/3", 8)
        pyxel.text(80, 4, f"PTS:{self.__puntuacion:03d}", 10)
        pyxel.text(144, 4, f"T:{minutos:02d}:{segundos:02d}", 7)

        # --- 2. DIBUJO DEL TABLERO (SUELO Y MUEBLES SEGÚN EL MAPA) ---
        # Recorremos cada fila y columna de MAPA_COCINA para dibujar lo que toque en cada casilla
        for fila in range(len(MAPA_COCINA)):
            for col in range(len(MAPA_COCINA[fila])):
                x = col * TAMANO_CASILLA
                y = ALTO_TABLERO + fila * TAMANO_CASILLA
                casilla = MAPA_COCINA[fila][col]

                # Primero pintamos siempre la baldosa de suelo debajo para que no queden huecos negros
                pyxel.blt(x, y, 0, DIB_SUELO[0], DIB_SUELO[1], TAMANO_CASILLA, TAMANO_CASILLA)

                # Ahora miramos qué letra hay en MAPA_COCINA y dibujamos el mueble encima del suelo
                # (Cambia las letras "S", "B", etc. si en tu MAPA_COCINA usaste otras letras)
                if casilla == "S":
                    pyxel.blt(x, y, 0, DIB_SARTEN[0], DIB_SARTEN[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "B":
                    pyxel.blt(x, y, 0, DIB_BASURA[0], DIB_BASURA[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "P":
                    pyxel.blt(x, y, 0, DIB_PLATOS[0], DIB_PLATOS[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "X":
                    pyxel.blt(x, y, 0, DIB_BATIDORA[0], DIB_BATIDORA[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "T":
                    pyxel.blt(x, y, 0, DIB_TABLA[0], DIB_TABLA[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "E":
                    pyxel.blt(x, y, 0, DIB_ENTREGA[0], DIB_ENTREGA[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)
                elif casilla == "M":
                    pyxel.blt(x, y, 0, DIB_PASO[0], DIB_PASO[1], TAMANO_CASILLA, TAMANO_CASILLA, 0)

        # --- 3. DIBUJO DE LA COMIDA ENCIMA DE LAS MESAS Y DE LOS CHEFS ---
        # Si alguna estación tiene un ingrediente o plato encima, lo dibuja
        for estacion in self.__estaciones:
            estacion.draw()

        # Dibujamos a los dos chefs por encima de todo
        self.__chef1.draw()
        self.__chef2.draw()