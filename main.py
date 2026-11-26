import pyxel
from constantes import ANCHO_PANTALLA, ALTO_TOTAL, FPS
from cocina import Cocina


class App:
    # Clase principal que arranca la ventana de Pyxel y ejecuta el bucle del juego
    def __init__(self):
        # Creamos la ventana del juego con el ancho, alto, título y fotogramas por segundo (FPS)
        pyxel.init(ANCHO_PANTALLA, ALTO_TOTAL, title="Overcooked Pyxel", fps=FPS)
        # Cargamos el archivo con los dibujos (sprites) que hemos creado en el editor de Pyxel
        # (Asegúrate de que el nombre del archivo coincida con el tuyo, por ejemplo "recursos.pyxres")
        pyxel.load("my_resource.pyxres")
        # Creamos el objeto Cocina, que prepara el mapa, los muebles, el reloj y los dos chefs
        self.cocina = Cocina()
        # Arrancamos el bucle infinito de Pyxel indicando qué función actualiza datos y cuál dibuja
        pyxel.run(self.update, self.draw)

    def update(self):
        # Esta función se ejecuta automáticamente en cada fotograma (ej. 30 veces por segundo)
        # 1. Restamos tiempo al reloj de la partida
        self.cocina.tiempo()
        # 2. Leemos las teclas pulsadas para mover al Chef 1 (WASD + Q) y al Chef 2 (Flechas + Espacio)
        self.cocina.chef1.actualizaracciones()
        self.cocina.chef2.actualizaracciones()

    def draw(self):
        # Esta función se ejecuta justo después de update() para pintar todo en la pantalla
        self.cocina.dibujar()


# Punto de entrada del programa: al ejecutar main.py, creamos App() y empieza el juego
if __name__ == "__main__":
    App()