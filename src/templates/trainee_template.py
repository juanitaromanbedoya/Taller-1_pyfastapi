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


def display_confirm_next():
    """Pregunta al usuario si desea registrar otro aprendiz."""
    display_message({"type": "info", "text": "¿Deseas registrar otro aprendiz? (si/no)"})

    next_option = input("").strip().lower()
    return next_option == "si"