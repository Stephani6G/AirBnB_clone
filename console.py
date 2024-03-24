#!/usr/bin/python3
"""Contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the hbnb project"""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Commnad to exit the HBNB console"""
        return True

    def do_EOF(self, args):
        """Handles EOF to exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
