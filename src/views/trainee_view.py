from models import trainee_model
from templates import trainee_template


def init_app_data():
    """Inicializa los datos de la aplicación."""
    trainee_model.load_data()


def register_trainee_view():
    """Registra un nuevo aprendiz."""
    data = trainee_template.get_trainee_input()

    success = trainee_model.register_trainee(data)

    if not success:
        trainee_template.display_message({
            "type": "error",
            "text": f"Ya existe un aprendiz con el documento {data['documento']}."
        })
        return

    trainee_template.display_message({
        "type": "success",
        "text": f"Aprendiz {data['nombre']} registrado exitosamente."
    })


def status_view():
    """Muestra todos los aprendices registrados."""
    trainee_template.display_trainee_list(
        trainee_model.get_all()
    )


def edit_trainee_view():
    """Actualiza la información de un aprendiz."""
    document = trainee_template.get_document_to_search()

    trainee = trainee_model.search_by_document(document)

    if not trainee:
        trainee_template.display_message({
            "type": "error",
            "text": "Aprendiz no encontrado."
        })
        return

    trainee_template.display_message({
        "type": "info",
        "text": f"Aprendiz encontrado: {trainee['nombre']}"
    })

    updated_data = trainee_template.get_update_input()

    if not trainee_template.confirm_action("actualizar"):
        return

    success = trainee_model.update_trainee(document, updated_data)

    trainee_template.display_message({
        "type": "success" if success else "error",
        "text": "Aprendiz actualizado exitosamente."
        if success else
        "No fue posible actualizar el aprendiz."
    })


def delete_trainee_view():
    """Elimina un aprendiz."""
    document = trainee_template.get_document_to_search()

    trainee = trainee_model.search_by_document(document)

    if not trainee:
        trainee_template.display_message({
            "type": "error",
            "text": "Aprendiz no encontrado."
        })
        return

    trainee_template.display_message({
        "type": "info",
        "text": f"Aprendiz a eliminar: {trainee['nombre']}"
    })

    if not trainee_template.confirm_action("eliminar"):
        return

    success = trainee_model.delete_trainee(document)

    trainee_template.display_message({
        "type": "success" if success else "error",
        "text": "Aprendiz eliminado exitosamente."
        if success else
        "No fue posible eliminar el aprendiz."
    })


def show_search_results(results, empty_message):
    """Muestra los resultados de una búsqueda."""

    if not results:
        trainee_template.display_message({
            "type": "info",
            "text": empty_message
        })
        return

    trainee_template.display_trainee_list(results)


def search_by_name_view():
    """Busca aprendices por nombre."""
    name = trainee_template.get_name_to_search()

    results = trainee_model.search_by_name(name)

    show_search_results(
        results,
        "No se encontraron aprendices con ese nombre."
    )


def search_by_ficha_view():
    """Busca aprendices por ficha."""
    ficha = trainee_template.get_ficha_to_search()

    results = trainee_model.search_by_ficha(ficha)

    show_search_results(
        results,
        f"No se encontraron aprendices en la ficha {ficha}."
    )


def export_csv_view():
    """Exporta la información a un archivo CSV."""

    success = trainee_model.export_to_csv()

    trainee_template.display_message({
        "type": "success" if success else "info",
        "text":
            "Lista de aprendices exportada correctamente a 'data/trainees_export.csv'."
            if success else
            "No hay aprendices registrados para exportar."
    })