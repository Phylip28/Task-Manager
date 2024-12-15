class Tareas:
    def __init__(self) -> None:
        self.tareas = {}
        self.id_tarea = 0

    def agregar_tarea(self, titulo, descripcion, fecha_limite, etiqueta) -> None:
        self.id_tarea += 1
        self.tareas[self.id_tarea] = {
            "Id": self.id_tarea,
            "Titulo": titulo,
            "Descripcion": descripcion,
            "Fecha_Limite": fecha_limite,
            "Etiqueta": etiqueta,
        }

    def listar_tareas(self) -> str | None:
        if not self.tareas:
            print("No hay tareas registradas")
            return
        for tarea in self.tareas.values():
            self.mostrar_tareas(tarea)

    def editar_tareas(
        self, id, nuevo_titulo, nueva_descripcion, nueva_fecha_limite, nueva_etiqueta
    ) -> bool:
        if not self.tareas:
            print("No hay tareas registradas")
            return False
        self.tareas[id].update(
            {
                "Titulo": nuevo_titulo,
                "Descripcion": nueva_descripcion,
                "Fecha_Limite": nueva_fecha_limite,
                "Etiqueta": nueva_etiqueta,
            }
        )
        return True

    def eliminar_tarea(self, id: int) -> bool:
        if not self.tareas:
            print("No hay tareas registradas")
            return False
        for ids, tareas in self.tareas.items():
            if tareas["Id"] == id:
                del self.tareas[ids]
                return True
        return False

    def buscar_tarea_por_etiqueta(self, etiqueta) -> list:
        return [
            etiquetas
            for etiquetas in self.tareas.values()
            if etiquetas["Etiqueta"] == etiqueta
        ]

    def buscar_tarea_por_id(self, id) -> dict | None:
        return self.tareas.get(id, None)

    def mostrar_tareas(self, tarea) -> None:
        print(
            f"Id: {tarea['Id']}",
            f"Titulo: {tarea['Titulo']}",
            f"Descripcion: {tarea['Descripcion']}",
            f"Fecha Limite: {tarea['Fecha_Limite']}",
            f"Etiqueta: {tarea['Etiqueta']}",
            sep="\n",
        )
