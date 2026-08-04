import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"


def input_numeric(message):
    """Solicita un dato numérico."""
    while True:
        value = input(message).strip()

        if value.isdigit():
            return int(value)

        print("⚠️ Error: Solo se permiten números.")


def input_name(message):
    """Solicita un nombre válido."""
    while True:
        name = input(message).strip().title()

        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", name):
            return name

        print("⚠️ Error: El nombre solo puede contener letras y espacios.")


def input_email(message):
    """Solicita un correo válido."""
    while True:
        email = input(message).strip()

        if re.fullmatch(EMAIL_REGEX, email):
            return email

        print("⚠️ Error: Correo electrónico inválido.")


def input_document_type():
    """Solicita el tipo de documento."""
    while True:
        document_type = input("Tipo de documento (CC/TI/CE): ").strip().upper()

        if document_type in ("CC", "TI", "CE"):
            return document_type

        print("⚠️ Debe ingresar CC, TI o CE.")

def get_trainee_input():
    """Solicita los datos para registrar un aprendiz."""

    return {
        "tipo_doc": input_document_type(),
        "documento": input_numeric("Número de documento: "),
        "nombre": input_name("Nombre completo: "),
        "correo": input_email("Correo electrónico: "),
        "ficha": input_numeric("Número de ficha: "),
        "programa": input("Programa de formación: ").strip().title()
    }


def display_message(message):
    icons = {"success": "✅ ", "error": "⚠️ ", "info": "ℹ️ "}
    print(f"{icons.get(message['type'], '')} {message['text']}")


def display_trainee_list(trainee):
    """Muestra la lista de aprendices registrados."""
    if not trainee:
        print("No hay aprendices registrados.")
        return

    print("\n--- Lista de Aprendices Registrados ---")
    for trai in trainee:
        print(
            f"Documento: {trai['documento']}, Nombre: {trai['nombre']}, Correo: {trai['correo']}, Ficha: {trai['ficha']}, Programa: {trai['programa']}"
        )

def get_update_input():
    """Solicita los nuevos datos del aprendiz."""

    return {
        "tipo_doc": input_document_type(),
        "nombre": input_name("Nuevo nombre: "),
        "correo": input_email("Nuevo correo: "),
        "ficha": input_numeric("Nueva ficha: "),
        "programa": input("Nuevo programa: ").strip().title()
    }

def get_name_to_search():
    """Solicita un nombre o parte de él para realizar la búsqueda."""
    return input("Ingrese el nombre o parte del nombre a buscar: ").strip()

def get_ficha_to_search():
    """Solicita el número de ficha."""
    return input_numeric("Ingrese el número de ficha: ")

def confirm_action(action_name):
    """Confirma si el usuario desea realizar una acción crítica (eliminar/actualizar)."""
    confirm = input(f"¿Estás seguro de que deseas {action_name} este aprendiz? (si/no): ").strip().lower()
    return confirm == "si"


def get_document_to_search():
    """Solicita el documento del aprendiz."""
    return input_numeric("Ingrese el número de documento: ")

def display_confirm_next():
    """Pregunta al usuario si desea registrar otro aprendiz."""
    display_message({"type": "info", "text": "¿Deseas registrar otro aprendiz? (si/no)"})

    next_option = input("").strip().lower()
    return next_option == "si"