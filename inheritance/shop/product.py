class Product:

    def __init__(self, name: str, quantity: int):
        self.name = str(name)
        self.quantity = int(quantity)

    def decrease(self,quantity: int):
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self,quantity):
        self.quantity += quantity

    
