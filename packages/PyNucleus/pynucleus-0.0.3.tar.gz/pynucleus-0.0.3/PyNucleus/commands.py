#######################################
# IMPORTS
#######################################

import inspect

from PyNucleus.errors import (
    InvalidCommand, 
    InvalidCommandName, 
    InvalidCommandFunction
    )
from PyNucleus.functions import PrintError

from typing import Callable

#######################################
# CLASSES
#######################################

def check_command_func(func) -> bool:
    """
    ## Check if command function is valid.
    """
    signature = inspect.signature(func)
    params = signature.parameters

    first_param_name = next(iter(params))
    first_param = params[first_param_name]

    try:
        if first_param.annotation == list[str]:
            return signature.return_annotation == int
        else:
            return False
    except:
        return False

#######################################
# CLASSES
#######################################

class CommandBase:
    """
    ## Only command class that is compatible with CommandRegister.

    ### >> Example of usage:
    ```
    from PyNucleus.commands import CommandBase

    def HelpCommand(args: list[str]) -> int:
        print("This is an example help command!")
        return 0

    command = CommandBase("help", "Display all commands", HelpCommand)
    ```
    """
    def __init__(self, name: str, details: str, func: Callable) -> None:
        self.name = name
        self.details = details
        self.func = func

    def Run(self, args: list[str]) -> int:
        return self.func(args)

    def __repr__(self) -> str:
        return f"Command '{self.name}'"

class CommandRegister:
    """
    ## The command register is used to make command management easier.

    ### >> Example of usage:
    ```
    from PyNucleus.commands import CommandRegister
    
    commandRegister = CommandRegister()
    ```
    """
    def __init__(self, printErrors: bool=True) -> None:
        self.commands: list[CommandBase] = []
        self.printErrors = printErrors

    def AddCommand(self, name: str, func: Callable[[list[str]], int]) -> int:
        """
        ## Add a command to the register.

        ### Posible errors:
        * Invalid Command Name
        * Invalid Command Function

        ### >> Example of usage:
        ```
        from PyNucleus.commands import CommandBase, CommandRegister

        commandRegister = CommandRegister()

        def HelpCommand(args: list[str]) -> int:
            print("This is an example help command.")
            return 0

        newCommand = CommandBase("help", "Display all commands", HelpCommand)

        commandRegister.AddCommand(newCommand)
        ```
        """
        for command in self.commands:
            if command.name == name:
                if self.printErrors: PrintError(InvalidCommandName(name, "This name is already taken"))
                return -1
            
        if not check_command_func(func):
            if self.printErrors: PrintError(InvalidCommandFunction(name, "Look on example of function in AddCommand description"))
            return -1
        
        newCommand = CommandBase(name, func)
        self.commands.append(newCommand)
        return 0

    def DeleteCommand(self, name: str) -> int:
        """
        ## Delete a command from register.

        ### Posible errors:
        * Invalid Command Name

        ### >> Example of usage:
        ```
        from PyNucleus.commands import CommandBase, CommandRegister

        ...

        commandRegister.DeleteCommand("help")
        ```
        """
        index = 0
        for command in self.commands:
            if command.name == name:
                self.commands.pop(index)
                return 0
            index += 1
            
        if self.printErrors: PrintError(InvalidCommandName(name, "Cannot delete command because that name does not exist"))
        return -1
    
    def HandleCommand(self, command: str, args: list[str]=[]) -> int:
        """
        ## Handle command from user.

        ### Posible errors:
        * Invalid Command

        ### >> Example of usage:
        ```
        from PyNucleus.commands import CommandRegister, CommandBase

        ...
        
        userInput = input(">: ")
        words = userInput.split()

        command, args = "", []

        if len(words) > 0: 
            command = words[0]
        if len(words) > 1:
            args = words[1:]

        commandRegister.HandleCommand(newCommand)
        ```
        """
        for cmd in self.commands:
            if cmd.name == command:
                cmd.Run(args)
                return 0
        
        if self.printErrors: PrintError(InvalidCommand(command, "That command does not exist"))
        return -1
    
    def HandleInput(self, entry: str="") -> int:
        """
        ## Handle the entire input from user.

        ### Posible errors:
        * Invalid Command

        ### >> Example of usage:
        ```
        from PyNucleus.commands import CommandRegister, CommandBase

        ...
        
        userInput = input(">: ")

        commandRegister.HandleInput(userInput)
        ```
        """
        words = entry.split()
        cmd = ""
        args = []
        if len(words) > 0: cmd = words[0]
        if len(words) > 1: args = words[1:]

        return self.HandleCommand(cmd, args)

    def __repr__(self) -> str:
        return f"CommandRegister: {len(self.commands)} commands"