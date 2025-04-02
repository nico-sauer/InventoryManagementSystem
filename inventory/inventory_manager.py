from inventory.product import Product
import pickle

class InventoryManager:
     
    
    def __init__(self):
        self.products = {}  # key = id, value = Product
    
    def save_products(self, filename: str):
        """Saves the current products to a file"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)
        
    def load_products(self, filename: str):
        """Loads the products from a file"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                self.products = obj.products
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
    
    def get_total_inventory_value(self):
        """Calculate the total value of the entire inventory"""
        total = 0.0  # initialise a float
        for prod in self.products.values():
            total += prod.price * prod.quantity
        return total
    