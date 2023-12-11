from pymongo import MongoClient

uri = "mongodb+srv://Ad22:Anthony3-751779@cluster0.2r60lxz.mongodb.net/"
cliente = MongoClient(uri)
db = cliente["diccionario_slangs"]
coleccion = db["palabras_guardadas"]


def agregar_palabra(coleccion):
    print("\nAgregar palabra\n")
    while True:
        try:
            palabra = input("Ingrese la nueva palabra: ").lower()
            revisar = coleccion.find_one({"palabra": palabra})
            if revisar:
                print("\nPalabra existente, intente con otra.")
            else:
                significado = input("Ingrese el significado de la palabra: ")
                nueva_palabra = {
                    "palabra": palabra,
                    "significado": significado,
                }
                coleccion.insert_one(nueva_palabra)
                print("\nPalabra agregada exitosamente.")
            break
        except Exception as e:
            print(f"\nError al agregar: {e}. Intente de nuevo.")


def editar_palabra(coleccion):
    print("\nEditar palabra\n")
    while True:
        try:
            palabra = input("Ingrese la palabra: ").lower()
            revisar = coleccion.find_one({"palabra": palabra})
            if revisar:
                nuevo_significado = input("Ingrese el nuevo significado: ")
                coleccion.update_one({"palabra": palabra}, {"$set": {"significado": nuevo_significado}})
                print("\nPalabra actualizada exitosamente.")
                break
            else:
                print("\nPalabra no existente, intente con otra")
        except Exception as e:
            print(f"\nError al editar: {e}. Intente de nuevo.")


def eliminar_palabra(coleccion):
    print("\nEliminar palabra")
    while True:
        try:
            palabra = input("\nIngrese palabra: ").lower()
            revisar = coleccion.find_one({"palabra": palabra})
            if revisar:
                coleccion.delete_one({"palabra": palabra})
                print("\nPalabra eliminada exitosamente")
                break
            else:
                print("\nPalabra no existente, intente con otra")
        except Exception as e:
            print(f"\nError al eliminar: {e}. Intente de nuevo.")


def listar_palabras(coleccion):
    print("\nLista de palabras\n")
    try:
        palabras = coleccion.find({}, {"_id": 0, "palabra": 1})
        count = 0

        for palabra in palabras:
            count += 1
            print(palabra["palabra"])

        if count == 0:
            print("\nEl diccionario está vacío.")
    except Exception as e:
        print(f"\nError al mostrar palabras: {e}.")


def buscar_significado(coleccion):
    print("\nBuscar significado")
    while True:
        try:
            palabra = input("\nIngrese palabra a buscar: ").lower()
            revisar = coleccion.find_one({"palabra": palabra})
            if revisar:
                print(f"'{palabra}': {revisar['significado']}")
                break
            else:
                print("\nPalabra no existente, intente con otra")
        except Exception as e:
            print(f"\nError al buscar: {e}. Intente de nuevo.")


while True:
    print("\n\n/-------------Diccionario de Slangs------------------/")
    print("1. Ingresa una palabra nueva.")
    print("2. Editar palabra.")
    print("3. Eliminar palabra.")
    print("4. Palabras guardadas.")
    print("5. Buscar palabra y su significado.")
    print("6. Salir.")
    try:
        op = int(input("Qué opción? "))
    except Exception as e:
        print(f"Algo salió mal, elegiste algo que no existe del menú: {e}")
        op = 999

    if op == 1:
        agregar_palabra(coleccion)
    if op == 2:
        editar_palabra(coleccion)
    if op == 3:
        eliminar_palabra(coleccion)
    if op == 4:
        listar_palabras(coleccion)
    if op == 5:
        buscar_significado(coleccion)
    if op == 6:
        print("Saliendo")
        cliente.close()
        break
