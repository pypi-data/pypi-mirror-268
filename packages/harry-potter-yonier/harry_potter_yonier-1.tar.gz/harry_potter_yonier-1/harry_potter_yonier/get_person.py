import requests

def obtener_personajes(URL):
    """Obtiene todos los personajes de Harry Potter
    >>> type(obtener_personajes(URL="https://hp-api.onrender.com/api/characters"))
    """
    r = requests.get(URL)
    if r.ok:
        respuesta = r.json()
        for personaje in respuesta:
            mensaje = f'Hola, soy "{personaje["name"]}" y pertenezco a la casa "{personaje["house"]}".'
            print(mensaje)

if __name__ == "__main__":
    obtener_personajes(URL="https://hp-api.onrender.com/api/characters")
