import sqlite3

conn = sqlite3.connect('inventario_alimentos.db')

conn.execute('''CREATE TABLE IF NOT EXISTS ALIMENTOS_INV
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                PRODUCTO TEXT NOT NULL,
                MARCA TEXT NOT NULL,
                CATEGORIA TEXT NOT NULL,
                DESCRIPCION TEXT NOT NULL,
                PRECIO REAL NOT NULL,
                CANTIDAD INTEGER NOT NULL);''')


def registro(conn):
    finbucle = False
    while not finbucle:
        try:
            print('\n-/--------Registro de Alimento--------/')
            producto = input('Producto: ').lower()
            marca = input('Marca: ').lower()
            categoria = input('Categoría: ').lower()
            descripcion = input('Descripción: ').lower()
            revisar = conn.execute('SELECT * FROM ALIMENTOS_INV WHERE PRODUCTO = ? AND MARCA = ? AND CATEGORIA = ? AND DESCRIPCION = ?', (producto, marca, categoria, descripcion)).fetchall()
            if revisar:
                print('\nEste alimento ha sido registrado anteriormente\n')
                while True:
                    print('a. Intentar agregar otro alimento')
                    print('b. Salir al menú principal')
                    opc2 = input('Ingrese una opción: ').lower()
                    if opc2 == 'a':
                        break
                    elif opc2 == 'b':
                        finbucle = True
                        break
                    else:
                        print('\nOpción no válida. Intente de nuevo\n')
            else:
                precio = float(input('Precio: '))
                cantidad = int(input('Cantidad en stock: '))
                conn.execute('INSERT INTO ALIMENTOS_INV (PRODUCTO, MARCA, CATEGORIA, DESCRIPCION, PRECIO, CANTIDAD) VALUES (?, ?, ?, ?, ?, ?)', (producto, marca, categoria, descripcion, precio, cantidad))
                conn.commit()
                print('\n¡Nuevo alimento agregado correctamente!\n')
                break
        except Exception as e:
            print(e)


def buscar(conn):
    finbucle = False
    while not finbucle:
        try:
            print('\n/--------------Buscar Alimento----------/')
            producto = input('Producto: ').lower()
            revisar = conn.execute('SELECT * FROM ALIMENTOS_INV WHERE PRODUCTO = ?', (producto,)).fetchall()
            if revisar:
                print('\nAlimentos encontrados:')
                for fila in revisar:
                    print(f'\tID: {fila[0]}; Producto: {fila[1]}; Marca: {fila[2]}; Categoría: {fila[3]}; Descripción: {fila[4]}; Precio: {fila[5]}; Cantidad: {fila[6]}')
                break
            else:
                print('\nNo hay alimentos de ese producto')
                while True:
                    print('\na. Intentar buscar otro producto')
                    print('b. Salir al menú principal')
                    opc2 = input('Ingrese una opción: ').lower()
                    if opc2 == 'a':
                        break
                    elif opc2 == 'b':
                        finbucle = True
                        break
                    else:
                        print('\nOpción no válida. Intente de nuevo\n')
        except Exception as e:
            print(e)


def editar(conn):
    finbucle = False
    while not finbucle:
        try:
            print('\n/----------------Editar Alimento---------------/')
            id = input('\nID: ')
            revisar = conn.execute('SELECT * FROM ALIMENTOS_INV WHERE ID = ?', (id,)).fetchone()
            if revisar is None:
                print('\nEste alimento no existe')
                while True:
                    print('\na. Intentar editar otro alimento')
                    print('b. Salir al menú principal')
                    opc2 = input('Ingrese una opción: ').lower()
                    if opc2 == 'a':
                        break
                    elif opc2 == 'b':
                        finbucle = True
                        break
                    else:
                        print('\nOpción no válida. Intente de nuevo\n')
            else:
                print('\nIngrese los nuevos datos del alimento')
                newproducto = input('Producto: ').lower()
                newmarca = input('Marca: ').lower()
                newcategoria = input('Categoría: ').lower()
                newdescripcion = input('Descripción: ').lower()
                newprecio = float(input('Precio: '))
                newcant = int(input('Cantidad: '))
                conn.execute('UPDATE ALIMENTOS_INV SET PRODUCTO = ?, MARCA = ?, CATEGORIA = ?, DESCRIPCION = ?, PRECIO = ?, CANTIDAD = ? WHERE ID = ?', (newproducto, newmarca, newcategoria, newdescripcion, newprecio, newcant, id))
                conn.commit()
                print('\n¡Alimento editado correctamente!\n')
                break
        except Exception as e:
            print(e)


def eliminar(conn):
    finbucle = False
    while not finbucle:
        try:
            print('\n/-------------Eliminar Alimento-----------/')
            id = input('\nID: ')
            revisar = conn.execute('SELECT * FROM ALIMENTOS_INV WHERE ID = ?', (id,)).fetchone()
            if revisar is None:
                print('\nEste alimento no existe')
                while True:
                    print('\na. Intentar eliminar otro alimento')
                    print('b. Salir al menú principal')
                    opc2 = input('Ingrese una opción: ').lower()
                    if opc2 == 'a':
                        break
                    elif opc2 == 'b':
                        finbucle = True
                        break
                    else:
                        print('\nOpción no válida. Intente de nuevo\n')
            else:
                conn.execute('DELETE FROM ALIMENTOS_INV WHERE ID = ?', (id,))
                conn.commit()
                print('\n¡Alimento eliminado correctamente!\n')
                break
        except Exception as e:
            print(e)


while True:
    print("\n\n/-----------------SISTEMA DE INVENTARIO DE ALIMENTOS--------------/")
    print("1. Registrar alimento.")
    print("2. Buscar alimento.")
    print("3. Editar alimento.")
    print("4. Eliminar alimento.")
    print("5. Salir.")
    try:
        op = int(input("Escoga una opcion: "))
    except :
        print(f"Algo salió mal, elegiste algo que no existe del menú")
        op = 999

    if op == 1:
        registro(conn)
    if op == 2:
        buscar(conn)
    if op == 3:
        editar(conn)
    if op == 4:
        eliminar(conn)
    if op == 5:
        print('\nSaliendo del inventario')
        break
        conn.close()
