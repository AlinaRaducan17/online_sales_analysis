from product_manager import ProductManager
from product import Product
from cart import Cart

if __name__ == '__main__':
    products = [
        Product("Ochelari", 589.99, 17),
        Product("Stilou", 124.49, 23),
        Product("Carte electronica", 44.45, 10) 
    ]

# for product in products:
#         print(product.display_info())

print(products[0].update_quantity(5))
print(products[1].update_quantity(2))
print(products[2].update_quantity(10))
    
product_manager = ProductManager()

for product in products:
    product_manager.add_product(product)
    
product_manager.add_product(Product("Caiet", 10.5, 2))
# product_manager.display_products()

product_manager.remove_product("Stilou")
# product_manager.display_products()

cart = Cart()
cart.add_product_cart(products[0])
cart.add_product_cart(products[1])
cart.add_product_cart(products[2])
    
print("Cosul contine urmtoarele produse:")
cart.display_products_cart()
print(f"Total de plată: {cart.total_spent_cart()} RON")
