#!/usr/bin/env python3
"""Script for the project console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[obj]) for obj in obj_dict])
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[obj]) for obj in obj_dict if obj.startswith(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in globals():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in obj_dict:
                print("** no instance found **")
            else:
                instance = obj_dict[key]
                setattr(instance, args[2], args[3])
                instance.save()

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_EOF(self, line):
        """Exit the console"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
