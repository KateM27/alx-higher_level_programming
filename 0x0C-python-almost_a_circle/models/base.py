#!/usr/bin/python3
"""
This class will be the base of all other classes
with the goal of managing id attr in all future classes
and avoid duplicating the same code
"""


import json
import csv
import turtle


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation of list_objs to a file"""
        file = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for i in list_objs:
                file.append(cls.to_dictionary(i))
        with open(file_name, mode="w") as my_file:
            my_file.write(cls.to_json_string(file))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string rep"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes already set"""
        if cls.__name__ is "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ is "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, mode="r") as my_file:
                file = cls.from_json_string(my_file.read())
            for i, j in enumerate(file):
                file[i] = cls.create(**file[i])
        except:
            pass
        return file

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in csv"""
        file_name = cls.__name__ + ".csv"
        with open(file_name,  mode="w", newline="") as my_csv:
            csv_writer = csv.writer(my_csv)
            if cls.__name__ is "Rectangle":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.width, obj.height,
                                        obj.x, obj.y])
            elif cls.__name__ is "Square":
                for obj in list_objs:
                    csv_writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in csv"""
        file_name = cls.__name__ + ".csv"
        file = []
        try:
            with open(file_name, mode="r") as my_csv:
                csv_reader = csv.reader(my_csv)
                for arg in csv_reader:
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(arg[0]),
                                      "width": int(arg[1]),
                                      "height": int(arg[2]),
                                      "x": int(arg[3]),
                                      "y": int(arg[4])}
                    elif cls.__name__ is "Square":
                        dictionary = {"id": int(arg[0]),
                                      "size": int(arg[1]),
                                      "x": int(arg[2]),
                                      "y": int(arg[3])}
                    obj = cls.create(**dictionary)
                    file.append(obj)
        except:
            pass
        return file
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the squares and rectangles"""

        turtle.penup()
        turtle.pensize(10)
        turtle.bgcolor("black")
        turtle.color("teal")
        turtle.hideturtle()
        turtle.goto(-300, 300)
        turtle.speed(0)

        for instance in list_rectangles:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 200
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 300)

        turtle.goto(-300, 100)
        for instance in list_squares:
            turtle.pendown()
            for i in range(2):
                turtle.forward(instance.width)
                turtle.right(90)
                turtle.forward(instance.height)
                turtle.right(90)
            turtle.penup()
            if instance.width < 100:
                move_by = 100
            else:
                move_by = instance.width + 30
            x_cordinate = round(turtle.xcor(), 5)
            turtle.goto(x_cordinate + move_by, 100)

        turtle.exitonclick()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
            this is my method
        '''
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode="w", newline='', encoding="UTF8") as fd:
            write_this = csv.writer(fd, delimiter=" ")

            if cls.__name__ == "Rectangle":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["width"]) + "," +
                               str(item["height"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)

            if cls.__name__ == "Square":
                for item in list_objs:
                    string = ""
                    item = item.to_dictionary()
                    string += (str(item["id"]) + "," +
                               str(item["size"]) + "," +
                               str(item["x"]) + "," + str(item["y"]))
                    write_this.writerow(string)
    
    @classmethod
    def load_from_file_csv(cls):
        '''
            this is my method
        '''
        return ([])
