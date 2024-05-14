#!/usr/bin/python3
"""Storage class Module"""


import os
import json
# from models import base_model

class FileStorage:
    """File Storage class for the project"""
    __file_path = "file.json"
    __objects = {}

         
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
        
    def save(self):
        """serializes"""
        with open(self.__file_path, "w") as file:
              _obj = {key: val.to_dict() for key, val in self.__objects.items()}
              json.dump(_obj, file)
    
    def reload(self):
        """Deserialises"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as f:
                json_dict = json.load(f)
                for obj in json_dict.values():
                    class_n = obj['__class__']
                    module_n = self.class_dict[class_n]
                    del obj['__class__']
                    self.new(eval(f'{module_n}.{class_n}')(**obj))
    