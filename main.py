from product_manager import ProductManager
from product import Product

if __name__ == '__main__':
    products = [
        Product("Ochelari", 589.99, 17),
        Product("Stilou", 124.49, 23),
        Product("Carte electronica", 44.45, 10) 
    ]

for product in products:
        print(product.display_info())

print(products[0].update_quantity(5))
print(products[1].update_quantity(2))
print(products[2].update_quantity(10))
    
product_manager = ProductManager()

for product in products:
    product_manager.add_product(product)
    
product_manager.add_product(Product("Caiet", 10.5, 2))
product_manager.display_products()

print(f"Valoarea totală a inventarului: {product_manager.total_spent()} RON")

product_manager.remove_product("Stilou")
product_manager.display_products()

 