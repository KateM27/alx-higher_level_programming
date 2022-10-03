#!/usr/bin/python3
"""
This class inherits from the Base
Private instance attributes will be used
with getters and setters
"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class with some inherited attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """prints stdout of the rectangle instance with '#'"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for a in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding the __str__ method"""
        return [Rectangle]({}), {}/{} - {}/{}.format(self.id,
                                                     self.__x,
                                                     self.__y,
                                                     self.__width,
                                                     self.__height)

    def update(self, *args, **kwargs):
        """args assigns an argument to each attribute"""
        """kwargs assigns a key-worded argument to attributes"""
        if len(args):
            for idx, attr in enumerate(args):
                if idx == 0:
                    self.id = attr
                elif idx == 1:
                    self.width = attr
                elif idx == 2:
                    self.height = attr
                elif idx == 3:
                    self.x = attr
                elif idx == 4:
                    self.y = attr
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a rectangle"""
        dct = {}
        dct["id"] = self.id
        dct["width"] = self.width
        dct["height"] = self.height
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
