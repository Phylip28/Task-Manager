# Importa la clase datetime desde el módulo datetime para trabajar con fechas
from datetime import datetime

# Función que valida los datos ingresados para la tarea
def validar_datos(titulo, descripcion, fecha_limite, etiqueta) -> bool:
    # Diccionario con los campos a validar
    campos = {
        "Titulo": titulo,
        "Descripcion": descripcion,
        "Fecha limite": fecha_limite,
        "Etiqueta": etiqueta,
    }
    # Verifica si algún campo está vacío
    for campo, valor in campos.items():
        if not valor:
            print(f"El campo {campo} no puede estar vacío.")
            return False
    try:
        # Verifica que la fecha límite tenga el formato correcto
        datetime.strptime(fecha_limite, "%Y-%m-%d")
    except ValueError:
        print("La fecha limite no es una fecha valida")
        return False
    return True
