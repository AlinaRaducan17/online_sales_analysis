class Cart():
    def __init__(self): 
        self.cart_items =[]
    
    def add_product_cart(self, product):
        self.cart_items.append(product)
        
    def total_spent_cart(self): 
        return sum(item.price * item.quantity for item in self.cart_items)
    
    def display_products_cart(self):
        print(f"Lista produselor este: ")
        print(self.cart_items)