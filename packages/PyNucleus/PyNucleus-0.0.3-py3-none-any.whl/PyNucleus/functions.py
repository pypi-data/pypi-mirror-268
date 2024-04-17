#######################################
# IMPORTS
#######################################

import random
import string

from PyNucleus.errors import InvalidPrefix

from colorama import init, Fore, Back, Style

#######################################
# INIT
#######################################

init(convert=True)

#######################################
# VARIABLES
#######################################

NUMBERS = "0123456789"
UPPERS  = string.ascii_uppercase
LOWERS  = string.ascii_lowercase

#######################################
# FUNCTIONS
#######################################

def PrintError(error) -> int:
    """
    ## Print error with red foreground.
    """
    print(f"{Fore.RED}{error}{Style.RESET_ALL}")
    return 0

def PrintSuccess(success) -> int:
    """
    ## Print success message with green foreground.
    """
    print(f"{Fore.GREEN}{success}{Style.RESET_ALL}")
    return 0

def generate_id(length: int=16, numbers: bool=True, lowers: bool=True, uppers: bool=True) -> str:
    """
    ## Generate ID with numbers, uppercase and lowercase letters.

    ### Example of generated ID: 
    * 7wCxklbqgbXkO0K6
    """
    chars = ""
    if numbers: chars += NUMBERS
    if lowers: chars += LOWERS
    if uppers: chars += UPPERS

    return ''.join(random.choice(chars) for _ in range(length))

def generate_custom_id(prefix: str, length: int=16) -> str:
    """
    ## Generate custom ID with numbers, uppercase and lowercase letters.

    ### How to write prefix?
    * Prefix must not be None.
    * Prefix must not have any numbers, special characters or spaces.

    ### Example of generated custom ID: 
    * $EXAMPLE#7wCxklbqgbXkO0K6
    """
    if not prefix: 
        PrintError(InvalidPrefix(prefix))
        return None
    else: 
        for c in prefix:
            if not c in UPPERS + LOWERS:
                PrintError(InvalidPrefix(prefix))
                return None
        return f"${prefix}#" + generate_id(length)