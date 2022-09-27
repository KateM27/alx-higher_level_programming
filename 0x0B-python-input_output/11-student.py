#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        n_dict = {}
        for i in n_dict:
            try:
                n_dict[i] = self.__dict__[i]
            except:
                pass
        return n_dict

    def reload_from_json(self, json):
        for k in json:
            try:
                attr(self, k, json[k])
            except:
                pass
