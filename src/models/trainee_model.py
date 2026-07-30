import json
import os


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

def search_by_document(document):
    """Busca un aprendiz por su número de documento."""
    load_data()
    for a in trainees:
        if a["documento"] == document:
            return a
    return None

def register_trainee(new_trainee):
    """Registra un nuevo aprendiz si no existe previamente y guarda los cambios."""
    load_data()
    if search_by_document(new_trainee["documento"]):
        return False  # Ya existe
    trainees.append(new_trainee)
    save_data()
    return True