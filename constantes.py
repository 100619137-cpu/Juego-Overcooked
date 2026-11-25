#Aqui se encuentran todas las constantes que tiene el juego, tanto dimensiones, como tiempos,
#puntuaciones, recetas y el mapa de la cocina

#DIMENSIONES DE LA PANTALLA Y ESCALA

ANCHO_PANTALLA=192
ALTO_TABLERO=32
ALTO_COCINA=144
ALTO_TOTAL=ALTO_TABLERO+ALTO_COCINA
TAMANO_CASILLA=16
ESCALA=4

#TIEMPOS, PUNTUACIÓN Y LÍMITES

FPS=30
DURACION_SERVICIO=180
MAX_FALLOS=3
MAX_PEDIDOS_MISMOTIEMPO=3
TIEMPO_PEDIDO_PRIMERO=3
PEDIDOS_NIVEL_INICIAL=4

#COORDENADAS DE LOS DIBUJOS EN EL ARCHIVO PYXRES

DIB_SARTEN=(16, 32)
DIB_BASURA=(32, 32)
DIB_PLATOS=(48, 32)
DIB_PLATO_VACIO=(0, 48)
DIB_BATIDORA=(16, 80)
DIB_TABLA=(32, 80)
DIB_ENTREGA=(48, 80)
DIB_PASO=(0, 96)
DIB_SUELO=(16, 96)
DIB_ENCIMERA=(48, 96)
DIB_PARED=(32, 96)
DIB_CHEF_1=(0, 112)
DIB_CHEF_2=(0, 128)

#COORDENADAS DE LOS INGREDIENTES

DIB_INGREDIENTES = {
    "tomate": {"entero": (0, 0), "cortado": (0, 16)},
    "patata": {"entero": (16, 0), "cortado": (16, 16)},
    "cebolla": {"entero": (32, 0), "cortado": (32, 16)},
    "chorizo": {"entero": (48, 0), "cortado": (48, 16)},
    "huevo": {"entero": (0, 32)}}

#COORDENADAS PLATOS TERMINADOS

DIB_PLATOS_TERMINADOS = {
    "gazpacho": (16, 48),
    "tortilla": (32, 48),
    "huevos_rotos": (48, 48)}

#COORDENADAS DE LOS CAJONES

DIB_CAJONES = {
    "chorizo": (0, 64),
    "tomate": (16, 64),
    "patata": (32, 64),
    "cebolla": (48, 64),
    "huevo": (0, 80)}

#Agrupamos estos en diccionarios para que vincular directamente el nombre
#de texto de cada elemento con su sprite "dibujo". Así las clases pueden consultar
#la imagen en una sola línea sin tener que escribir bloques repetitivos de condicionales


#RECETAS: NOMBRE, INGREDIENTES, APARATO, PUNTOS, TIEMPO Y PENALIZACIÓN (utilizanndo un diccionario)

RECETAS={
    "gazpacho": (["tomate_cortado", "cebolla_cortada"], "batidora", 10, 48, 5),
    "tortilla": (["patata_cortada", "cebolla_cortada", "huevo"], "sarten", 12, 60, 6),
    "huevos_rotos": (["patata_cortada", "huevo", "chorizo_cortado"], "sarten", 12, 60, 6)}

#Orientación de los elementos de la cocina

MAPA_COCINA=[
    ["C_CEB", "C_HUE", "C_CHO", "E", "TAB", "E", "BAT", "E", "E", "E", "E", "ENT"], # Fila 0 (Encimera Chef 1)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 1 (Suelo Chef 1)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 2 (Suelo Chef 1)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 3 (Suelo Chef 1)
    ["P", "PAS", "P", "PAS", "P", "BAS", "P", "PAS", "P", "P", "PAS", "P"],         # Fila 4 (Barra central)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 5 (Suelo Chef 2)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 6 (Suelo Chef 2)
    [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],                   # Fila 7 (Suelo Chef 2)
    ["C_TOM", "C_PAT", "E", "E", "E", "TAB", "E", "SAR", "E", "PLA", "E", "E"]]     # Fila 8 (Encimera Chef 2)

"""Guardamos el mapa de la cocina en una lista de listas (9 filas x 12 columnas) para representar el plano 
de la Figura 1 y crear todas las casillas con dos bucles sin tener que escribir cada mueble uno por uno"""

#Posición inicial de los chefs

POS_INICIAL_CHEF_1=(5 * TAMANO_CASILLA + 8, ALTO_TABLERO + 2 * TAMANO_CASILLA)
POS_INICIAL_CHEF_2 = (5 * TAMANO_CASILLA + 8, ALTO_TABLERO + 6 * TAMANO_CASILLA)

#Cada chef empieza en el centro de su zona (columna 5, filas 2 y 6),

