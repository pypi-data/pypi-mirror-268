import logging
from harry_potter_yonier import get_one_person, get_person

if __name__ == "__main__":
    while True:
        # Mostrar las opciones disponibles
        print("1. Buscar personaje")
        print("2. Listar personajes")
        print("3. Salir")
        
        # Capturar la elección del usuario
        choose = input("Ingrese el número de la opción que desea: ")
        
        if choose == "1":
            buscar_personaje = input("Ingrese el nombre del personaje que desea buscar: ")
            final_get_one = get_one_person.obtener_personajes(URL="https://hp-api.onrender.com/api/characters", PERSONAJE=buscar_personaje)
            print(final_get_one)
            break  # Salir del bucle while
        elif choose == "2":
            get_person.obtener_personajes(URL="https://hp-api.onrender.com/api/characters")
            break  # Salir del bucle while
        elif choose == "3":
            logging.warning("Saliendo del programa...")
            break  # Salir del bucle while
        else:
            logging.warning("Opción inválida. Por favor, elija una opción válida.")
