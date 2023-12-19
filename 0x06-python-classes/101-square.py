#!/usr/bin/python3

""" Defines a class square"""

class Square:
    """ Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initiate a new square
        
        Arge:
            size (int): The size of the new Square
            position (int, int): The position of the new sqaure.
       """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
            return
        
        [print("") for _ in range(0, self.position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for j in range(0,self.position[1])]
            [print(" ", end="") for k in range(0,self.__size)]
            print("")
            
    def __str__(self):
        if self.__size !=0:
            [print(" ") for i in range(0,self.position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for j in range(0,self.position[1])]
            [print(" ", end="") for k in range(0,self.__size)]
            if i !=self.__size -1:
                print("")
        return ("")
