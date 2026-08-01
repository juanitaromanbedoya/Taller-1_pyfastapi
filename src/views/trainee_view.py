from models import trainee_model
from templates import trainee_template

def init_app_data():
    """Inicializa los datos de la aplicación, creando la tabla de aprendices si no existe."""
    trainee_model.load_data()


def register_trainee_view():
    """Vista para registrar un nuevo aprendiz validando que no esté duplicado."""
    
    data = trainee_template.get_trainee_input()
    if trainee_model.search_by_document(data["documento"]):
        trainee_template.display_message({
            "type": "error", 
            "text": f"Ya existe un aprendiz registrado con el número de documento {data['documento']}."
        })
        return

    trainee_model.add_trainee(data)
    
    # 4. Mostrar mensaje de éxito
    trainee_template.display_message({
        "type": "success", 
        "text": f"Aprendiz {data['nombre']} registrado exitosamente en la ficha {data['ficha']}."
    })

def status_view():
    """Muestra el estado actual de la lista de aprendices registrados."""
    all_trainees = trainee_model.get_all()
    trainee_template.display_trainee_list(all_trainees)


def edit_trainee_view():
    """Edita los datos del aprendiz"""
    doc = trainee_template.get_document_to_search()
    aprendiz = trainee_model.search_by_document(doc)
    
    if not aprendiz:
        trainee_template.display_message({"type": "error", "text": "Aprendiz no encontrado."})
        return

    print(f"\nAprendiz encontrado: {aprendiz['nombre']}")
    nuevos_datos = trainee_template.get_update_input()
    
    if trainee_template.confirm_action("actualizar"):
        success = trainee_model.update_trainee(doc, nuevos_datos)
        if success:
            trainee_template.display_message({"type": "success", "text": "Aprendiz actualizado exitosamente."})
        else:
            trainee_template.display_message({"type": "error", "text": "No se pudo actualizar."})

def delete_trainee_view():
    """Elimina Datos del aprendiz"""
    doc = trainee_template.get_document_to_search()
    aprendiz = trainee_model.search_by_document(doc)
    
    if not aprendiz:
        trainee_template.display_message({"type": "error", "text": "Aprendiz no encontrado."})
        return

    print(f"\nAprendiz a eliminar: {aprendiz['nombre']}")
    if trainee_template.confirm_action("eliminar"):
        success = trainee_model.delete_trainee(doc)
        if success:
            trainee_template.display_message({"type": "success", "text": "Aprendiz eliminado exitosamente."})
        else:
            trainee_template.display_message({"type": "error", "text": "No se pudo eliminar."})



def search_by_name_view():
    """Vista para buscar aprendices por nombre."""
    name_query = trainee_template.get_name_to_search()
    results = trainee_model.search_by_name(name_query)
    
    if not results:
        trainee_template.display_message({"type": "info", "text": "No se encontraron aprendices con ese nombre."})
    else:
        print(f"\n--- Resultados de búsqueda por nombre: '{name_query}' ---")
        trainee_template.display_trainee_list(results)

def search_by_ficha_view():
    """Vista para buscar aprendices por número de ficha."""
    ficha_number = trainee_template.get_ficha_to_search()
    results = trainee_model.search_by_ficha(ficha_number)
    
    if not results:
        trainee_template.display_message({"type": "info", "text": f"No se encontraron aprendices en la ficha {ficha_number}."})
    else:
        print(f"\n--- Resultados de búsqueda para la Ficha: {ficha_number} ---")
        trainee_template.display_trainee_list(results)

def export_csv_view():
    """Vista para exportar los aprendices a un archivo CSV."""
    success = trainee_model.export_to_csv()
    if success:
        trainee_template.display_message({
            "type": "success", 
            "text": "Lista de aprendices exportada exitosamente a 'data/trainees_export.csv'."
        })
    else:
        trainee_template.display_message({
            "type": "info", 
            "text": "No hay aprendices registrados para exportar."
        })