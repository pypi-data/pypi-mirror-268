#######################################
# IMPORTS
#######################################

from PyNucleus.errors import CalculatorException

from PyNucleus.functions import PrintError

#######################################
# VARIABLES
#######################################

NUMBER_TYPES = (float, int)

#######################################
# CLASSES
#######################################

class Calculator:
    """
    ## A calculator class that solves math problems.
    """
    def __init__(self, printErrors: bool=True) -> None:
        self.printErrors = printErrors
        self.count = 0
        
    def add(self, n1: float, n2: float) -> float:
        """
        ## Add two numbers together.
        """
        if type(n1) not in NUMBER_TYPES or type(n2) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"add({n1}, {n2}) | The numbers must be a float or integer"))
            return None
        
        self.count += 1
        return n1 + n2
    
    def sub(self, n1: float, n2: float) -> float:
        """
        ## Subtract two numbers from each other.
        """
        if type(n1) not in NUMBER_TYPES or type(n2) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"sub({n1}, {n2}) | The numbers must be a float or integer"))
            return None
        
        self.count += 1
        return n1 - n2
    
    def mul(self, n1: float, n2: float) -> float:
        """
        ## Multiply two numbers.
        """
        if type(n1) not in NUMBER_TYPES or type(n2) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"mul({n1}, {n2}) | The numbers must be a float or integer"))
            return None
        
        self.count += 1
        return n1 * n2
    
    def div(self, n1: float, n2: float) -> float:
        """
        ## Divide two numbers.
        """
        if type(n1) not in NUMBER_TYPES or type(n2) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"div({n1}, {n2}) | The numbers must be a float or integer"))
            return None
        
        if n2 == 0:
            if self.printErrors: PrintError(CalculatorException("Cannot divide by 0"))
            return None
        else: 
            self.count += 1
            return n1 / n2 

    def pow(self, n1: float, n2: float)  -> float:
        """
        ## Raise a number (n1) to a power (n2)
        """
        if type(n1) not in NUMBER_TYPES or type(n2) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"sqrt({n1}, {n2}) | The numbers must be a float or integer"))
            return None
        
        self.count += 1
        return n1 ** n2
    
    def sqrt(self, number: float) -> float:
        if type(number) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"sqrt({number}) | The number must be a float or integer"))
            return None
        
        if number < 0:
            if self.printErrors: PrintError(CalculatorException("Cannot compute square root of a negative number"))
            return None

        guess = number / 2.0
        while True:
            new_guess = 0.5 * (guess + number / guess)
            if abs(new_guess - guess) < 1e-9:
                self.count += 1
                return new_guess
            guess = new_guess

    def factorial(self, n: int) -> int:
        """
        ## Calculate the product of all positive integers up to a given non-negative integer.
        """
        if type(n) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"factorial({n}) | The number must be a float or integer"))
            return None
        
        if n < 0:
            if self.printErrors: PrintError(CalculatorException("Calculate the product of all positive integers up to a given non-negative integer"))
            return None
        if n == 0:
            return 1
        
        self.count += 1
        return n * self.factorial(n - 1)

    def abs(self, n: float) -> float:
        """
        ## Get the absolute value of a number.
        """
        if type(n) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"abs({n}) | The number must be a float or integer"))
            return None
        
        self.count += 1
        return abs(n)

    def percentage(self, n: float, percent: float) -> float:
        """
        ## Get a given percentage of a given number.
        """
        if type(n) not in NUMBER_TYPES or type(percent) not in NUMBER_TYPES:
            if self.printErrors: PrintError(CalculatorException(f"percentage({n}, {percent}) | The number and percentage must be a float or integer"))
            return None
        
        self.count += 1
        return (percent / 100) * n
    
    def int_to_bytes(self, number: int) -> bytes:
        if type(number) != int:
            if self.printErrors: PrintError(CalculatorException(f"int_to_bytes({number}) | The number must be an integer"))
            return None
        
        self.count += 1
        return int.to_bytes(number)
    
    def float_to_hex(self, number: float) -> str:
        if type(number) != float:
            if self.printErrors: PrintError(CalculatorException(f"float_to_hex({number}) | The number must be a float"))
            return None
        
        self.count += 1
        return float.hex(number)
    
    ### OTHER FUNCTIONS

    def SolveString(self, entry: str) -> float:
        """
        ## Function that will solve string math problem.

        ### >> Example of usage:
        ```
        from PyNucleus.calculator import Calculator

        calc = Calculator()

        result = calc.SolveString("2 + 2 * 2")

        print(result) # Output: 6
        """
        try:
            result = eval(entry)
            return result
        except Exception as e:
            if self.printErrors: PrintError(CalculatorException(e))
            return None
        
    def Reset(self):
        self.count = 0

    def __repr__(self) -> str:
        return f"Calculator class: {self.__count} calculations"