from views import trainee_view
from templates import trainee_template

def main():
    # Inicializa los datos de la aplicación y el archivo JSON
    trainee_view.init_app_data()
    
    while True:
        print("1. Registrar nuevo aprendiz")
        print("2. Ver lista de todos los aprendices")
        print("3. Actualizar datos de un aprendiz")
        print("4. Eliminar un aprendiz")
        print("5. Buscar aprendices por nombre")
        print("6. Buscar aprendices por número de ficha")
        print("7. Salir")
        
        opcion = input("\nSelecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            trainee_view.register_trainee_view()
        elif opcion == "2":
            trainee_view.status_view()
        elif opcion == "3":
            trainee_view.edit_trainee_view()
        elif opcion == "4":
            trainee_view.delete_trainee_view()
        elif opcion == "5":
            trainee_view.search_by_name_view()
        elif opcion == "6":
            trainee_view.search_by_ficha_view()
        elif opcion == "7":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            trainee_template.display_message({"type": "error", "text": "Opción inválida. Por favor, selecciona un número entre 1 y 7."})

if __name__ == "__main__":
    main()