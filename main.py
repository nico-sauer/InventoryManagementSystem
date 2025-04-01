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
        print("*         Inventory               *")
        print("*       Managment System          *")
        print("*              ***                *")
        print("***********************************")
        time.sleep(1)
        print("")
        print("")
        print("************************")
        print(" >>> Menu Options:")
        print("  > 1. Check Inventory.") #check whole inventory
        print("  > 2. Check Product Inventory") #check specific product
        print("  > 3. Add new product.")  #add new product immediately
        print("")
        print("   Click 'x' to quit. ")
        print("************************")
        option = input("—> ").lower()
        
        while option not in (["1", "2", "3", "x"]):
            print("Invalid Input. Try again.")
            option = input("—> ").lower()
        
        #checking inventory 
        if option == "1":
            time.sleep(1)
            inventory_menu()
                  
        #checking specific item in inventory             
        elif option == "2":
            time.sleep(1)
            print("Scan barcode or enter product number:")
            id = input("ID —> ")
            time.sleep(1)
            item_menu(id)
            break
              
        #add new product 
        elif option == "3":
            product = new_item()
            manager.add_product(product)
            manager.save_products(products_file)
            
        else:
            sys.exit()
            
#function to add a new product to inventory             
def new_item():
    
    name = input("Name: ")     
    price = float(input("Product Price: "))
    cost_price = float(input("Product Cost Price: "))
    category = input("Category: ")
    quantity = int(input("Enter Quantity: "))
    id = randint(1000, 99999) 
    while id in manager.get_product_ids():
        id = randint(1000, 99999) 
    print(id)
    return Product(id, name, price, quantity, cost_price, category)
    
#item inventory menu 
         
def item_menu(id):
   
    while True:

        print("")
        print("************************")
        print("Printing the current inventory details of 'scanned' product.") #take out later
        print(manager.get_product_info(id))
        print("  > 1. Update Quantity")
        print("  > 2. Update Price")
        print("  > 3. Return to Inventory Menu.")
        print("")
        print("   Click 'x' to quit. ")
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
            manager.update_price(new_price)
            manager.update_cost_price(new_cost_price)
            manager.save_products(products_file)
            print(f"Product price updated. Current Price: {new_price}.\nCost price updated. Current cost price: {new_cost_price}.")
        
        
        elif option == "3":
            inventory_menu()
               
        else:
            sys.exit() 

#inventory menu
def inventory_menu():
   
    while True:
        print("")
        print("************************")
        print(" >>> Menu Options:")
        print("")
        print("  > 1. Full Inventory.") 
        print("  > 2. Check Product.")
        print("  > 3. Third Option Maybe")
        print("")
        print("   Click 'x' to quit. ")
        print("************************")

        option = input("Enter your option (1 to 3) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "3", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 3 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
            #print out whole inventory
            for key in manager.get_product_ids():
                print(manager.get_product_info(key))
                
            #get_total_inventory_value 
            print(f"Total Inventory Value: {manager.get_total_inventory_value():.2f}€")
         
        #checking specific item in inventory                  
        elif option == "2":
            print("Enter product ID number:")
            id = input("ID —>")
            item_menu(id)
        
        elif option == "3":
            #leaving this here for now just in case we want another option
            pass
               
        else:
            sys.exit() 



if __name__ == "__main__":
    main()
