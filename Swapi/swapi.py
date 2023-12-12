import requests

def clima():
    swapi = requests.get("https://swapi.dev/api/planets/")
    datos = swapi.json()
    planetario = [planeta for planeta in datos["results"] if "arid" in planeta["climate"]]
    cantidad = len(planetario)
    print(f"\nCantidad de peliculas en el que aparecen planetas de clima árido: {cantidad}.")


def wookiee():
    swapi = requests.get("https://swapi.dev/api/films/3/")
    datos = swapi.json()
    wookiees = [person for person in datos["characters"] if "Wookiee" in person]
    cantidad = len(wookiees)
    print(f"\nCantidad de wookies que aparecen en la sexta pelicula: {cantidad}.")


def naves():
    swapi = requests.get("https://swapi.dev/api/starships/")
    datos = swapi.json()
    tamano = max(datos["results"], key=lambda x: int(x["length"]) if x["length"].isnumeric() else 0)
    nave = tamano["name"]
    print(f"\nAeronave más grande de la saga: {nave}")


while True:
    print("\n\nPreguntas")
    print("a) ¿En cuántas películas aparecen planetas cuyo clima sea árido?")
    print("b) ¿Cuántos Wookies aparecen en la sexta película?")
    print("c) ¿Cuál es el nombre de la aeronave más grande en toda la saga?")
    print("d) Salir del menu")
    try:
        op = input("Escoga una opcion: ").lower()
    except Exception as e:
        print(f"Algo salió mal, elegiste algo que no existe del menú: {e}")
    if op == 'a':
        clima()
    elif op == 'b':
        wookiee()
    elif op == 'c':
        naves()
    elif op == 'd':
        print("Saliendo")
        break
