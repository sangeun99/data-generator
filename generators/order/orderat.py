import random
from datetime import datetime, timedelta

from generators.generators import GeneratorBase

class OrderAt(GeneratorBase) :
    
    def __init__(self): 
        
        min_year=2022
        max_year=datetime.now().year

        start = datetime(min_year, 1, 1, 00, 00, 00)
        years = max_year - min_year+1
        end = start + timedelta(days=365 * years)

        self.orderAt = start + (end - start) * random.random()

    def generate(self):
        return self.orderAt