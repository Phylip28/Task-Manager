from random import randint
from time import sleep


def tablero_sudoku():
    # Crea matriz 9x9 vacía con puntos
    tablero = [["•"] * 9 for _ in range(9)]
    return tablero


def tablero_inicial(tablero):
    # Coloca números aleatorios en las esquinas de cada bloque 3x3
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                tablero[i][j] = randint(1, 9)
            else:
                tablero[i][j] = "•"
    return tablero


def imprimir_tablero(tablero):
    # Imprime el tablero con formato y coordenadas
    print("    1 2 3   4 5 6   7 8 9")
    for i in range(9):
        if i % 3 == 0:
            print("  +-------+-------+-------+")
        print(chr(65 + i), end=" ")
        for j in range(9):
            if j % 3 == 0:
                print("|", end=" ")
            print(tablero[i][j], end=" ")
        print("|")
    print("  +-------+-------+-------+")


def verificar_tablero(tablero):
    # Obtiene las coordenadas de las celdas vacías
    campo = [
        (fila, columna)
        for fila in range(9)
        for columna in range(9)
        if tablero[fila][columna] == "•"
    ]
    return campo if campo else False


def marcar(tablero, coordenada, valor):
    try:
        # Verifica si el tablero está lleno
        if not verificar_tablero(tablero):
            raise ValueError(" El tablero está lleno")
        coordenada = coordenada.replace(" ", "")

        # Valida formato de coordenada (ej: B9)
        if len(coordenada) != 2:
            raise ValueError("Por favor ingrese una coordenada valida, por ejemplo: B9")
        fila = ord(coordenada[0].upper()) - 65
        columna = int(coordenada[1]) - 1

        # Valida rango de coordenadas
        if not (0 <= fila <= 8 and 0 <= columna <= 8):
            raise ValueError("Las coordenadas estan entre A1 y I9, por ejemplo: F5")

        # Valida valor entre 1 y 9
        if not (1 <= valor <= 9):
            raise ValueError(
                "Por favor ingrese un valor valido entre 1 y 9, por ejemplo: 4"
            )

        # Verifica si la celda está vacía
        if tablero[fila][columna] != "•":
            raise ValueError("La posición ya está ocupada")
        tablero[fila][columna] = valor
        return True

    except ValueError as e:
        print(f"Error: {e}")
        return False


def verificar_filas_columnas_y_bloques(tablero):
    # Verifica filas
    for fila in range(9):
        valores_fila = [
            tablero[fila][columna]
            for columna in range(9)
            if tablero[fila][columna] != "•"
        ]
        if len(valores_fila) == 9 and len(set(valores_fila)) != 9:
            return False

    # Verifica columnas
    for columna in range(9):
        valores_columna = [
            tablero[fila][columna] for fila in range(9) if tablero[fila][columna] != "•"
        ]
        if len(valores_columna) == 9 and len(set(valores_columna)) != 9:
            return False

    # Verifica bloques 3x3
    for bloque_fila in range(3):
        for bloque_columna in range(3):
            valores_bloque = []

            for fila in range(3):
                for columna in range(3):
                    valores = tablero[fila + bloque_fila * 3][
                        columna + bloque_columna * 3
                    ]
                    if valores != "•":
                        valores_bloque.append(valores)

                    if len(valores_bloque) == 9 and len(set(valores_bloque)) != 9:
                        return False
    return True


def condicion_victoria(tablero):
    # Verifica si se ganó el juego
    if verificar_tablero(tablero) and verificar_filas_columnas_y_bloques(tablero):
        print("Has ganado!")
        return True


def intrucciones():
    # Lista de mensajes instructivos
    mensajes = [
        # Mensajes generales
        "Bienvenido al juego de Sudoku.",
        "Por favor, selecciona una opción del menú.",
        # Instrucciones del menú principal
        "1. Iniciar juego: Comienza una nueva partida de Sudoku.",
        "2. Cómo jugar: Aprende las reglas del juego y cómo interactuar.",
        "3. Salir del juego: Termina la sesión actual.",
        # Instrucciones de juego
        "Ingresa una coordenada en formato letra-número (ejemplo: C6).",
        "Ingresa un valor entre 1 y 9 para llenar la celda.",
        "Asegúrate de que la celda seleccionada esté vacía antes de intentar llenarla.",
        "Para ganar, llena el tablero respetando las reglas del Sudoku.",
    ]

    for mensaje in mensajes:
        print(mensaje)
        sleep(1.5)


# Bucle principal del juego
while True:
    print(
        f"""
    Bienvenido al juego de Sudoku
            
    1. Iniciar juego
    2. Como jugar
    3. Salir del juego
    """
    )
    try:
        opcion = int(input("Elija una opción: "))

        match opcion:
            case 1:
                try:
                    # Inicia nueva partida
                    tablero = tablero_inicial(tablero_sudoku())
                    print("Cargando tablero inicial...")
                    sleep(2)
                    imprimir_tablero(tablero)

                    while True:
                        if verificar_tablero(tablero):
                            coordenada = input("Ingresa la coordenada: ")
                            valor = int(input("Ingresa el valor: "))
                            marcar(tablero, coordenada, valor)
                            imprimir_tablero(tablero)

                            # Verifica si el movimiento fue válido
                            if not verificar_filas_columnas_y_bloques(tablero):
                                print("Has perdido, buena suerte en la próxima partida")
                                break
                        else:
                            condicion_victoria(tablero)
                            break
                except TypeError:
                    print("Error: Solo se permiten numeros")
                except KeyboardInterrupt:
                    print("\nJuego interrumpido. Volviendo al menú principal... ")
            case 2:
                intrucciones()
            case 3:
                print("Gracias por jugar. ¡Hasta la próxima!")
                break
            case default:
                print("Selecciona alguna de las opciones del menu")
    except ValueError:
        print("Por favor ingresa un numero válido")
    except KeyboardInterrupt:
        print("\nPara salir, usa la opción 3 del menú.")
