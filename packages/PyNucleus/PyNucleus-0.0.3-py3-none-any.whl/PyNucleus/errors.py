class ErrorBase:
    def __init__(self, error: str, details: str) -> None:
        self.error = error
        self.details = details

    def __repr__(self) -> str:
        return f"{self.error}: {self.details}"
    
class InvalidPrefix(ErrorBase):
    def __init__(self, prefix: str) -> None:
        super().__init__("Invalid Pefix", prefix)

class InvalidCommandName(ErrorBase):
    def __init__(self, name: str, details: str) -> None:
        super().__init__("Invalid Command Name", f"'{name}' {f'({details})' if details else ''}")

class InvalidCommandFunction(ErrorBase):
    def __init__(self, func: str, details: str) -> None:
        super().__init__("Invalid Command Function", f"'{func}' {f'({details})' if details else ''}")

class InvalidCommand(ErrorBase):
    def __init__(self, command: str, details) -> None:
        super().__init__("Invalid Command", f"'{command}' {f'({details})' if details else ''}")

class CalculatorException(ErrorBase):
    def __init__(self, details: str) -> None:
        super().__init__("Calculator Exception", details)

class MemoryException(ErrorBase):
    def __init__(self, details: str) -> None:
        super().__init__("Memory Exception", details)

class MemoryInitFailed(ErrorBase):
    def __init__(self, details: str) -> None:
        super().__init__("Memory Init Failed", details)