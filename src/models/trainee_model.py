import json
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"

DATABASE_FILE = DATA_DIR / "trainees.json"
trainees = []

def ensure_data_file_exists():
    """Crea la carpeta data y el archivo trainees.json si no existen."""

    DATA_DIR.mkdir(exist_ok=True)

    if not DATABASE_FILE.exists():

        DATABASE_FILE.write_text(
            "[]",
            encoding="utf-8"
        )

def load_data():
    """
    ¿Qué hace? Lee los datos guardados en el archivo JSON de la carpeta data/.
    """
    global trainees
    ensure_data_file_exists()
    try:
        with DATABASE_FILE.open(
            "r",
            encoding="utf-8"
        )  as file:   
            trainees = json.load(file)
    except json.JSONDecodeError:
        trainees = []

def save_data():
    """¿Qué hace? Guarda la lista actual de aprendices dentro de la carpeta data/ en la raíz."""

    ensure_data_file_exists()

    with DATABASE_FILE.open("w", encoding="utf-8") as file:
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


def search_by_ficha(ficha_number):
    """Busca aprendices que pertenezcan a un número de ficha específico."""
    load_data()
    results = [a for a in trainees if a["ficha"] == ficha_number]
    return results

def register_trainee(new_trainee):
    """Registra un aprendiz si el documento no existe"""
    load_data()

    if search_by_document(new_trainee["documento"]):
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
    filepath = DATA_DIR / filename
    
    try:
        # Obtenemos las llaves del diccionario a partir del primer aprendiz
        keys = trainees[0].keys()

        with filepath.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(trainees)

        return True
    
    except Exception as e:
        print(f"Error al exportar: {e}")
        return False