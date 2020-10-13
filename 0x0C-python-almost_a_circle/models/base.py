#!/usr/bin/python3
"""
This module defines a Base class
"""
import json
import csv


class Base:
    """
    Defines a Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_ = []
        if list_objs is not None:
            for obj in list_objs:
                list_.append(obj.to_dictionary())
        with open(filename, mode="w") as f:
            f.write(Base.to_json_string(list_))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        filename = cls.__name__ + ".json"
        list_ = []
        try:
            with open(filename) as file_:
                jlist_ = Base.from_json_string(file_.read())
                for obj in jlist_:
                    list_.append(cls.create(**obj))
        except Exception:
            pass
        return list_

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to a csv file
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w") as file_:
            writer_ = csv.writer(file_, delimiter=",")
            if cls.__name__ is "Rectangle":
                keys = ["id", "width", "height", "x", "y"]
            elif cls.__name__ is "Square":
                keys = ["id", "size", "x", "y"]
            for obj in list_objs:
                writer_.writerow([getattr(obj, key) for key in keys])

    @classmethod
    def load_from_file_csv(cls):
        """
        read from csv
        """
        filename = cls.__name__ + ".csv"
        list_ = []
        with open(filename) as file_:
            reader_ = csv.reader(file_)
            if cls.__name__ is "Rectangle":
                keys = ["id", "width", "height", "x", "y"]
            elif cls.__name__ is "Square":
                keys = ["id", "size", "x", "y"]
            for row in reader_:
                values = [int(row[i]) for i in range(len(row))]
                obj = dict(zip(keys, values))
                list_.append(cls.create(**obj))
            return list_
