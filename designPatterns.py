
#builder pattern 
from typing import Any


def builderPattern():
    print("adapter pattern")
    vendors = []
    aws = AWS()
    azure = AZURE()
    vendors.append(Adapter(aws, createMachine = aws.createInstance))
    vendors.append(Adapter(azure, createMachine = azure.addMachinesToVmss))
    for vendor in vendors:
        vendor.createMachine()
    
class AWS:
    def __init__(self) -> None:
        self.name = "AWS"
    
    def createInstance(self) ->None:
        print("create aws instance")

class AZURE:
    def __init__(self) -> None:
        self.name = "AZURE"

    def addMachinesToVmss(self) -> None:
        print("Azure - increase vmss")

class Adapter:
    def __init__(self, object, **adapted_method) -> None:
        """Change the name of the method"""
        self._object = object
		#Add a new dictionary item that establishes the mapping between the generic method name: createMachine() and the concrete method
        self.__dict__.update(adapted_method)

    def __getattr__(self, name: str) -> Any:
        return getattr(self._object, name)
