class Product:
    """The Products that we are managing"""
    
    def __init__(self, id: int, name: str, price: float, quantity: int, cost_price: float, category: str):
        """Initiator for Product, assigning default values

        Args:
            id (int): The id of the product
            name (str): The product name
            price (float): The product price
            quantity (int): The product quantity
        """
        self.__id = id
        self.__name = name 
        self.__price = price
        self.__quantity = quantity
        self.__cost_price = cost_price
        self.__category = category
    
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
    def category(self) -> str:
        return self.__category
    @category.setter
    def category(self, category):
        self.__category = category
        
        
    def update_quantity(self, quantity: int):
        """Update the quantity of the product"""
        self.__quantity = quantity
    
    def update_price(self, price: float):
        """Update the price of the product"""
        self.__price = price
        
    def update_cost_price(self, cost_price: float):
        """Update the cost price of the product."""
        self.__cost_price = cost_price
        
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
        return f"Product id: {self.__id}, name: {self.__name} price; ${self.__price}, Cost Price: ${self.__cost_price}, quantity: {self.__quantity}"