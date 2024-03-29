#!/usr/bin/python3
"""
Module console
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command line interface class"""

    prompt = "(hbnb) " if sys.stdin.isatty() else "(hbnb) \n"
    existed_models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
        }

    def do_create(self, model):
        """
        Creates an instance
        """
        if model:
            if model in self.existed_models:
                new_model = self.existed_models[model]()
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
            return

    def do_show(self, arg):
        """Prints representation of instance"""
        if len(arg) < 1:
            print("** class name missing **")
            return
        model, obj_id = arg.split()
        instance = storage.all()

        if model in self.existed_models:
            if obj_id:
                model_id = f"{model}.{obj_id}"
                for key, obj_value in instance.items():
                    if model_id == key:
                        print(obj_value)
                        return
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Deletes an instance
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        model = args[0]
        try:
            get_id = args[1]
        except IndexError:
            print("** instance id missing **")
            return
        if model in self.existed_models:
            model_id = "{}.{}".format(model, get_id)
            for obj_key in storage.all().keys():
                if model_id == obj_key:
                    del storage.all()[obj_key]
                    storage.save()
            else:
                print("** no instance found **")
            return
        else:
            print("** class doesn't exist **")

    def do_all(self, model):
        """
        Prints representation of all instances
        """
        obj_list = []
        if model:
            if model in self.existed_models:
                for obj_val in storage.all().values():
                    if obj_val.__class__.__name__ == model:
                        obj_list.append(obj_val.__str__())
                print(obj_list)
            else:
                print("** class doesn't exist **")
        else:
            for obj_val in storage.all().values():
                obj_list.append(obj_val.__str__())
            print(obj_list)

    def do_update(self, arg):
        """
        Handles the `update` command to update a
        specific attribute of an instance.
        """
        args = split_line(arg)
        if len(args) < 1:
            print("** class name missing **")
            return

        if len(args) == 4:
            model_name, instance_id, attr_name, attr_val = args[:4]

            if model_name not in self.existed_models:
                print("** class doesn't exist **")
                return
            if not instance_id:
                print("** instance id missing **")
                return
            model_id = f"{model_name}.{instance_id}"
            if model_id not in storage.all():
                print("** no instance found **")
                return
            if not attr_name:
                print("** attribute name missing **")
                return
            if not attr_val:
                print("** value missing **")
                return
            for obj_val in storage.all().values():
                if isinstance(attr_val, str) and attr_val.isnumeric():
                    attr_val = int(attr_val)
                if instance_id == obj_val.id:
                    setattr(obj_val, attr_name, attr_val)
                    obj_val.save()

    def do_EOF(self, arg):
        """
        Handles the EOF condition.
        """
        print()
        return True

    def do_quit(self, arg):
        """Quits the program."""
        return True

    def emptyline(self):
        """Ignores empty commands"""
        pass

    def do_help(self, arg):
        """
        Shows help for a command
        """
        command_help = {
                "quit": "Quit: Exit the program normally.",
                "EOF": "Exit the program with Ctrl+D.",
                "help": "Show help for available commands."
                }
        if arg:
            if arg in command_help:
                print(command_help[arg])
            else:
                print(f"No command available for '{arg}'.")


def split_line(line_string):
    """Split line string into words in array
    """
    output = []
    has_quote = False
    arg = ''
    for char in line_string:
        if char == ' ' and not has_quote:
            if arg:
                output.append(arg)
                arg = ''
        elif char == '"':
            has_quote = not has_quote
        else:
            arg += char
    if arg:
        output.append(arg)
    return output


if __name__ == '__main__':
    HBNBCommand().cmdloop()
