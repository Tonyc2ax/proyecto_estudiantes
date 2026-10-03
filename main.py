from views import (
    crear_estudiante,
    obtener_todos,
    buscar_estudiantes,
    actualizar_estudiante,
    eliminar_estudiante,
    agregar_nota,
    materias_ofertadas,
    estudiantes_en_comun
)

from shared.herramientas import (
    limpiar_pantalla,
    imprimir_color,
    imprimir_titulo,
    RESPUESTAS_SI
)


def pausar():
    input("\nPresiona ENTER para continuar...")


def buscar_por_id(id_estudiante):
    try:
        id_estudiante = int(id_estudiante)
    except ValueError:
        return None

    for estudiante in obtener_todos():
        if estudiante.id == id_estudiante:
            return estudiante

    return None


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        imprimir_color(
            "No hay estudiantes registrados.",
            "amarillo"
        )
        return

    for estudiante in estudiantes:
        imprimir_color(
            f"ID: {estudiante.id} | "
            f"Carnet: {estudiante.carnet} | "
            f"Nombre: {estudiante.obtener_nombre_completo()} | "
            f"Email: {estudiante.email} | "
            f"Promedio: {estudiante.obtener_promedio()}",
            "blanco"
        )


def opcion_crear():
    limpiar_pantalla()
    imprimir_titulo("CREAR ESTUDIANTE")

    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    email = input("Email: ").strip()
    carnet = input("Carnet: ").strip()

    datos = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "carnet": carnet
    }

    exito, mensaje = crear_estudiante(datos)

    if exito:
        imprimir_color(mensaje, "verde")
    else:
        imprimir_color(mensaje, "rojo")


def opcion_listar():
    limpiar_pantalla()
    imprimir_titulo("LISTA DE ESTUDIANTES")

    estudiantes = obtener_todos()

    mostrar_estudiantes(estudiantes)


def opcion_buscar():
    limpiar_pantalla()
    imprimir_titulo("BUSCAR ESTUDIANTE")

    texto = input(
        "Nombre, apellido, email o carnet: "
    ).strip()

    resultados = buscar_estudiantes(texto)

    mostrar_estudiantes(resultados)


def opcion_actualizar():
    limpiar_pantalla()
    imprimir_titulo("ACTUALIZAR ESTUDIANTE")

    id_estudiante = input(
        "ID del estudiante: "
    ).strip()

    estudiante = buscar_por_id(id_estudiante)

    if estudiante is None:
        imprimir_color(
            "Estudiante no encontrado.",
            "rojo"
        )
        return

    imprimir_color(
        "Deja vacío si no deseas cambiar el dato.",
        "amarillo"
    )

    nombre = input(
        f"Nombre [{estudiante.nombre}]: "
    ).strip()

    apellido = input(
        f"Apellido [{estudiante.apellido}]: "
    ).strip()

    email = input(
        f"Email [{estudiante.email}]: "
    ).strip()

    carnet = input(
        f"Carnet [{estudiante.carnet}]: "
    ).strip()

    datos = {
        "nombre": nombre or estudiante.nombre,
        "apellido": apellido or estudiante.apellido,
        "email": email or estudiante.email,
        "carnet": carnet or estudiante.carnet
    }

    exito, mensaje = actualizar_estudiante(
        id_estudiante,
        datos
    )

    if exito:
        imprimir_color(mensaje, "verde")
    else:
        imprimir_color(mensaje, "rojo")


def opcion_eliminar():
    limpiar_pantalla()
    imprimir_titulo("ELIMINAR ESTUDIANTE")

    id_estudiante = input(
        "ID del estudiante: "
    ).strip()

    estudiante = buscar_por_id(id_estudiante)

    if estudiante is None:
        imprimir_color(
            "Estudiante no encontrado.",
            "rojo"
        )
        return

    imprimir_color(
        f"Estudiante: "
        f"{estudiante.obtener_nombre_completo()}",
        "amarillo"
    )

    respuesta = input(
        "¿Desea eliminarlo? (s/n): "
    ).strip().lower()

    if respuesta not in RESPUESTAS_SI:
        imprimir_color(
            "Operación cancelada.",
            "amarillo"
        )
        return

    exito, mensaje = eliminar_estudiante(
        id_estudiante
    )

    if exito:
        imprimir_color(mensaje, "verde")
    else:
        imprimir_color(mensaje, "rojo")


def opcion_agregar_nota():
    limpiar_pantalla()
    imprimir_titulo("AGREGAR NOTA")

    id_estudiante = input(
        "ID del estudiante: "
    ).strip()

    estudiante = buscar_por_id(id_estudiante)

    if estudiante is None:
        imprimir_color(
            "Estudiante no encontrado.",
            "rojo"
        )
        return

    imprimir_color(
        f"Estudiante: "
        f"{estudiante.obtener_nombre_completo()}",
        "blanco"
    )

    materia = input("Materia: ").strip()
    nota = input("Nota (0 - 20): ").strip()

    exito, mensaje = agregar_nota(
        id_estudiante,
        materia,
        nota
    )

    if exito:
        imprimir_color(mensaje, "verde")
    else:
        imprimir_color(mensaje, "rojo")


def opcion_ver_promedio():
    limpiar_pantalla()
    imprimir_titulo("VER PROMEDIO")

    id_estudiante = input(
        "ID del estudiante: "
    ).strip()

    estudiante = buscar_por_id(id_estudiante)

    if estudiante is None:
        imprimir_color(
            "Estudiante no encontrado.",
            "rojo"
        )
        return

    imprimir_color(
        f"Estudiante: "
        f"{estudiante.obtener_nombre_completo()}",
        "blanco"
    )

    imprimir_color(
        f"Promedio: "
        f"{estudiante.obtener_promedio()}",
        "verde"
    )

    if estudiante.notas:
        print()

        for materia, notas in estudiante.notas.items():
            imprimir_color(
                f"{materia}: {notas}",
                "blanco"
            )
    else:
        imprimir_color(
            "El estudiante no tiene notas.",
            "amarillo"
        )


def opcion_materias_ofertadas():
    limpiar_pantalla()
    imprimir_titulo("MATERIAS OFERTADAS")

    materias = materias_ofertadas()

    if not materias:
        imprimir_color(
            "No hay materias registradas.",
            "amarillo"
        )
        return

    for materia in sorted(materias):
        imprimir_color(
            f"- {materia}",
            "blanco"
        )


def opcion_materias_en_comun():
    limpiar_pantalla()
    imprimir_titulo("MATERIAS EN COMÚN")

    id_a = input(
        "ID del primer estudiante: "
    ).strip()

    id_b = input(
        "ID del segundo estudiante: "
    ).strip()

    estudiante_a = buscar_por_id(id_a)
    estudiante_b = buscar_por_id(id_b)

    if estudiante_a is None:
        imprimir_color(
            "El primer estudiante no existe.",
            "rojo"
        )
        return

    if estudiante_b is None:
        imprimir_color(
            "El segundo estudiante no existe.",
            "rojo"
        )
        return

    materias = estudiantes_en_comun(
        id_a,
        id_b
    )

    if not materias:
        imprimir_color(
            "No tienen materias en común.",
            "amarillo"
        )
        return

    imprimir_color(
        "Materias en común:",
        "verde"
    )

    for materia in sorted(materias):
        imprimir_color(
            f"- {materia}",
            "blanco"
        )


def mostrar_menu():
    limpiar_pantalla()

    imprimir_titulo("SISTEMA DE ESTUDIANTES")

    imprimir_color("1. Crear estudiante", "blanco")
    imprimir_color("2. Listar estudiantes", "blanco")
    imprimir_color("3. Buscar estudiante", "blanco")
    imprimir_color("4. Actualizar estudiante", "blanco")
    imprimir_color("5. Eliminar estudiante", "blanco")
    imprimir_color("6. Agregar nota", "verde")
    imprimir_color("7. Ver promedio", "verde")
    imprimir_color("8. Materias ofertadas", "amarillo")
    imprimir_color("9. Materias en común", "amarillo")
    imprimir_color("0. Salir", "gris")


def main():
    while True:
        mostrar_menu()

        opcion = input(
            "\nSeleccione una opción: "
        ).strip()

        if opcion == "1":
            opcion_crear()

        elif opcion == "2":
            opcion_listar()

        elif opcion == "3":
            opcion_buscar()

        elif opcion == "4":
            opcion_actualizar()

        elif opcion == "5":
            opcion_eliminar()

        elif opcion == "6":
            opcion_agregar_nota()

        elif opcion == "7":
            opcion_ver_promedio()

        elif opcion == "8":
            opcion_materias_ofertadas()

        elif opcion == "9":
            opcion_materias_en_comun()

        elif opcion == "0":
            imprimir_color(
                "Programa finalizado.",
                "verde"
            )
            break

        else:
            imprimir_color(
                "Opción inválida.",
                "rojo"
            )

        pausar()


if __name__ == "__main__":
    main()