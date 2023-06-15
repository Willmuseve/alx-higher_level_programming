#!/usr/bin/python3
""" a class Student that defines a student """


class Student:
    """ a class Student that defines a student by:
        public instance attributes; first_name,
        last_name, age"""
    def __init__(self, first_name, last_name, age):
        """ Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method that retrieves a dictionary representation
        of a student instance"""
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ public method  that replaces all attributes of the
        Student instance """
        for i in json:
            self.__dict__.update({i: json[i]})
