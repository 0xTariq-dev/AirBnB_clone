#!/usr/bin/python3
"""Model console: Defines HBNHCommand class."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


def parse(arg):
    # Splits the argument by characters defined in delim.
    delim = re.compile(r"[{}[\],\s]+")
    return re.split(delim, arg)


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand:
        The entry point of the command interperter.
    """
    prompt = '(hbnb) '
    __classes = {"BaseModel", "User", "State",
                 "City", "Place", "Review", "Amenity"}

    def do_create(self, arg):
        """Creates a new instance of BaseModel, save it to json file,
        and prints the id.
        """
        arg1 = parse(arg)
        if not arg:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id.
        """
        arg1 = parse(arg)
        if not arg:
            print("** class name missing **")
            return
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg1) < 2:
            print("** instance id missing **")
            return

        ob = arg1[0] + '.' + arg1[1]
        obj_dict = storage.all()

        if ob not in obj_dict:
            print("** no instance found **")
            return
        else:
            print(obj_dict[ob])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        arg1 = parse(arg)
        if not arg:
            print("** class name missing **")
            return
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg1) < 2:
            print("** instance id missing **")
            return

        ob = arg1[0] + '.' + arg1[1]
        obj_dict = storage.all()

        if ob not in obj_dict:
            print("** no instance found **")
            return
        else:
            if obj_dict[ob] is not None:
                del obj_dict[ob]
                storage.save()

    def do_update(self, arg):
        """
        Updates an instance based on the class name
            and id by adding or updating attribute.
        """
        arg1 = parse(arg)
        if not arg:
            print("** class name missing **")
            return
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(arg1) < 2:
            print("** instance id missing **")
            return

        ob = arg1[0] + '.' + arg1[1]
        obj_dict = storage.all()

        if ob not in obj_dict:
            print("** no instance found **")
            return
        elif len(arg1) < 3:
            print("** attribute name missing **")
        elif len(arg1) < 4:
            print("** value missing ** ")
        else:
            if arg1[2] not in ["id", "created_at", "updated_at"]:
                if obj_dict[ob] is not None:
                    setattr(obj_dict[ob], arg1[2], arg1[3])
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        arg1 = parse(arg)
        dict_values = storage.all().values()
        all_list = []
        if not arg:
            for value in dict_values:
                all_list.append(str(value))
            print(all_list)
        else:
            class_name = arg1[0]
            if class_name in str(dict_values):
                for value in dict_values:
                    if class_name == value.__class__.__name__:
                        all_list.append(str(value))
                if len(all_list) != 0:
                    print(all_list)
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """Skips any empty line and repeat prompt"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Captures CTRL+D interupt command"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
