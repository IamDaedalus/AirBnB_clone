#!/usr/bin/python3
""" This is a command interpreter we can use to
manipulate the ojects of our web application.
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Defines a class which is the entry point of our command interpreter."""

    prompt = "(hbnb) "
    missing_class = "** class name missing **"
    unknown_class = "** class doesn't exist **"
    missing_id = "** instance id missing **"
    unknown_id = "** no instance found **"

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
        """ Create new class instance, save and display its id"""
        # need better help documentation
        if args == "" or args is None:
            print(self.missing_class)
        else:
            commands = args.split(" ")

            class_name = self.extract_arg(commands[0])
            if class_name in storage.class_map():
                # create a new instance based on the class name
                new_instance = storage.class_map()[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print(self.unknown_class)
            # TODO: are spaces handled as missing or non-existing argument?

    # GOD ABEG
    def do_show(self, args):
        """ Get and print instance str representation by id and class name"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = self.extract_arg(cmds[0])
            cls_id = self.extract_arg(cmds[1])

            # id arg check
            if len(cmds) < 2:
                print(self.missing_id)
            elif not cls_name in storage.class_map():
                print(self.unknown_class)
            else:
                val = "{}.{}".format(cls_name, cls_id)

                if val in storage.all():
                    print(storage.all()[val])
                else:
                    print(self.unknown_id)

    def do_destroy(self, args):
        """ Removes a saved instance based on class name and id"""
        if args == "" or args is None:
            print(self.missing_class)
        else:
            cmds = args.split(" ")
            cls_name = self.extract_arg(cmds[0])
            cls_id = self.extract_arg(cmds[1])

            # id arg check
            if len(cmds) < 2:
                print(self.missing_id)
            elif not cls_name in storage.class_map():
                print(self.unknown_class)
            else:
                val = "{}.{}".format(cls_name, cls_id)

                if val in storage.all():
                    storage.all().pop(val)
                else:
                    print(self.unknown_id)

    def do_all(self, args):
        """ Prints all stored args otherwise prints passed class name"""
        if args == "":
            # default behaviour to print everything in the file.json
            # if no args are passed
            for _, values in storage.all().items():
                print(values)
        else:
            cmd = self.extract_arg(args.split(" ")[0])

            # if the cmd doesn't exist don't print it
            if cmd not in storage.class_map():
                print(self.unknown_class)
            else:
                for _, values in storage.all().items():
                    if type(values).__name__ == cmd:
                        print(values)

    def do_update(self, args):
        pass

    # HELPERS
    def extract_arg(self, arg="", msg=""):
        """Given a string it returns the string itself or extracts
        the values of the string in between the quotes

        Example:
            "hello" returns hello
            'hello' returns hello

        Args:
            arg: the argument
            msg: the message to print if extraction unsuccessful
        """
        # extract the text between string quotes
        # now to match the braces for a correct formatted str
        # IF WE GET A LOT OF RED CHECKS FOR TASK 7 CONSIDER
        # REMOVING CALLS TO THIS FUNCTION AND JUST PASSING
        # THEM STRAIGHT AWAY
        if '"' in arg or '\'' in arg:
            return arg[1:-1]
        else:
            return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()
