from gestor.tareas import Tareas
from gestor.helpers import validar_datos
from time import sleep


def mostrar_menu() -> None:
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tareas por etiqueta")
    print("6. Salir")


tarea = Tareas()

while True:
    mostrar_menu()

    try:
        opcion = int(input("Elija una opcion: "))

        match opcion:
            case 1:
                try:
                    while True:
                        print("\n")
                        titulo = input("Ingresa el titulo de la tarea: ")
                        descripcion = input("Descripcion: ")
                        fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
                        etiqueta = input("Etiqueta (opcional): ")
                        print("Verificando datos...")
                        sleep(1.5)
                        if validar_datos(titulo, descripcion, fecha_limite, etiqueta):
                            tarea.agregar_tarea(
                                titulo, descripcion, fecha_limite, etiqueta
                            )
                            print("Tarea agregada con exito.")
                            break
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 2:
                try:
                    print("Cargando tareas registradas")
                    sleep(1.5)
                    tarea.listar_tareas()
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 3:
                try:
                    while True:
                        id = int(input("Ingrese el id de la tarea a modificar: "))
                        print("Por favor espere un momento...")
                        sleep(1.5)
                        if not tarea.buscar_tarea_por_id(id):
                            print("No se encontro una tarea con el id especificado")
                            break
                        nuevo_titulo = input("Ingresa el titulo de la tarea: ")
                        nueva_descripcion = input("Descripcion: ")
                        nueva_fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
                        nueva_etiqueta = input("Etiqueta (opcional): ")
                        print("Resolviendo cambios...")
                        sleep(1.5)
                        if validar_datos(
                            nuevo_titulo,
                            nueva_descripcion,
                            nueva_fecha_limite,
                            nueva_etiqueta,
                        ):
                            tarea.editar_tareas(
                                id,
                                nuevo_titulo,
                                nueva_descripcion,
                                nueva_fecha_limite,
                                nueva_etiqueta,
                            )
                            print("Cambios realizados con exito.")
                            break
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 4:
                try:
                    id = int(input("Ingrese el id de la tarea a eliminar: "))
                    print("Por favor espere un momento...")
                    sleep(1.5)
                    if not tarea.buscar_tarea_por_id(id):
                        print("No se encontro una tarea con el id especificado")
                    else:
                        print("Eliminando tarea...")
                        sleep(1.5)
                        tarea.eliminar_tarea(id)
                        print("Tarea eliminada con exito.")
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 5:
                try:
                    etiqueta = input("Ingrese la etiqueta de busqueda: ")
                    print("Buscando tareas...")
                    sleep(1.5)
                    tareas = tarea.buscar_tarea_por_etiqueta(etiqueta)
                    if not tareas:
                        print("No se encontraron tareas con esa etiqueta")
                    else:
                        for t in tareas:
                            print("\n")
                            print(f'Id Tarea: {t["Id"]}')
                            print(f'Titulo: {t["Titulo"]}')
                            print(f'Descripcion: {t["Descripcion"]}')
                            print(f'Fecha Limite: {t["Fecha_Limite"]}')
                            print(f'Etiqueta: {t["Etiqueta"]}')
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 6:
                print("Hasta luego!")
                break
    except ValueError:
        print("Por favor ingrese un numero valido")
        continue
    except KeyboardInterrupt:
        print("\nVolviendo al menu principal...")
