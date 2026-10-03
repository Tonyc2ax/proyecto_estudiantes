from model import Estudiante
from shared.json_manager import GestorJSON


gestor = GestorJSON("data/estudiantes.json")

CAMPOS_OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")
CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")


def es_email_valido(email):
    email = str(email).strip()

    if "@" not in email:
        return False

    usuario, dominio = email.rsplit("@", 1)

    return bool(usuario) and "." in dominio

def carnets_registrados(excepto_id=None):
    return {
        str(registro.get("carnet", "")).lower()
        for registro in gestor.leer()
        if registro.get("id") != excepto_id
    }


def siguiente_id():
    ids = [registro.get("id", 0) for registro in gestor.leer()]
    return max(ids) + 1 if ids else 1


def crear_estudiante(datos):
    try:
        valores = {
            campo: str(datos.get(campo, "")).strip()
            for campo in CAMPOS_OBLIGATORIOS
        }

        if not all(valores.values()):
            return False, "Todos los campos son obligatorios"

        if not es_email_valido(valores["email"]):
            return False, "El email no es válido"

        if valores["carnet"].lower() in carnets_registrados():
            return False, "El carnet ya está registrado"

        estudiante = Estudiante(
            siguiente_id(),
            valores["nombre"],
            valores["apellido"],
            valores["email"],
            valores["carnet"]
        )

        registros = gestor.leer()
        registros.append(estudiante.a_diccionario())

        if gestor.guardar(registros):
            return True, "Estudiante creado correctamente"

        return False, "Error al guardar el estudiante"

    except (KeyError, TypeError, ValueError) as error:
        return False, f"Error al crear estudiante: {error}"


def obtener_todos():
    return [
        Estudiante.desde_diccionario(registro)
        for registro in gestor.leer()
    ]


def buscar_estudiantes(texto):
    texto = str(texto).strip().lower()

    if not texto:
        return []

    resultados = []

    for registro in gestor.leer():
        for campo in CAMPOS_BUSCABLES:
            valor = str(registro.get(campo, "")).lower()

            if texto in valor:
                resultados.append(
                    Estudiante.desde_diccionario(registro)
                )
                break

    return resultados


def actualizar_estudiante(id_estudiante, datos):
    try:
        id_estudiante = int(id_estudiante)
    except (TypeError, ValueError):
        return False, "El ID debe ser un número"

    registros = gestor.leer()

    for registro in registros:
        if registro.get("id") == id_estudiante:

            valores = {
                campo: str(
                    datos.get(
                        campo,
                        registro.get(campo, "")
                    )
                ).strip()
                for campo in CAMPOS_OBLIGATORIOS
            }

            if not all(valores.values()):
                return False, "Todos los campos son obligatorios"

            if not es_email_valido(valores["email"]):
                return False, "El email no es válido"

            if valores["carnet"].lower() in carnets_registrados(
                id_estudiante
            ):
                return False, "El carnet ya está registrado"

            registro.update(valores)

            if gestor.guardar(registros):
                return True, "Estudiante actualizado correctamente"

            return False, "Error al guardar los cambios"

    return False, "Estudiante no encontrado"


def eliminar_estudiante(id_estudiante):
    try:
        id_estudiante = int(id_estudiante)
    except (TypeError, ValueError):
        return False, "El ID debe ser un número"

    registros = gestor.leer()

    for registro in registros:
        if registro.get("id") == id_estudiante:
            registros.remove(registro)

            if gestor.guardar(registros):
                return True, "Estudiante eliminado correctamente"

            return False, "Error al eliminar el estudiante"

    return False, "Estudiante no encontrado"


def agregar_nota(id_estudiante, materia, nota):
    try:
        id_estudiante = int(id_estudiante)
    except (TypeError, ValueError):
        return False, "El ID debe ser un número"

    try:
        nota = float(nota)
    except (TypeError, ValueError):
        return False, "La nota debe ser un número"

    if nota < 0 or nota > 20:
        return False, "La nota debe estar entre 0 y 20"

    materia = str(materia).strip()

    if not materia:
        return False, "La materia es obligatoria"

    registros = gestor.leer()

    for registro in registros:
        if registro.get("id") == id_estudiante:

            if "notas" not in registro:
                registro["notas"] = {}

            if materia not in registro["notas"]:
                registro["notas"][materia] = []

            registro["notas"][materia].append(nota)

            registro.setdefault("materias", [])

            if materia not in registro["materias"]:
                registro["materias"].append(materia)

            if gestor.guardar(registros):
                return True, "Nota agregada correctamente"

            return False, "Error al guardar la nota"

    return False, "Estudiante no encontrado"


def materias_ofertadas():
    materias = set()

    for registro in gestor.leer():
        materias.update(
            registro.get("materias", [])
        )

    return materias


def estudiantes_en_comun(id_a, id_b):
    try:
        id_a = int(id_a)
        id_b = int(id_b)
    except (TypeError, ValueError):
        return set()

    registros = gestor.leer()

    estudiante_a = None
    estudiante_b = None

    for registro in registros:
        if registro.get("id") == id_a:
            estudiante_a = registro

        if registro.get("id") == id_b:
            estudiante_b = registro

    if estudiante_a is None or estudiante_b is None:
        return set()

    materias_a = set(
        estudiante_a.get("materias", [])
    )

    materias_b = set(
        estudiante_b.get("materias", [])
    )

    return materias_a.intersection(materias_b)