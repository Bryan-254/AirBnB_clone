#!/usr/bin/python3
"""Console module for the command interpreter."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create new instance, save to JSON file, and print id."""
        if not arg:
            print("** class name missing **")
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
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
        """Deletes an instance."""
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
        """Prints all string representations of instances."""
        obj_dict = storage.all()
        if not arg:
            print([str(obj_dict[obj]) for obj in obj_dict])
        elif arg not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[obj]) for obj in obj_dict
                  if obj.startswith(arg)])

    def do_update(self, arg):
        """Updates an instance."""
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
        """Do nothing on empty line."""
        pass

    def do_EOF(self, line):
        """Exit the console."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
