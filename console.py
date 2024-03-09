#!/usr/bin/python3
"""
Module console
"""
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Command line interface class"""

    prompt = "(hbnb) " if sys.stdin.isatty() else "(hbnb) \n"
    existed_models = {"BaseModel": BaseModel, }

    def do_create(self, arg):
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
        get_id = arg.split()[1]
        instance = storage.all()
        model = arg.split()[0]

        if arg:
            if model in self.existed_models:
                if get_id:
                    print(instance)
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Deletes an instance
        """
        get_id = arg.split()[1]
        model = arg.split()[0]

        if arg:
            if model in self.existed_models:
                if get_id:
                    storage.reload()
                    if storage.__objects[model] == get_id:
                        del storage.__objects[model]
                        storage.save()
                        return
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, model):
        """
        Prints representation of all instances
        """
        if model:
            if model in self.existed_models:
                for key in storage.__objects.items:
                    print(str())
        else:
            print(storage.all())

    def do_EOF(self, arg):
        """
        Handles the EOF condition.
        """
        return True

    def do_quit(self, arg):
        """Quits the program."""
        return True

    def do_empty(self, arg):
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
