from datetime import datetime


def validar_datos(titulo, descripcion, fecha_limite, etiqueta) -> bool:
    campos = {
        "Titulo": titulo,
        "Descripcion": descripcion,
        "Fecha limite": fecha_limite,
        "Etiqueta": etiqueta,
    }
    for campo, valor in campos.items():
        if not valor:
            print(f"El campo {campo} no puede estar vacío.")
            return False
    try:
        datetime.strptime(fecha_limite, "%Y-%m-%d")
    except ValueError:
        print("La fecha limite no es una fecha valida")
        return False
    return True
