from PyNucleus.errors import MemoryException, MemoryInitFailed
from PyNucleus.functions import PrintError

import sys

class Memory:
    """
    ## Memory class to store byte arrays on addresses.
    """
    def __init__(self, size: int) -> None:
        self.memory: list[bytearray] = []
        self.showErrors = True

        self.inited = self.OnInit(size)

    def OnInit(self, size: int) -> bool:
        if type(size) != int:
            if self.showErrors: PrintError(MemoryInitFailed(f"OnInit({size}) | Size must be an integer"))
            return False
        
        self.size = size
        self.memory = [bytearray() for _ in range(self.size + 1)]
        return True

    def GetAddress(self, address: int) -> bytearray:
        """
        ## Get byte array stored on address.
        """
        if type(address) != int:
            if self.showErrors: PrintError(MemoryException(f"GetAddress({address}) | Address must be an integer"))
            return None
        
        if address < 0 and address > len(self.memory):
            if self.showErrors: PrintError(MemoryException(f"GetAddress({address}) | Address must be greather than 0 and less than {len(self.memory)}"))
            return None
        
        return self.memory[address]

    def WriteAddress(self, address: int, value: bytearray) -> int:
        """
        ## Write byte array to address.
        """
        if self.inited:
            if address < 0 or address > len(self.memory):
                if self.showErrors: PrintError(MemoryException(f"WriteAddress({address}, {value}) | Address must be greather than 0 and less than {len(self.memory)}"))
                return -1
            else:
                self.memory[address] = value
                return 0
        else:
            if self.showErrors: PrintError(MemoryException(f"WriteAddress({address}, {value}) | The memory was not initialized successfully"))
            return -1
        
    def __repr__(self) -> str:
        return f"Memory class: {sys.getsizeof(self.memory)} bytes of size"