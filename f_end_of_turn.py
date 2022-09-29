from _helper_functions import *

class End_of_turn():
    '''function to do any submitted commands at the end of turn
    usage: append a python command as a string with ? replacing any variables
            append variables to end_args'''
    def __init__(self):
        self.end_commands = []
        self.end_args = []

    def add_end_command(self, command, args):
        '''add commands and corresponding args to end of turn'''
        self.end_commands.append(command)
        self.end_args.extend(args)


    def end_of_turn(self):
        a = iter(self.end_args)
        for command in self.end_commands:
            command = list(command)
            for i, char in enumerate(command):
                if char == '?':
                    command.pop(i)
                    command.insert(i, "next(a)")

            exec("".join(command))

        #reset end_of_turn lists
        self.end_args = []
        self.end_commands = []