from inventory.product import Product
import json

class InventoryManager:
     
    filename: str = "saved_inventory.json"
    
    def __init__(self):
        self.products = {}  # key = id, value = Product
    
    def save_products_to_file(self):
        """Saves the current products to a file"""
        with open(self.filename, "w") as file:
            json.dump(self.__serialise_products(), file, indent=2)
            
    def __serialise_products(self) -> dict:
        """Serialises the self.products dictionary, because otherwise it cannot be saved to JSON."""
        serialised_dict = {}
        for key, product in self.products.items():
            serialised_dict[key] = product.__dict__
        return serialised_dict
        
    def load_products_from_file(self):
        """Loads the products from a file"""
        try:
            with open(self.filename, "r") as file:  # r = read
                dct = json.load(file)
                self.products = {}
                for key, values in dct.items():
                    self.products[int(key)] = Product(*values.values())
        except:
            self.products = {}
    
    def add_product(self, product: Product):
        """Adds a new or overrides an existing product with the given product"""
        self.products[product.id] = product
    
    def remove_product(self, product_id: int):
        """Removes a product by name"""
        # get the id by name:
        #id = next((id for id, name in self.products.items() if name == product_name), None)
        self.products.pop(int(product_id), None)  # "None" caters for if key was not found: then do nothing.
    
    def update_quantity(self, product_id: int, new_quantity: int):
        """Update quantity of specified product"""
        self.products[int(product_id)].update_quantity(new_quantity)
        
    def add_stock_to_inventory(self, product_id: int, update_by: int):
        """Updating quantity of product by a specific amount."""
        self.products[int(product_id)].add_stock_to_inventory(update_by)
        
    def remove_stock_from_inventory(self, product_id: int, update_by: int):
        """Updating quantity of product by a specific amount."""
        self.products[int(product_id)].remove_stock_from_inventory(update_by)
         
    def update_price(self, product_id: int, new_price: float):
        """Update price of specified product"""
        self.products[int(product_id)].update_price(new_price)
    
    def update_cost_price(self, product_id: int, new_cost_price: float):
        """Update cost price of specified product"""
        self.products[int(product_id)].update_cost_price(new_cost_price)
        
    def update_category(self, product_id: int, new_category: str):
        """Update category of specified product"""
        self.products[int(product_id)].update_category(new_category)
    
    def get_product_id(self, product_name: str):
        """Gets the first id of a product by the given name"""
        return next((id for id, name in self.products.items() if name == product_name), None)
    
    def get_product_ids(self):
        return self.products.keys()
    
    def get_product_info(self, product_id: int):
        """Retrieve product information by name"""
        # get the id by name:
        # id = next((id for id, name in self.products.items() if name == product_name), None)
        # if id == None:
        #     return "Product not found"
        # else:
        try:
            return self.products[int(product_id)].get_product_info()
        except Exception as e:
            return f"Product not found. Error: {e}"
        
    def sort_by_name(self, name):
        for prod in self.products.values():
            if name in prod.name:
                product_id = prod.id 
                print(self.products[int(product_id)].get_product_info())
    
    def sort_by_colour(self, colour):
        for prod in self.products.values():
            if colour in prod.colour:
                product_id = prod.id 
                print(self.products[int(product_id)].get_product_info())
    
    def sort_by_category(self, category):
        for prod in self.products.values():
            if category in prod.category:
                product_id = prod.id 
                print(self.products[int(product_id)].get_product_info())
                
    def sort_by_brand(self, brand):
        for prod in self.products.values():
            if brand in prod.brand:
                product_id = prod.id 
                print(self.products[int(product_id)].get_product_info())
    
    def get_total_inventory_value(self):
        """Calculate the total value of the entire inventory"""
        total = 0.0  # initialise a float
        for prod in self.products.values():
            total += prod.price * prod.quantity
        return total
    