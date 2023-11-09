#!/usr/bin/python3
"""Model console: Defines HBNHCommand class."""
import cmd
import re
from models import storage
from models.base_model import BaseModel


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
    __classes = {"BaseModel"}

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, save it to json file,
        and prints the id.
        """
        arg1 = parse(arg)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg1[0])().id)
            storage.save()

    def emptyline(self, arg):
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
