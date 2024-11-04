import os
import shutil

def menu():
    print("\n-- Administrador de Archivos--")
    print("1. Listar contenido de un directorio")
    print("2. Cambiar de directorio")
    print("3. Crear un nuevo directorio")
    print("4. Eliminar directorio")
    print("5. Copiar un archivo")
    print("6. Mover un archivo")
    print("7. Eliminar un archivo")
    print("8. Salir")
    return input("Selecciona una opcion: ")

def ls_dir():
    path = input("Ingresa el directorio: ")
    if os.path.isdir(path):
        print("Contenido:", os.listdir(path))
    else:
        print("Directorio no encontrado.")

def chg_dir():
    path = input("Ingresa el path del directorio al que deseas cambiar: ")
    if os.path.isdir(path):
        os.chdir(path)
        print("Directorio cambiado a: ", os.getcwd())
    else:
        print("Directorio no encontrado.")

def mk_dir():
    nombre = input("Ingresa el nombre del nuevo directorio: ")
    try:
        os.mkdir(nombre)
        print(f"Directorio '{nombre}' creado.")
    except FileExistsError:
        print("El directorio ya existe.")

def rm_dir():
    nombre = input("Ingresa el nombre del directorio a eliminar: ")
    try:
        shutil.rmtree(nombre)
        print(f"Directorio '{nombre}' eliminado.")
    except FileNotFoundError:
        print("Directorio no encontrado")

def cp_file():
    origen = input("Ingresa el path del archivo a copiar: ")
    destino = input("Ingresa el path del destino: ")
    try:
        shutil.copy(origen, destino)
        print(f"Archivo copiado a '{destino}'.")
    except FileNotFoundError:
        print("Archivo o directorio no encontrado.")

def mv_file():
    origen = input("Ingresa el path del archivo a mover: ")
    destino = input("Ingresa el path del destino: ")
    try:
        shutil.move(origen, destino)
        print(f"Archivo se movio a '{destino}'.")
    except FileNotFoundError:
        print("Archivo o directorio no encontrado.")

def rm_file():
    nombre = input("Ingresa el path del archivo a eliminar: ")
    try:
        os.remove(nombre)
        print(f"Archivo '{nombre}' eliminado.")
    except FileNotFoundError:
        print("Archivo no encontrado.")


while True:
    opcion = menu()
    if opcion == '1':
        ls_dir()
    elif opcion == '2':
        chg_dir()
    elif opcion == '3':
        mk_dir()
    elif opcion == '4':
        rm_dir()
    elif opcion == '5':
        cp_file()
    elif opcion == '6':
        mv_file()
    elif opcion == '7':
        rm_file()
    elif opcion == '8':
        print("Saliendo del administrador de archivos.")
        break
    else:
        print("Opcion no valida. Selecciona de nuevo.")
