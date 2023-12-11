#!/usr/bin/python3
# base.py
import json

"""Represents the base of all other classes in this project"""


class Base:
    __nb__objects = 0

    def __init__(self, id=None):
        """Initializes a new Base

        Args:
            id (_int_):The identity of the new Base.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (_string_): _a list of dictionaries_
        """
        
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """a function that writes the JSON string representation of list_objs to a file

        Args:
            list_objs : _list of objects_
        """
        
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
    
    @staticmethod          
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_json_): _a JSON string representing a list of dictionaries_
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """returns an instance when all attributes are set
        """
        
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1,1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
        
    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []        