class Product:
    """The Products that we are managing"""
    
    def __init__(self, id: int, name: str, price: float, quantity: int):
        """Initiator for Product, assigning default values

        Args:
            id (int): The id of the product
            name (str): The product name
            price (float): The product price
            quantity (int): The product quantity
        """
        self.id = id
        self.name = name 
        self.price = price
        self.quantity = quantity
    
    def update_quantity(self, quantity: int):
        """Update the quantity of the product"""
        self.quantity = quantity
    
    def update_price(self, price: float):
        """Update the price of the product"""
        self.price = price
    
    def get_product_info(self):
        """Get the product information as a string representation"""
        return f"Product id: {self.id}, name: {self.name} price; ${self.price: float}, quantity: {self.quantity}"