class Product:
    """The Products that we are managing"""
    
    def __init__(self, id: int, name: str, price: float, quantity: int, cost_price: float, brand: str, category: list, colour: list):
        """Initiator for Product, assigning default values

        Args:
            id (int): The id of the product
            name (str): The product name
            price (float): The product price
            quantity (int): The product quantity
        """
        self.__id = int(id)
        self.__name = name 
        self.__price = float(price)
        self.__quantity = int(quantity)
        self.__cost_price = float(cost_price)
        self.__brand = brand
        self.__category = category
        self.__colour = colour
    
    @property
    def id(self) -> int:
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
        
    @property
    def quantity(self) -> float:
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity
        
    @property
    def cost_price(self) -> float:
        return self.__cost_price
    @cost_price.setter
    def cost_price(self, cost_price):
        self.__cost_price = cost_price    
    
    @property
    def brand(self) -> str:
        return self.__brand
    @brand.setter
    def brand(self, brand):
        self.__brand = brand
        
    @property
    def category(self) -> list:
        return self.__category
    @category.setter
    def category(self, category):
        self.__category = category
    
    @property
    def colour(self) -> list:
        return self.__colour
    @colour.setter
    def colour(self, colour):
        self.__colour = colour
        
    def update_quantity(self, quantity: int):
        """Update the quantity of the product"""
        self.__quantity = quantity
    
    def add_stock_to_inventory(self, update_by: int): 
        """Add stock to inventory."""   
        self.__quantity += update_by
    
    def remove_stock_from_inventory(self, update_by: int): 
        """Remove stock from inventory"""
        self.__quantity -= update_by
        
    def update_price(self, price: float):
        """Update the price of the product"""
        self.__price = price
        
    def update_cost_price(self, cost_price: float):
        """Update the cost price of the product."""
        self.__cost_price = cost_price
        
    def update_name(self, name: str):
        """Update the name of the product."""
        self.__name = name.title()
        
    def update_colour(self, colour: list):
        """Update the colour of the product."""
        self.__colour = colour.title()
        
    def update_category(self, category: str):
        """Update the category of the product."""
        self.__category = category.capitalize()
        
    def get_discount(self) -> float:
        """return the discount."""
        return self.__price - self.__cost_price
    
    def get_total_value(self) -> float:
        """Calculate the total value of the product in the inventory (price * quantity)."""
        return self.__price * self.__quantity
    
    def get_profit(self) -> float:
        """Calculate the total profit for the product (selling price - cost price) * quantity."""
        return (self.__price - self.__cost_price) * self.__quantity            

    def get_product_info(self) -> str:
        """Get the product information as a string representation"""
        return f"Product ID—> {self.__id}\n—————————————————————————————————————————————————\
            \nName: {self.__name} | Category: {self.__category}\
            \nColour: {self.__colour} | Brand: {self.__brand}\
            \nPrice: {self.__price:.2f}€ | Cost Price: {self.__cost_price:.2f}€ | Stock: {self.__quantity}\
            \n—————————————————————————————————————————————————"
     
    
    #note —> we could also return the full value of the stock with product info 