class Product():
        def __init__(self, name : str, price : float, quantity : int):
            self.name = name
            self.price = price
            self.quantity = quantity    
        
        def display_info(self):
            return f"Produsul {self.name}, are pretul de {self.price} in cantitate de {self.quantity}"
                 
        def update_quantity(self, quantity):
            self.quantity += quantity
            return self.quantity
        
        def __str__(self):
            return f"('{self.name}', {self.price}, {self.quantity})"
        
        def __repr__(self):
            return self.__str__()

        
    
        
    