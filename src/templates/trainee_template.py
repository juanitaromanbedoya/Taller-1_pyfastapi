import re

# Capa TEMPLATE: Interfaz de usuario por consola para registrar aprendices

def get_trainee_input():
    """Solicita al usuario los datos para registrar un aprendiz con validaciones robustas."""
    
    # 1. Validar documento (Debe ser numérico)
    while True:
        id_str = input("Número de documento: ").strip()
        if id_str.isdigit():
            id = int(id_str)
            break
        print("⚠️ Error: El número de documento debe contener solo dígitos.")

    # 2. Tipo de documento
    while True:
        type_id = input("Tipo de documento (CC/TI/CE): ").strip().upper()
        if type_id in ["CC", "TI", "CE"]:
            break
        print("⚠️ Opción inválida. Debe ser CC, TI o CE. Inténtalo de nuevo.")

    # 3. Nombre completo (Validar que no esté vacío y contenga letras)
    while True:
        name = input("Nombre completo: ").strip().title()
        if name and all(x.isalpha() or x.isspace() for x in name):
            break
        print("⚠️ Error: El nombre solo debe contener letras.")

    # 4. Correo electrónico (Validar formato básico con expresiones regulares)
    while True:
        mail = input("Ingrese Correo electrónico: ").strip()
        if "@" in mail and "." in mail: 
            break
        print("⚠️ Correo inválido. Debe incluir '@' y un punto '.'. Inténtalo de nuevo.")

    # 5. Número de Ficha (Debe ser numérico)
    while True:
        group_str = input("Número de Ficha: ").strip()
        if group_str.isdigit():
            group_code = int(group_str)
            break
        print("⚠️ Error: El número de ficha debe contener solo dígitos.")

    # 6. Programa de Formación
    program = input("Programa de Formación: ").strip().title()

    return {
        "tipo_doc": type_id,
        "documento": id,
        "nombre": name,
        "correo": mail,
        "ficha": group_code,
        "programa": program,
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
    """Solicita los nuevos datos para actualizar un aprendiz."""
    print("\n--- Actualizar Datos del Aprendiz ---")
    type_id = input("Actualice tipo de documento (CC/TI/CE): ").strip().upper()
    
    while True:
        name = input("Actualice nombre completo: ").strip().title()
        if name and all(x.isalpha() or x.isspace() for x in name):
            break
        print("⚠️ Error: El nombre solo debe contener letras.")

    while True:
        mail = input("Actualice correo electrónico: ").strip()
        if "@" in mail and "." in mail:
            break
        print("⚠️ Correo inválido. Debe incluir '@' y un punto '.'.")

    while True:
        group_str = input("Actualice número de ficha: ").strip()
        if group_str.isdigit():
            group_code = int(group_str)
            break
        print("⚠️ Error: La ficha debe ser numérica.")

    program = input("Actualice programa de formación: ").strip().title()

    return {
        "tipo_doc": type_id,
        "nombre": name,
        "correo": mail,
        "ficha": group_code,
        "programa": program,
    }

def get_name_to_search():
    """Solicita un nombre o parte de él para realizar la búsqueda."""
    return input("Ingrese el nombre o parte del nombre a buscar: ").strip()

def get_ficha_to_search():
    """Solicita el número de ficha para buscar."""
    while True:
        ficha_str = input("Ingrese el número de ficha a buscar: ").strip()
        if ficha_str.isdigit():
            return int(ficha_str)
        print("⚠️ Error: El número de ficha debe contener solo dígitos.")

def confirm_action(action_name):
    """Confirma si el usuario desea realizar una acción crítica (eliminar/actualizar)."""
    confirm = input(f"¿Estás seguro de que deseas {action_name} este aprendiz? (si/no): ").strip().lower()
    return confirm == "si"

def display_confirm_next():
    """Pregunta al usuario si desea registrar otro aprendiz."""
    display_message({"type": "info", "text": "¿Deseas registrar otro aprendiz? (si/no)"})

    next_option = input("").strip().lower()
    return next_option == "si"

def get_document_to_search():
    """Solicita el número de documento para buscar, actualizar o eliminar."""
    while True:
        doc_str = input("Ingrese el número de documento del aprendiz: ").strip()
        if doc_str.isdigit():
            return int(doc_str)
        print("⚠️ Error: El documento debe contener solo dígitos.")