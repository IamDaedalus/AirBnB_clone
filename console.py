#!/usr/bin/python3
""" This is a command interpreter we can use to
manipulate the ojects of our web application.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines a class which is the entry point of our command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """ overides default emptyline execution """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ Exits the program with EOF command like cntrl+D
        """
        print()
        return True

    def do_create(self, args):
        """ creates a new instance, saves it (to the json file)
        and prints the id
        """
        commands = args.split(" ")
        if not commands[0]:
            print("** class name missing **")
        else:
            class_name = commands[0]
            if class_name == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
            # TODO: are spaces handled as missing or non-existing argument?


if __name__ == '__main__':
    HBNBCommand().cmdloop()
