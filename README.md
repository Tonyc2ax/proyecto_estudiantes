# Sistema de Gestión de Estudiantes

Proyecto desarrollado en Python para administrar información de estudiantes utilizando una estructura basada en clases, archivos JSON y funciones separadas por módulos.

## Funcionalidades

El sistema permite:

- Crear estudiantes.
- Listar estudiantes registrados.
- Buscar estudiantes por nombre, apellido, correo o carnet.
- Actualizar información de un estudiante.
- Eliminar estudiantes.
- Agregar notas por materia.
- Calcular el promedio de cada estudiante.
- Mostrar las materias registradas.
- Consultar materias en común entre dos estudiantes.
- Validar que el carnet no esté repetido.
- Validar datos ingresados por el usuario.

## Estructura del proyecto

```text
proyecto_estudiantes/
│
├── data/
│   └── estudiantes.json
│
├── shared/
│   ├── __init__.py
│   ├── herramientas.py
│   └── json_manager.py
│
├── main.py
├── model.py
├── views.py
└── README.md