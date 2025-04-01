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
    
    name = input("Name: ")     
    price = float(input("Product Price: "))
    cost_price = float(input("Product Cost Price: "))
    category = input("Category: ")
    quantity = int(input("Enter Quantity: "))
    id = randint(10000, 99999) 
    while id in manager.get_product_ids():
        id = randint(10000, 99999) 
    print(id)
    return Product(id, name, price, quantity, cost_price, category)
    


#inventory menu
def inventory_menu():
   
    while True:
    
        print("***********************************")
        print("")
        print(" >>> Menu Options:")
        time.sleep(1)
        print("     ————————————— ")
        print("")
        print("  > 1. Show Full Inventory.") 
        print("  > 2. Show Inventory by Category.")
        print("  > 3. Find Product by ID.")
        print("  > 4. Find Product by Name.")
        print("  > 5. Add new product.")
        print("")
        print("   Click 'x' to quit. ")
        print("***********************************")

        option = input("Enter your option (1 to 5) or 'x' to quit:\n—> ").lower()
        
        while option not in (["1", "2", "3", "4", "5", "x"]):
            print("Invalid. Try again.")
            option = input(" > Enter your option (1 to 5 or 'x' to quit):\n—> ").lower()
        
        if option == "1":
            #print out whole inventory
            for key in manager.get_product_ids():
                print(manager.get_product_info(key))
                time.sleep(1)
                
            #get_total_inventory_value 
            print(f"Total Inventory Value: {manager.get_total_inventory_value():.2f}€")
            time.sleep(2)
        #checking specific item in inventory                  
        elif option == "2":
            print("Enter product category:")
            id = input("—> ")
            print("Printing inventory of specified category.")
            time.sleep(2)
               
        elif option == "3":
            print("Enter product ID number:")
            id = input("ID —> ")
            item_menu(id)
            
        
        elif option == "4":
            print("Enter product name:")
            name = input("—> ")
            print(f"Printing inventory of all products with name {name}.")
            #maybe in a way where we can check for similar categories
            #say clothes/clothes like if a certain amount of characters overlap
        elif option == "5":
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
