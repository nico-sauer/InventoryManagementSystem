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
    
    def update_quantity():
        """Update the quantity of the product"""
        pass
    
    def update_price():
        """Update the price of the product"""
        pass
    
    def get_product_info():
        """Get the product information as a string representation"""
        pass