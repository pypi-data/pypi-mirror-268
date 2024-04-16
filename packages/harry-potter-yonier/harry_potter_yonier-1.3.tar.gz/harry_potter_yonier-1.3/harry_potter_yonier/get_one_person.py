import requests

def get_one_person():
    """Obtiene un personaje de Harry Potter"""
    
    buscar_personaje = input("Ingrese el nombre del personaje que desea buscar: ")
    URL = "https://hp-api.onrender.com/api/characters"
    PERSONAJE = buscar_personaje.lower()  # Convertir a minúsculas para comparar
    
    r = requests.get(URL)
    if r.ok:
        respuesta = r.json()
        
        encontrado = False  # Bandera para indicar si se encontró al menos un personaje
        for r in respuesta:
            if PERSONAJE in r["name"].lower():
                print(f"Hola, soy {r['name']} y pertenezco a la casa {r['house']}.")
                encontrado = True  # Cambiar la bandera a True si se encuentra un personaje
        
        if not encontrado:
            print(f'El personaje "{buscar_personaje}" no existe')

if __name__ == "__main__":
    get_one_person()
