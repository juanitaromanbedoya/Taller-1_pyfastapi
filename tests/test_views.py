import pytest
from unittest.mock import patch
from views import trainee_view


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """
    Fixture que se ejecuta automáticamente antes de cada prueba.
    Garantiza un entorno limpio o simulado.
    """
    yield


@patch("templates.trainee_template.display_message")
@patch("templates.trainee_template.get_trainee_input")
@patch("models.trainee_model.register_trainee")
def test_register_trainee_view_success(
    mock_register,
    mock_get_input,
    mock_display_msg,
):
    mock_input_data = {
        "tipo_doc": "CC",
        "documento": 12345,
        "nombre": "Juan Perez",
        "correo": "juan@sena.edu.co",
        "ficha": 2671234,
        "programa": "ADSO",
    }

    mock_get_input.return_value = mock_input_data
    mock_register.return_value = True

    trainee_view.register_trainee_view()

    mock_register.assert_called_once_with(mock_input_data)

    mock_display_msg.assert_called_once_with(
        {
            "type": "success",
            "text": "Aprendiz Juan Perez registrado exitosamente."
        }
    )

@patch("templates.trainee_template.display_message")
@patch("templates.trainee_template.get_trainee_input")
@patch("models.trainee_model.register_trainee")
def test_register_trainee_view_duplicate(
    mock_register,
    mock_get_input,
    mock_display_msg,
):
    mock_input_data = {
        "tipo_doc": "CC",
        "documento": 12345,
        "nombre": "Juan Perez",
        "correo": "juan@sena.edu.co",
        "ficha": 2671234,
        "programa": "ADSO",
    }

    mock_get_input.return_value = mock_input_data

    mock_register.return_value = False

    trainee_view.register_trainee_view()

    mock_register.assert_called_once_with(mock_input_data)

    mock_display_msg.assert_called_once_with(
        {
            "type": "error",
            "text": "Ya existe un aprendiz con el documento 12345."
        }
    )

# --- PRUEBA 3: Listado de Aprendices ---
# Cambiamos 'display_trainees_list' por 'display_trainee_list' (singular) que es como se llama en tu vista
@patch("templates.trainee_template.display_trainee_list")
@patch("models.trainee_model.get_all")
def test_list_view(mock_get_all, mock_display_list):
    """Prueba que list_view obtenga todos los aprendices y los envíe a la plantilla."""

    mock_trainees = [
        {"documento": "123", "nombre": "Ana"},
        {"documento": "456", "nombre": "Carlos"},
    ]

    mock_get_all.return_value = mock_trainees

    trainee_view.status_view()

    mock_get_all.assert_called_once()

    # Tu función status_view solo le pasa los datos, sin texto extra de título
    mock_display_list.assert_called_once_with(mock_trainees)