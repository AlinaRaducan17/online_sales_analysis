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