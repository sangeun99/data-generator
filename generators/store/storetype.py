import random

from generators.generators import GeneratorBase

class StoreType(GeneratorBase):
    
    types = []

    def __init__(self) :
        self.type = random.choice(StoreType.types)
    
    def generate(self) :
        return self.type