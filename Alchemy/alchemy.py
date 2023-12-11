from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine("mariadb+mariadbconnector://root:acdm2212@localhost:3306/diccionario_panameno")


class Diccionario(Base):
    __tablename__ = "Tabla"
    palabra = Column(String(length=15), primary_key=True)
    significado = Column(String(length=25))

    def __init__(self, palabra, significado):
        self.palabra = palabra
        self.significado = significado


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def existe_palabra(buscar, Diccionario):
    buscar = session.query(Diccionario).filter_by(palabra=buscar).first()
    return buscar


def agregar_palabra(Diccionario):
    print("Agrega una nueva palabra en el diccionario.")  # Agregar nueva palabra
    continuar = True
    while continuar:
        palabra = input("\nEscribir nueva palabra: ")
        buscar = existe_palabra(palabra, Diccionario)
        if buscar:
            print("\nLa palabra ya existe")
        else:
            significado = input("\nEscribir significado: ")
            registro = Diccionario(palabra=palabra, significado=significado)
            session.add(registro)
            session.commit()
            print("\n¡Palabra agregada con éxito!")
            continuar = False


def editar_palabra(Diccionario):
    print("\nVamos a cambiar algo que ya está...")  # Editar palabra existente
    continuar = True
    while continuar:
        palabra = input("\nEscribe la palabra a editar: ").lower()
        buscar = existe_palabra(palabra, Diccionario)
        if not buscar:
            print("\nLa palabra no existe")
        else:
            nueva_palabra = input("\nEscribe el nuevo significado: ")
            palabra_editar = session.query(Diccionario).filter_by(palabra=palabra).first()
            palabra_editar.significado = nueva_palabra
            session.commit()
            print("\nPalabra editada con éxito")
            continuar = False


def eliminar_palabra(Diccionario):
    print("\n¡Eliminar una palabra!")
    palabra = input("\nEscribe la palabra a eliminar: ").lower()
    buscar = existe_palabra(palabra, Diccionario)
    if not buscar:
        print("\nLa palabra no existe")
    else:
        confirmacion = input(f"\n¿Estás seguro de que deseas eliminar la palabra '{palabra}'? (Sí/No): ").lower()
        if confirmacion == "si" or confirmacion == "s":
            session.delete(buscar)
            session.commit()
            print("\nPalabra eliminada con éxito")
        else:
            print("\nOperación de eliminación cancelada")


def listar_palabras(Diccionario):
    print("\n¡Listado de palabras!")
    palabras = session.query(Diccionario.palabra).all()
    if not palabras:
        print("Diccionario vacío, intenta añadir una palabra primero")
    else:
        for palabra in palabras:
            print(palabra[0])


def significado_palabra(Diccionario):
    print("\nVamos a encontrar qué significa una palabra...")
    continuar = True
    while continuar:
        palabra = input("\nEscriba la palabra para buscar su significado: ")
        buscar = palabra.lower()
        registro = session.query(Diccionario).filter_by(palabra=buscar).first()
        if registro:
            print(f"\n{palabra}: {registro.significado}")
            continuar = False
        else:
            print(f"\nNo se encontró el significado de {palabra}.")


def mostrar_menu():
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
        except:
            print("Algo salió mal, elegiste algo que no existe del menú.\n")  # Error
            op = 999

        if op == 1:
            agregar_palabra(Diccionario)
        elif op == 2:
            editar_palabra(Diccionario)
        elif op == 3:
            eliminar_palabra(Diccionario)
        elif op == 4:
            listar_palabras(Diccionario)
        elif op == 5:
            significado_palabra(Diccionario)
        elif op == 6:
            print("¡Saliendo!")
            session.close()
            exit()


if __name__ == "__main__":
    mostrar_menu()
