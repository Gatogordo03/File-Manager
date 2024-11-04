# Administrador de Archivos en Python

Este proyecto es un administrador de archivos de terminal en Python, que utiliza las librerías `os` y `shutil` para realizar operaciones básicas de archivos y directorios. Permite listar, crear, mover, copiar y eliminar archivos y carpetas de manera interactiva con la terminal.

## Características

1. Listar el contenido de un directorio.
2. Cambiar de directorio.
3. Crear un nuevo directorio.
4. Eliminar un directorio.
5. Copiar un archivo.
6. Mover un archivo.
7. Eliminar un archivo.

## Dependencias

Este proyecto utiliza solo librerías estándar de Python:

```python
import os
import shutil
```

## Como usar

1. Ejecuta el script en tu terminal con:

```python
python AdministradorArchivos.py
```

2. Selecciona una opción ingresando el numero correspondiente
3. Sigue las instrucciónes para cada opción seleccionada

## Descripción de Funciones

- `menu()`: Muestra las opciones del menú principal.
- `ls_dir()`: Lista el contenido de un directorio especificado por el usuario.
- `chg_dir()`: Cambia el directorio actual a uno especificado por el usuario.
- `mk_dir()`: Crea un nuevo directorio con el nombre especificado.
- `rm_dir()`: Elimina un directorio y su contenido.
- `cp_file()`: Copia un archivo a la ubicación de destino.
- `mv_file()`: Mueve un archivo a la ubicación de destino.
- `rm_file()`: Elimina un archivo específico.

## Notas

Esta herramienta es realizada de un manera muy básica con fines de aprendizaje y no accede a todos los archivos y directorios por falta de permisos para su ejecución.
