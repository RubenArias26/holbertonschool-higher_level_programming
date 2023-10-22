#!/usr/bin/python3
"""Este módulo define la clase Rectangle."""


class Rectangle:
    """Esta clase expone un Rectangle."""

    def __init__(self, width=0, height=0):
        """Método constructor, tiene 2 parámetros opcionales.

        Args:
            width (int): El ancho del Rectangle.
            height (int): El alto del Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Este método retorna el ancho de nuestro Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Este propiedad configura el ancho"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Este método retorna el alto de  nuestro Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Esta propiedad configura el alto"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value