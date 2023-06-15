#!/usr/bin/python3
""" a class Student that defines a student """


class Student:
    """ defines student by:
        public instance attributes
        instantiation first name, last name age"""
    def __init__(self, first_name, last_name, age):
        """ Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Punlic method that retrieves a dictionary"""
        return self.__dict__
