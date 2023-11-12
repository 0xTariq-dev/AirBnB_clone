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

    def cls_check(self, class_name):
        """Class name validator"""
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel, save it to json file,
        and prints the id.
        """
        arg1 = parse(arg)
        if not arg:
            print("** class name missing **")
        elif not self.cls_check(arg1[0]):
            return
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
        elif not self.cls_check(arg1[0]):
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
        elif not self.cls_check(arg1[0]):
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
        """Updates an instance based on the class name and id."""
        arg1 = []
        quote = False
        curr = ""

        for c in arg:
            if c == ' ' and not quote:
                arg1.append(curr)
                curr = ""
            elif c == '"':
                quote = not quote
            else:
                curr += c

        if curr:
            arg1.append(curr)

        if len(arg1) < 1:
            print("** class name missing **")
        elif not self.cls_check(arg1[0]):
            return
        elif len(arg1) < 2:
            print("** instance id missing **")
        elif len(arg1) < 3:
            print("** attribute name missing **")
        elif len(arg1) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(arg1[0], arg1[1])
            if obj_key in storage.all():
                instance = storage.all()[obj_key]
                attribute_name = arg1[2]
                value = arg1[3]
                setattr(instance, attribute_name, value)
                storage.save()
            else:
                print("** no instance found **")

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

    def precmd(self, arg):
        """Executes before arg"""
        pattern = re.compile(r"(\S+)\.(\S+)\((.*)\)")
        match = pattern.search(arg)
        if not match:
            return arg

        matched = match.groups()
        if matched[1] == "all":
            return "{} {}".format(matched[1], matched[0])
        elif matched[1] == "count":
            count = 0
            for i in storage.all().keys():
                pattern = re.compile(r"{}".format(matched[0]))
                if pattern.match(i):
                    count += 1
            print(count)
            return "\n"
        elif matched[1] in ["show", "destroy"]:
            return "{} {} {}".format(matched[1], matched[0], matched[2][1:-1])
        elif matched[1] == "update":
            args = matched[2].split(", ")
            if args[1][0] == "{":
                obj_key = "{}.{}".format(matched[0], eval(matched[2])[0])
                if obj_key in storage.all():
                    obj = storage.all()[obj_key]
                    update_dict = eval(matched[2])[1]
                    for key, value in update_dict.items():
                        setattr(obj, key, value)
                    storage.save()
                else:
                    print("** no instance found **")
                return "\n"
            elif len(args) == 3:
                return "{} {} {} {} {}".format(
                        matched[1], matched[0],
                        args[0][1:-1], args[1][1:-1], args[2])
        else:
            return "command doesn't exist"

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
