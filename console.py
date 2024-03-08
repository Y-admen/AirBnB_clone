#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.__init__ import storage
class HBNBCommand(cmd.Cmd):
    """Command line interface class"""
    
    prompt = "(hbnb) "
    existed_classes = ["BaseModel", "FileStorage"]

    
    def do_create(self, arg):
        if arg:
            if arg in  self.existed_classes:
                new = BaseModel(arg)
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def  do_show(self, arg):
        get_id = arg.split()[1]
        instance = storage.all()
        get_class = arg.split()[0]
        
        if arg:
            if get_class in  self.existed_classes:
                if get_id:
                    print(instance)
                else:
                   print ("** instance id missing **") 
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    def do_destroy(self, arg):
        get_id = arg.split()[1]
        get_class = arg.split()[0]
        
        if arg:
            if get_class in  self.existed_classes:
                if get_id:
                    storage.reload()
                    if storage.__objects[get_class] == get_id:
                        del  storage.__objects[get_class]
                        storage.save
                else:
                   print ("** instance id missing **") 
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        
    def do_all(self,arg):
        if arg:
            if arg in  self.existed_classes:
                for key in storage.__objects.items:
                    print(str())
            
                
        else:
                print(storage.all())
    
        
    def do_eof(self, arg):
        """command handeler:Handles the EOF condition."""
        return True

    def do_quit(self, arg):
        """Quits the program."""
        return True

    def do_empty(self, arg):
        """Ignores empty commands"""
        pass

    def do_help(self, arg):
        """""Shows help for a command"""""
        command_help = {
        "quit": "Quit: Exit the program normally.",
        "EOF": "Exit the program with Ctrl+D.",
        "help": "Show help for available commands."}
        if arg:
            if arg in  command_help:
                print(command_help[arg])
            else:
                print(f"No command available for '{arg}'.")
        
                 
if __name__ == '__main__':
    HBNBCommand().cmdloop()
