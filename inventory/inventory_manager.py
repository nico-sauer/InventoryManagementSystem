from inventory.product import Product
import json

class InventoryManager:
    
    saved_inventory_filename = "saved_inventory.txt"
    
    def __init__(self):
        self.products = {}  # key = id, value = Product
    
    def save_products(self):
        """Saves the current products to a file"""
        with open(self.saved_inventory_filename, "w") as fp:  # w = write
            json.dump(self.products, fp)  # encode dict into JSON
        
    def load_products(self):
        """Loads the products from a file"""
        with open(self.saved_inventory_filename, "r") as fp:  # r = read
            # Load the dictionary from the file
            self.products = json.load(fp)
    
    def add_product(self, product: Product):
        """Adds a new or overrides an existing product with the given product"""
        self.products[product.id] = product
    
    def remove_product(self, product_name: str):
        """Removes a product by name"""
        # get the id by name:
        id = next((id for id, name in self.products.items() if name == product_name), None)
        self.products.pop(id, None)  # "None" caters for if key was not found: then do nothing.
    
    def update_quantity(self, product_id: int, new_quantity: int):
        """Update quantity of specified product"""
        self.products[product_id].update_quantity(new_quantity)
        
    def update_price(self, product_id: int, new_price: float):
        """Update price of specified product"""
        self.products[product_id].update_price(new_price)
    
    def update_cost_price(self, product_id: int, new_cost_price: float):
        """Update cost price of specified product"""
        self.products[product_id].update_cost_price(new_cost_price)
    
    def get_product_id(self, product_name: str):
        """Gets the first id of a product by the given name"""
        return next((id for id, name in self.products.items() if name == product_name), None)
    
    def get_product_info(self, product_name: str):
        """Retrieve product information by name"""
        # get the id by name:
        id = next((id for id, name in self.products.items() if name == product_name), None)
        if id == None:
            return "Product not found"
        else:
            return self.products[id].get_product_info()
    
    def get_total_inventory_value(self):
        """Calculate the total value of the entire inventory"""
        total = 0.0  # initialise a float
        for prod in self.products.values():
            total += prod.price * prod.quantity
        return total
    
    

