import sqlite3
import time

conn = sqlite3.connect('Diccionario Panameño')

conn.execute('''CREATE TABLE IF NOT EXISTS DICCIONARIO
                (PALABRA TEXT PRIMARY KEY,
                SIGNIFICADO TEXT NOT NULL);''')

while True:
    print("\n\n/-------------Diccionario de Slangs------------------/")  # Menu principal
    print("1. Ingresa una palabra nueva.")
    print("2. Editar palabra.")
    print("3. Eliminar palabra.")
    print("4. Palabras guardadas.")
    print("5. Buscar palabra y su significado.")
    print("6. Salir.")
    try:
        op = int(input("Qué opción? ")) # Elige una opción
    except:
        print("Algo salio mal, elegiste algo que no existe del menu.\n")  # Error
        op = 999
        time.sleep(3)

    if op == 1:
        print("Agrega una nueva palabra en el diccionario.") # Agregar nueva palabra
        time.sleep(1)
        control = True
        while control:
            try:
                palabra = input("\nQué palabra quieres agregar? ")
                busca = conn.execute("SELECT PALABRA FROM DICCIONARIO WHERE PALABRA = ?", (palabra,))
                row = busca.fetchone()
                if not row:
                    significado = input("Qué significa eso? ") # Significado de la palabra
                    conn.execute('INSERT INTO DICCIONARIO(palabra, significado) VALUES(?, ?)', (palabra, significado))
                    print("\nPalabra agregada con éxito")
                    time.sleep(1)
                    print("\nRegresando al menú")
                    conn.commit()
                    time.sleep(1)
                    control = False
                else:
                    print("\nYa existe esa palabra, intenta con otra")
                    time.sleep(2)
            except:
                print("\nError añadiendo palabra. Volviendo al menú...") # Error al agregar
                time.sleep(2)
                control = False
    # OPCIÓN EDITAR PALABRA
    if op == 2:
        busca = conn.execute('SELECT * FROM DICCIONARIO')
        registro = busca.fetchall()
        if registro:
            print("\nVamos a cambiar algo que ya está...") # Editar palabra existente
            time.sleep(1)
            control = True
            while control:
                try:
                    edit_palabra = input("\nCuál palabra quieres cambiar? ") # Palabra a editar
                    busca = conn.execute('SELECT * FROM DICCIONARIO WHERE PALABRA = ?', (edit_palabra,))
                    row = busca.fetchone()
                    if row:
                        nuevo_sig = input("Qué será ahora eso? ") # Nuevo significado
                        conn.execute('UPDATE DICCIONARIO SET SIGNIFICADO = ? WHERE PALABRA = ?', (nuevo_sig, edit_palabra))
                        print("\n¡Palabra editada")
                        time.sleep(1)
                        print("\nRegresando al menú")
                        conn.commit()
                        time.sleep(1)
                        control = False
                    else:
                        print("\nLa palabra no existe, intenta otra vez.")
                        time.sleep(2)
                except:
                    print("\nError buscando. Volviendo al menú...")
                    time.sleep(2)
                    control = False
        else:
            print("\nDiccionario vacío. Necesitas agragar una palabra.")
            time.sleep(3)
    # OPCION ELIMINAR PALABRA
    if op == 3:
        busca = conn.execute('SELECT * FROM DICCIONARIO')
        registro = busca.fetchall()
        if registro:
            print("\nEliminando una palabra...")
            time.sleep(1)
            control = True
            while control:
                try:
                    palabra = input("\nCuál palabra quieres eliminar? ")
                    busca = conn.execute('SELECT * FROM DICCIONARIO WHERE PALABRA = ?', (palabra,))
                    row = busca.fetchone()
                    if row:
                        conn.execute('DELETE FROM DICCIONARIO WHERE PALABRA = ?', (palabra,))
                        print("\nPalabra eliminada con éxito")
                        time.sleep(1)
                        print("\nRegresando al menú")
                        conn.commit()
                        time.sleep(1)
                        control = False
                    else:
                        print("\nEsa palabra no existe, intenta de nuevo.")
                        time.sleep(2)
                except:
                    print("\nError borrando. Volviendo al menú...")
                    time.sleep(2)
                    control = False
        else:
            print("\nDiccionario vacío. Necesitas agragar una palabra.")
            time.sleep(3)
    # OPCIÓN PALABRAS GUARDADAS
    if op == 4:
        busca = conn.execute('SELECT * FROM DICCIONARIO')
        registro = busca.fetchall()
        if registro:
            print("\nVamos a ver qué palabras están aquí...") # Ver palabras del diccionario
            time.sleep(1)
            palabras = conn.execute('SELECT * FROM DICCIONARIO ORDER BY PALABRA')
            for diccionario in palabras:
                print(str(diccionario[0]) + ". ") # Imprimir palabras
            print(input("\nPulsa enter para seguir -> "))
        else:
            print("\nDiccionario vacío. Necesitas agragar una palabra.")
            time.sleep(3)
    # OPCIÓN BUSCAR SIGNIFICADO
    if op == 5:
        busca = conn.execute('SELECT * FROM DICCIONARIO')
        registro = busca.fetchall()
        if registro:
            print("\nVamos a encontrar qué significa una palabra...")
            time.sleep(1)
            control = True
            while control:
                try:
                    palabra = input("\nQué palabra quieres buscar? ") # Palabra a buscar
                    busca = conn.execute('SELECT SIGNIFICADO FROM DICCIONARIO WHERE PALABRA = ?', (palabra,))
                    row = busca.fetchone()
                    if row:
                        print(palabra + ": " + row[0]) # Significado de la palabra
                        control = False
                        print(input("\nPulsa enter para seguir -> "))
                    else:
                        print("\nLa palabra no está, intenta otra vez.")
                        time.sleep(2)
                except:
                    print("\nError buscando. Regresando al menú...")
                    time.sleep(2)
                    control = False
        else:
            print("\nDiccionario vacío. Necesitas agragar una palabra.")
            time.sleep(3)
    # OPCIÓN SALIR
    if op == 6:
        conn.close
        print("\n¡Saliendo!")
        time.sleep(1)
        exit()
