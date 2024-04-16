import requests

def get_person():
    """Obtiene todos los personajes de Harry Potter
    >>> type(get_person(URL="https://hp-api.onrender.com/api/characters"))
    """
    
    URL="https://hp-api.onrender.com/api/characters"
    r = requests.get(URL)
    if r.ok:
        respuesta = r.json()
        for personaje in respuesta:
            mensaje = f'Hola, soy "{personaje["name"]}" y pertenezco a la casa "{personaje["house"]}".'
            print(mensaje)

if __name__ == "__main__":
    get_person()
