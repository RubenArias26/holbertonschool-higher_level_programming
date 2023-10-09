#!/usr/bin/python3
"""
Este módulo representa la clase Square
"""


class Square:
    """
    Esta clase define un cuadrado
    """

    def __init__(self, size=0):
        """
        Este es el constructor de la clase Square.
        Inicializa un nuevo objeto Square con el size recibido.

        Args:
            size (int o float): La longitud de los lados del square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Este método retorna el area de un cuadrado.

        Returns:
            __size ** 2 (el cuadrado de __size)
        """
        return self.__size ** 2
