#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """Command line interface class"""
    
    prompt = "(hbnb) "

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
