   
import json
import os


class GestorJSON:
    def __init__(self, ruta):
        self.ruta = ruta  # Guarda la ubicación del archivo JSON
        carpeta = os.path.dirname(ruta)  # Obtiene la carpeta donde estará el JSON

        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)  # Crea la carpeta si no existe

    def leer(self):
        # Si el archivo todavía no existe, devuelve una lista vacía
        if not os.path.exists(self.ruta):
            return []

        try:
            with open(self.ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

            return datos if isinstance(datos, list) else []

        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        try:
            with open(self.ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)

            return True

        except (TypeError, OSError):
            return False  

   