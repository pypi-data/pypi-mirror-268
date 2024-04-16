import requests

def get_one_person():
    """Obtiene un personaje de Harry Potter"""
    
    buscar_personaje = input("Ingrese el nombre del personaje que desea buscar: ")
    URL="https://hp-api.onrender.com/api/characters"
    PERSONAJE=buscar_personaje
    
    r = requests.get(URL, PERSONAJE)
    if r.ok:
        respuesta = r.json()       
        for r in respuesta:
            if PERSONAJE.lower() in r["name"].lower():
                # print(f"Hola, soy {r['name']} y pertenezco a la casa {r['house']}.")
                print(f"Hola, soy {r['name']} y pertenezco a la casa {r['house']}.")

if __name__ == "__main__":
    get_one_person()
    