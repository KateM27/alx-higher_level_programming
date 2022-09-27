#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        c_dict = self.__dict__
        n_dict = dict()

        if type(attrs) is list:
            for a in attrs:
                if type(a) is not str:
                    return c_dict

                if a in c_dict:
                    n_dict[a] = c_dict[a]
                return n_dict
            return c_dict

    def reload_from_json(self, json):
        for d in json:
            if d in self.__dict__.keys():
                self.__dict__[d] = json[d]
