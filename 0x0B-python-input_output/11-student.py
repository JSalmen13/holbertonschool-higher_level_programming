#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves student dict"""
        if type(attrs) is list:
            my_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    my_dict[i] = self.__dict__[i]
            return(my_dict)
        return(self.__dict__)

    def reload_from_json(self, json):
        """replaces student attributes"""
        self.__dict__ = dict(json)
        return(self.__dict__)
