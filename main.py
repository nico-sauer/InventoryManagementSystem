from inventory.inventory_manager import InventoryManager
from inventory.product import Product
import time
import sys
from random import randint
import re

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
        print("***********************************")
        print("")
        print("Enter mode:")
        print("  > 1. Cash Register.")
        print("  > 2. Inventory Management.")
        print("")
        print("  Click 'x' to quit.")
    
        option = input("Enter your option (1 or 2) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 or 2 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
            cash_register()
            
        elif option == "2":
            inventory_menu()
        
        else:
            sys.exit() 
        
 
        
#function to add a new product to inventory             
def new_item():
    
    name = input("Name: ").title()  
    price = float(input("Product Price: "))
    cost_price = float(input("Product Cost Price: "))
    category = input("Category: ").title()
    colour = input("Colour: ").title()
    quantity = int(input("Quantity: "))
    brand = input("Brand: ")
    id = randint(10000, 99999) 
    while id in manager.get_product_ids():
        id = randint(10000, 99999) 
    print(id)
    return Product(id, name, price, quantity, cost_price, brand, category, colour)
    
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
           #maybe check if id exists before item menu opens maybe with get_product_ids
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
            category = input("—> ").title()
            manager.sort_by_category(category)
            time.sleep(2)
        
        elif option == "4":
            print("Enter product name:")
            name = input("—> ").title()
            manager.sort_by_name(name)
            
        elif option == "5":
            print("Enter product colour:")
            colour = input("—> ").title()
            manager.sort_by_colour(colour)
            
        elif option == "6": 
            product = new_item()
            manager.add_product(product)
            manager.save_products(products_file)
            time.sleep(1)
        
        else:
            #sys.exit() 
            main()

#item inventory menu 
         
def item_menu(id):
   
    while True:

        print("")
        print("************************")
        print(manager.get_product_info(id))
        print("")
        time.sleep(1)
        print("  > 1. Update Stock.")
        print("  > 2. Update Price.")
        print("  > 3. Update Category.")
        print("  > 4. Update Name.")
        print("  > 5. Update Colour.")
        print("  > 6. Delete Product.")
        print("")
        print("  Click 'x' to return to Inventory Menu.")
        print("************************")
        
        option = input("Enter your option (1 to 6) or 'x' to leave:\n—> ").lower()
        
        while option not in (["1", "2", "3", "4", "5", "6", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 6 or 'x' to leave.):\n—> ").lower()
        
        if option == "1":
            update_stock(id)
            
         
        elif option == "2":
            new_price = float(input("Enter updated price: "))
            new_cost_price = float(input("Enter updated cost price: "))
            manager.update_price(id, new_price)
            manager.update_cost_price(id, new_cost_price)
            manager.save_products(products_file)
            print(f"Product price updated. Current Price: {new_price}.\nCost price updated. Current cost price: {new_cost_price}.")
        
        elif option == "3":
            new_category = input("Enter updated category: ").title()
            manager.update_category(id, new_category)
            manager.save_products(products_file)
            print(f"Product category updated. Current category: {new_category}.")
            
        elif option == "4":
            new_name = input("Enter updated name: ").title()
            manager.products[int(id)].update_name(new_name)
            manager.save_products(products_file)
            print(f"Product name updated. Current name: {new_name}.")
        
        elif option == "5":
            new_colour = input("Enter updated colour: ").title()
            manager.products[int(id)].update_colour(new_colour)
            manager.save_products(products_file)
            print(f"Product colour updated. Current colour: {new_colour}.")
        
        elif option == "6":
            manager.remove_product(id)
            manager.save_products(products_file)
            inventory_menu()
               
        else:
            inventory_menu()


def cash_register():
    #could be used to keep track of transactions with separate file or print receipt or whatever.
    transaction = True
    print("Start Transaction.\nPlease scan items or enter ID manually.\
        \nTo return or cancel a purchase first press 'x.\n Click = end transaction")
    
    while transaction: 
        scan = input(">>> ").lower()
        if scan == "=":
            print("placeholder for printing receipt with total")
            transaction = False
            
        elif re.match("^(['x']?[0-9]\\d*|0)$", scan):
            if scan.isdigit():
                id = scan
                update_by = 1
                if manager.products.get(scan, None) == None:
                    print("Product not found. Please try again: ")
                    continue
                manager.remove_stock_from_inventory(id, update_by)
                manager.save_products(products_file)
                #could add item name + price to receipt for example
                
            elif scan[0] == "x":
                id = int(scan[1:])
                update_by = 1
                manager.add_stock_to_inventory(id, update_by)
                manager.save_products(products_file)
        
    
    #54674 item id for testing
def update_stock(id):
    while True:
        option = input("To add or remove stock press +/- and select amount.\nTo manually edit stock enter custom amount.\nPress 'x' to cancel.\n-> ").lower()
        if re.match("^([+-]?[0-9]\\d*|0)$", option):
            break
        elif option == "x":
            item_menu(id)
         
    if option.isdigit():
        new_quantity = int(option)
        manager.update_quantity(id, new_quantity)
        manager.save_products(products_file)
        print(f"Updated quantity in inventory. Current Quantity: {new_quantity}.")
        
    elif option[0] == "+":
        update_by = int(option[1:])
        manager.add_stock_to_inventory(id, update_by)
        manager.save_products(products_file)
        
    elif option[0] == "-":
        update_by = int(option[1:])
        manager.remove_stock_from_inventory(id, update_by)
        manager.save_products(products_file)
  
if __name__ == "__main__":
    main()