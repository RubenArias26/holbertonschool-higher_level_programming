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
        Este método retorna el área de un cuadrado.

        Returns:
            _size ** 2 (el tamaño al cuadrado)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Este método imprime un cuadrado en stdout usando #,
        siempre y cuando __size > 0.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("{0}".format('#' * self.__size))

    @property
    def size(self):
        """Esta propiedad devuelve el __size

            Returns:
                retorna el __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Esta función configura el valor de __size
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
