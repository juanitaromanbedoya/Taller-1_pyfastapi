import json
import os
import csv

# __file__ es src/models/trainee_model.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Estamos en src/models/
SRC_DIR = os.path.dirname(BASE_DIR)                    # Subimos a src/
ROOT_DIR = os.path.dirname(SRC_DIR)                    # Subimos a la raíz del proyecto
DATA_DIR = os.path.join(ROOT_DIR, "data")
DATABASE_FILE = os.path.join(DATA_DIR, "trainees.json")

trainees = []

def ensure_data_file_exists():
    """
    ¿Qué hace? Verifica si la carpeta 'data' en la raíz y el archivo 'trainees.json' existen. 
    Si no existen, los crea automáticamente.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)
        
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump([], file)  # Crea el archivo con una lista vacía

def load_data():
    """
    ¿Qué hace? Lee los datos guardados en el archivo JSON de la carpeta data/.
    """
    global trainees
    ensure_data_file_exists()
    try:
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            trainees = json.load(file)
    except json.JSONDecodeError:
        trainees = []

def save_data():
    """
    ¿Qué hace? Guarda la lista actual de aprendices dentro de la carpeta data/ en la raíz.
    """
    ensure_data_file_exists()
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(trainees, file, ensure_ascii=False, indent=4)

def get_all():
    """Obtiene todos los aprendices registrados."""
    load_data()
    return trainees

def add_trainee(trainee_data):
    """Agrega un nuevo aprendiz a la lista y guarda los cambios."""
    load_data()
    trainees.append(trainee_data)
    save_data()

def update_trainee(document, updated_data):
    """Actualiza los datos de un aprendiz existente según su documento."""
    load_data()
    for index, trainee in enumerate(trainees):
        if trainee["documento"] == document:
            # Actualizamos los campos manteniendo el documento original
            trainees[index].update(updated_data)
            save_data()
            return True
    return False

def delete_trainee(document):
    """Elimina un aprendiz de la lista según su documento."""
    load_data()
    global trainees
    initial_length = len(trainees)
    # Filtramos la lista para sacar al aprendiz con ese documento
    trainees = [t for t in trainees if t["documento"] != document]
    
    if len(trainees) < initial_length:
        save_data()
        return True
    return False

def search_by_document(document):
    """Busca un aprendiz por su número de documento."""
    load_data()
    for a in trainees:
        if a["documento"] == document:
            return a
    return None

def search_by_name(name_query):
    """Busca aprendices que contengan el texto ingresado en su nombre."""
    load_data()
    # Usamos .lower() para que la búsqueda no distinga entre mayúsculas y minúsculas
    results = [a for a in trainees if name_query.lower() in a["nombre"].lower()]
    return results

def search_by_file(ficha_number):
    """Busca aprendices que pertenezcan a un número de ficha específico."""
    load_data()
    results = [a for a in trainees if a["ficha"] == ficha_number]
    return results

def search_by_ficha(ficha_number):
    """Busca aprendices que pertenezcan a un número de ficha específico."""
    load_data()
    results = [a for a in trainees if a["ficha"] == ficha_number]
    return results

def register_trainee(new_trainee):
    """Registra un nuevo aprendiz si no existe previamente y guarda los cambios."""
    load_data()
    if search_by_file and search_by_name (new_trainee["Nombre,ficha"]):
        return False  # Ya existe
    trainees.append(new_trainee)
    save_data()
    return True


def export_to_csv(filename="trainees_export.csv"):
    """Exporta la lista de aprendices a un archivo CSV."""
    load_data()
    if not trainees:
        return False
    
    # Asegurarnos de que exista la carpeta data o guardar en la raíz
    os.makedirs("data", exist_ok=True)
    filepath = os.path.join("data", filename)
    
    try:
        # Obtenemos las llaves del diccionario a partir del primer aprendiz
        keys = trainees[0].keys()
        with open(filepath, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(trainees)
        return True
    except Exception as e:
        print(f"Error al exportar: {e}")
        return False