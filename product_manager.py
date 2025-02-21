from product import Product

class ProductManager():
    def __init__(self): 
        self.products =[]
                       
    def add_product(self, product):
        self.products.append(product)
               
    def display_products(self):
        print(f"Lista produselor este: ")
        print(self.products)
       
    def total_spent(self): 
        return sum(item.price * item.quantity for item in self.products)
    
    def remove_product(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
               