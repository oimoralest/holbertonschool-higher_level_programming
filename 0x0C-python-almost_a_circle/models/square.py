#!/usr/bin/python3
"""
This module defines a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines a Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size
        )

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update a Square
        """
        keys = ['id', 'size', 'x', 'y']
        if kwargs and len(args) == 0:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)
        elif args is not None:
            for key, value in zip(keys, args):
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dict representation of Square
        """
        keys = ['id', 'size', 'x', 'y']
        dict_ = {}
        for key in keys:
            dict_[key] = getattr(self, key)
        return dict_
