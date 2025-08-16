# Crea una lista de tareas como diccionarios.
# Escribe una función que marque una tarea como completada por su id.

tareas = [
    {"id": 1, "descripcion": "Estudiar Python", "completado": False},
    {"id": 2, "descripcion": "Leer sobre APIs", "completado": True},
]


def marcar_tarea(id_tarea: int):
    for tarea in tareas:
        if tarea.get("id") == id_tarea:
            print(tarea)
            # print(tarea["completado"])
            tarea["completado"] = True
            print(tarea)
            break


if __name__ == "__main__":
    marcar_tarea(1)
