#!/usr/bin/python3
"""
Este modulo define una función para escribir
sobre un archivo
"""


def write_file(filename="", text=""):
    """
    Esta función sobreescribe una archivo,
    si no existe lo crea.

    Args:
        filename (string): Ruta del archivo.
        text (string): Texto a escribir.
    Returns:
        int: número de bytes escritos.
    """
    with open(filename, "w") as f:
        f.write(text)
        return f.tell()