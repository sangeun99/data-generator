from generators.common.address import Address
from generators.common.id import Id
from generators.store.storetype import StoreType

class Store:
    def __init__(self) :
        self.id = Id().generate()
        self.type = StoreType().generate()
        self.address = Address().generate()
        location = self.address.split()[2]
        self.name = f"{self.type} {location}점"

    def generate(self):
        generatedData = {
            "id" : self.id, 
            "name" : self.name, 
            "type" : self.type, 
            "address" : self.address
        }
        return generatedData