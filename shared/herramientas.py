# Colores utilizados por la interfaz del sistema
COLORES = {
    "rojo": "\033[91m",
    "verde": "\033[92m",
    "amarillo": "\033[93m",
    "blanco": "\033[97m",
    "gris": "\033[90m",
    "reset": "\033[0m"
}


# Respuestas consideradas afirmativas
RESPUESTAS_SI = ("s", "si", "sí", "y", "yes")


def limpiar_pantalla():
    # Limpia la terminal de Windows
    import os
    os.system("cls")


def imprimir_color(mensaje, color="reset"):
    # Imprime un mensaje utilizando el color seleccionado
    print(f"{COLORES[color]}{mensaje}{COLORES['reset']}")


def imprimir_titulo(titulo):
    # Muestra un título separado por líneas
    print("=" * 50)
    print(titulo)
    print("=" * 50)