from inventory.inventory_manager import InventoryManager
from inventory.product import Product
import time
import sys
from random import randint

manager = InventoryManager()
products_file = "./inventory/saved_inventory.txt"
def main():

    #load the inventory from file:
    manager.load_products(filename=products_file)
    
    while True:
        
        print("***********************************")
        print("*              ***                *")
        print("*           Inventory             *")
        print("*       Managment System          *")
        print("*              ***                *")
    
        inventory_menu()

#function to add a new product to inventory             
def new_item():
    
    name = input("Name: ").capitalize()  
    price = float(input("Product Price: "))
    cost_price = float(input("Product Cost Price: "))
    category = input("Category: ").capitalize()
    colour = input("Colour: ").capitalize()
    quantity = int(input("Enter Quantity: "))
    id = randint(10000, 99999) 
    while id in manager.get_product_ids():
        id = randint(10000, 99999) 
    print(id)
    return Product(id, name, price, quantity, cost_price, category, colour)
    


#inventory menu
def inventory_menu():
   
    while True:
    
        print("***********************************")
        print("")
        print(" >>> Menu Options:")
        time.sleep(1)
        print("     ————————————— ")
        print("")
        print("  > 1. Access Product by ID.")
        print("  > 2. Show Full Inventory.") 
        print("  > 3. Show Inventory by Category.")
        print("  > 4. Show Inventory by Name.")
        print("  > 5. Show Inventory by Colour.")
        print("  > 6. Add new product to inventory.")
        print("")
        print("   Click 'x' to quit. ")
        print("***********************************")

        option = input("Enter your option (1 to 6) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "3", "4", "5", "6", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 6 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
           print("Enter product ID number:")
           id = input("ID —> ")
           item_menu(id)
            
        #checking specific item in inventory                  
        elif option == "2":
             #print out whole inventory
            for key in manager.get_product_ids():
                print(manager.get_product_info(key))
                time.sleep(1)
                
            #get_total_inventory_value 
            print(f"Total Inventory Value: {manager.get_total_inventory_value():.2f}€")
            time.sleep(2)
               
        elif option == "3":
            print("Enter product category:")
            category = input("—> ").capitalize()
            manager.sort_by_category(category)
            time.sleep(2)
        
        elif option == "4":
            print("Enter product name:")
            name = input("—> ").capitalize()
            manager.sort_by_name(name)
            
        elif option == "5":
            print("Enter product colour:")
            colour = input("—> ").capitalize()
            manager.sort_by_colour(colour)
            
        elif option == "6": 
            product = new_item()
            manager.add_product(product)
            manager.save_products(products_file)
            time.sleep(1)
        
        else:
            sys.exit() 

#item inventory menu 
         
def item_menu(id):
   
    while True:

        print("")
        print("************************")
        print(manager.get_product_info(id))
        print("")
        time.sleep(1)
        print("  > 1. Update Quantity.")
        print("  > 2. Update Price.")
        print("  > 3. Delete Product.")
        print("")
        print("  Click 'x' to return to Inventory Menu.")
        print("************************")
        
        option = input("Enter your option (1 to 3) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "3", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 3 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
            new_quantity = int(input("Enter new quantity: "))
            manager.update_quantity(id, new_quantity)
            manager.save_products(products_file)
            print(f"Updated quantity in inventory. Current Quantity: {new_quantity}.")
            
         
        elif option == "2":
            new_price = float(input("Enter updated price: "))
            new_cost_price = float(input("Enter updated cost price: "))
            manager.update_price(id, new_price)
            manager.update_cost_price(id, new_cost_price)
            manager.save_products(products_file)
            print(f"Product price updated. Current Price: {new_price}.\nCost price updated. Current cost price: {new_cost_price}.")
        
        elif option == "3":
            manager.remove_product(id)
            manager.save_products(products_file)
            inventory_menu()
               
        else:
            inventory_menu()

if __name__ == "__main__":
    main()