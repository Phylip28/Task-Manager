# Clase que gestiona las tareas
class Tareas:
    def __init__(self) -> None:
        # Diccionario para almacenar las tareas, con el id como clave
        self.tareas = {}
        # Variable para generar un id único para cada tarea
        self.id_tarea = 0

    # Método para agregar una nueva tarea
    def agregar_tarea(self, titulo, descripcion, fecha_limite, etiqueta) -> None:
        self.id_tarea += 1
        # Almacena la tarea en el diccionario usando el id generado
        self.tareas[self.id_tarea] = {
            "Id": self.id_tarea,
            "Titulo": titulo,
            "Descripcion": descripcion,
            "Fecha_Limite": fecha_limite,
            "Etiqueta": etiqueta,
        }

    # Método para listar todas las tareas registradas
    def listar_tareas(self) -> str | None:
        if not self.tareas:
            print("No hay tareas registradas")
            return
        for tarea in self.tareas.values():
            self.mostrar_tareas(tarea)

    # Método para editar una tarea existente
    def editar_tareas(
        self, id, nuevo_titulo, nueva_descripcion, nueva_fecha_limite, nueva_etiqueta
    ) -> bool:
        if not self.tareas:
            print("No hay tareas registradas")
            return False
        # Actualiza la tarea con el id especificado
        self.tareas[id].update(
            {
                "Titulo": nuevo_titulo,
                "Descripcion": nueva_descripcion,
                "Fecha_Limite": nueva_fecha_limite,
                "Etiqueta": nueva_etiqueta,
            }
        )
        return True

    # Método para eliminar una tarea existente
    def eliminar_tarea(self, id: int) -> bool:
        if not self.tareas:
            print("No hay tareas registradas")
            return False
        for ids, tareas in self.tareas.items():
            if tareas["Id"] == id:
                del self.tareas[ids]
                return True
        return False

    # Método para buscar tareas por etiqueta
    def buscar_tarea_por_etiqueta(self, etiqueta) -> list:
        return [
            etiquetas
            for etiquetas in self.tareas.values()
            if etiquetas["Etiqueta"] == etiqueta
        ]

    # Método para buscar una tarea por su id
    def buscar_tarea_por_id(self, id) -> dict | None:
        return self.tareas.get(id, None)

    # Método para mostrar los detalles de una tarea
    def mostrar_tareas(self, tarea) -> None:
        print(
            f"Id: {tarea['Id']}",
            f"Titulo: {tarea['Titulo']}",
            f"Descripcion: {tarea['Descripcion']}",
            f"Fecha Limite: {tarea['Fecha_Limite']}",
            f"Etiqueta: {tarea['Etiqueta']}",
            sep="\n",
        )
