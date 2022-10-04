#!/usr/bin/python3
"""class Square which inherits from Rectangle
a square is a rectangle with same width and height"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """init of attributes inherited from class Rectangle"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """overloading the string method"""
        return [Square]({}), {}/{} - {}.format(self.id, self.x,
                                               self.y, self.width)

    @property
    def size(self):
        """getter of size"""
        return self.size

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """args assigns an argument to each attribute"""
        """kwargs assigns a key-worded argument to attributes"""
        if len(args):
            for idx, attr in enumerate(args):
                if idx == 0:
                    self.id = attr
                if idx == 1:
                    self.size = attr
                if idx == 2:
                    self.x = attr
                if idx == 3:
                    self.y = attr
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of a square"""
        dct = {}
        dct["id"] = self.id
        dct["size"] = self.size
        dct["x"] = self.x
        dct["y"] = self.y
        return dct
