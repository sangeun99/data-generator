import random

from generators.generators import GeneratorBase

class OrderId(GeneratorBase):
    
    orders = []
    selected = []

    def __init__(self):
        while True:
            orderInfo = random.choice(OrderId.orders)
            if orderInfo[0] in OrderId.selected:
                continue
            else :
                self.orderId = orderInfo[0]
                OrderId.selected.append(self.orderId)
                break
        
    def generate(self):
        return self.orderId