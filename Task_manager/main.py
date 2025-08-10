# Importa las clases y funciones necesarias
from gestor.tareas import Tareas  # Importa la clase Tareas desde el módulo tareas
from gestor.helpers import validar_datos  # Importa la función validar_datos desde el módulo helpers
from time import sleep  # Importa la función sleep para hacer pausas en la ejecución

# Función que muestra el menú principal del sistema
def mostrar_menu() -> None:
    print("\nSistema de Gestión de Tareas")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Buscar tareas por etiqueta")
    print("6. Salir")

# Crear una instancia de la clase Tareas
tarea = Tareas()

# Bucle principal del sistema
while True:
    mostrar_menu()  # Muestra el menú

    try:
        # Solicita al usuario que ingrese una opción del menú
        opcion = int(input("Elija una opcion: "))

        # Uso de match-case para ejecutar la opción seleccionada
        match opcion:
            case 1:
                try:
                    while True:
                        # Solicita datos para la nueva tarea
                        print("\n")
                        titulo = input("Ingresa el titulo de la tarea: ")
                        descripcion = input("Descripcion: ")
                        fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
                        etiqueta = input("Etiqueta (opcional): ")
                        print("Verificando datos...")
                        sleep(1.5)
                        # Verifica que los datos sean válidos
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
                    # Muestra las tareas registradas
                    print("Cargando tareas registradas")
                    sleep(1.5)
                    tarea.listar_tareas()
                except KeyboardInterrupt:
                    print("\nVolviendo al menu...")
            case 3:
                try:
                    # Solicita el id de la tarea para editarla
                    while True:
                        id = int(input("Ingrese el id de la tarea a modificar: "))
                        print("Por favor espere un momento...")
                        sleep(1.5)
                        # Verifica si la tarea existe
                        if not tarea.buscar_tarea_por_id(id):
                            print("No se encontro una tarea con el id especificado")
                            break
                        nuevo_titulo = input("Ingresa el titulo de la tarea: ")
                        nueva_descripcion = input("Descripcion: ")
                        nueva_fecha_limite = input("Fecha limite (YYYY-MM-DD): ")
                        nueva_etiqueta = input("Etiqueta (opcional): ")
                        print("Resolviendo cambios...")
                        sleep(1.5)
                        # Verifica que los datos sean válidos antes de realizar el cambio
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
                    # Solicita el id de la tarea a eliminar
                    id = int(input("Ingrese el id de la tarea a eliminar: "))
                    print("Por favor espere un momento...")
                    sleep(1.5)
                    # Verifica si la tarea existe antes de eliminarla
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
                    # Solicita la etiqueta de búsqueda para listar tareas
                    etiqueta = input("Ingrese la etiqueta de busqueda: ")
                    print("Buscando tareas...")
                    sleep(1.5)
                    tareas = tarea.buscar_tarea_por_etiqueta(etiqueta)
                    # Muestra las tareas encontradas o un mensaje si no hay resultados
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
