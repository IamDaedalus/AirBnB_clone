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
        """ Creates a new instance of the class specified, saves
        it to the file and prints the new instance's id
        """
        class_name = ""
        commands = args.split(" ")
        if not commands[0]:
            print("** class name missing **")
        else:
            # extract the text between string quotes
            if '"' in commands[0] or '\'' in commands[0]:
                class_name = commands[0][1:-1]
            else:
                class_name = commands[0]
            # TODO: we'll probably have to make this check dynamic
            #       just like we did in FileStorage.reload()
            if class_name == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
            # TODO: are spaces handled as missing or non-existing argument?

    def do_show(self, args):
        pass

    def do_destroy(self, args):
        pass

    def do_all(self, args):
        pass

    def do_update(self, args):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
