import flet as ft  # Controls can be found here:  https://flet.dev/docs/controls
from inventory.inventory_manager import InventoryManager
from inventory.product import Product
import random

manager = InventoryManager()

def main(page: ft.Page):
    # Load products from files:
    manager.load_products_from_file()

    # Initialise page defaults
    page_initialisation(page)
    
    #region HELPER FUNCTIONS
    def clear_addedit_controls():
        """Empties the fields in row_addedit_controls"""
        for control in row_addedit_controls.controls:
            control.value = ""  # clear the value
    
    def validate_add_product_fields() -> bool:
        """Checks if the values for adding a product makes sense"""
        # validate if all values are entered
        for control in row_addedit_controls.controls:
            # must have content
            if len(control.value) == 0:
                return False
            # some content must be numeric
            if control.keyboard_type == ft.KeyboardType.NUMBER:
                try:
                    float(control.value) # isinstance(control.value, float):
                except:
                    return False
        return True  # no issues found
        
    #endregion HELPER FUNCTIONS
    
    #region CONTROL FUNCTIONS
    
    def submit_changes(e):
        """When the user pressed "Enter" to submit the changes, trigger add or save accordingly."""
        if btn_add.visible:
            add_product(e)
        else:
            save_product(e)
    
    def add_product(e):
        """Code for adding the new product to the data and grid"""
        # Toggle control visibilities
        if row_addedit_controls.visible == False:
            row_addedit_controls.visible = True
            btn_save.visible = False
            btn_delete.visible = False
            btn_cancel.visible = True
        else:
            # first do a validation of the fields
            if not validate_add_product_fields():
                # validation failed, so tell the user and then abandon the adding
                page.open(ft.AlertDialog(title=ft.Text("Invalid values!", text_align="center"), actions_padding=0,title_padding=5))
                return  
            
            # Add new product:
            new_id = random.randint(1000, 99999) 
            while new_id in manager.get_product_ids():
                new_id = random.randint(1000, 99999) 
            product = Product(new_id, 
                              str(txt_add_product_name.value), 
                              float(txt_add_product_price.value), 
                              int(txt_add_product_quantity.value),
                              float(txt_add_product_cost_price.value),
                              str(txt_add_product_brand.value),
                              str(txt_add_product_category.value),
                              str(txt_add_product_colour.value))
            manager.add_product(product)
            manager.save_products_to_file()
            
            # Also add it to the datatable:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f"{len(data_table_products.rows)}"), visible=False),  # 0 - based rowid
                    ft.DataCell(ft.Text(f"{product.id}")),
                    ft.DataCell(ft.Text(f"{product.name}")),
                    ft.DataCell(ft.Text(f"{product.price}")),
                    ft.DataCell(ft.Text(f"{product.cost_price}")),
                    ft.DataCell(ft.Text(f"{product.quantity}")),
                    ft.DataCell(ft.Text(f"{product.brand}")),
                    ft.DataCell(ft.Text(f"{product.category}")),
                    ft.DataCell(ft.Text(f"{product.colour}"))
                ], on_select_changed=lambda e: change_product_selection(e, int(e.control.data))
                , data=product.id  # primary key (get via e.control.data)
            )
            data_table_products.rows.append(row)
            
            # Clear fields again
            clear_addedit_controls()
            row_addedit_controls.visible = False
            btn_cancel.visible = False
        page.update()
    
    def change_product_selection(e, product_id):

        # Show the Edit/Delete buttons:
        btn_save.visible = True
        btn_delete.visible = True
        btn_add.visible = False
        btn_cancel.visible = True
        
        # Load the add/edit fields with the selected item's values:
        row_addedit_controls.visible = True
        product = manager.products[product_id]
        lbl_product_id.value = product_id
        lbl_datagrid_row_nr.value = e.control.cells[0].content.value  # get row index from our first column
        txt_add_product_name.value = product.name
        txt_add_product_price.value = f"{product.price:.2f}"
        txt_add_product_quantity.value = str(product.quantity)
        txt_add_product_cost_price.value = f"{product.cost_price:.2f}"
        txt_add_product_brand.value = product.brand
        txt_add_product_category.value = product.category
        txt_add_product_colour.value = product.colour

        page.update()
 
    def save_product(e):
        # first do a validation of the fields
        if not validate_add_product_fields():
            # validation failed, so tell the user and then abandon the adding
            page.open(ft.AlertDialog(title=ft.Text("Invalid values!", text_align="center"), actions_padding=0,title_padding=5))
            return
        
        # update the products
        product = Product(int(lbl_product_id.value), 
                          str(txt_add_product_name.value),
                          float(txt_add_product_price.value),
                          int(txt_add_product_quantity.value),
                          float(txt_add_product_cost_price.value),
                          str(txt_add_product_brand.value),
                          str(txt_add_product_category.value),
                          str(txt_add_product_colour.value)
                          )
        manager.add_product(product)
        manager.save_products_to_file()
        
        # update the grid
        row_nr = int(lbl_datagrid_row_nr.value)
        data_table_products.rows[row_nr].cells[2].content = ft.Text(f"{txt_add_product_name.value}")
        data_table_products.rows[row_nr].cells[3].content = ft.Text(f"{txt_add_product_price.value}")
        data_table_products.rows[row_nr].cells[4].content = ft.Text(f"{txt_add_product_cost_price.value}")
        data_table_products.rows[row_nr].cells[5].content = ft.Text(f"{txt_add_product_quantity.value}")
        data_table_products.rows[row_nr].cells[6].content = ft.Text(f"{txt_add_product_brand.value}")
        data_table_products.rows[row_nr].cells[7].content = ft.Text(f"{txt_add_product_category.value}")
        data_table_products.rows[row_nr].cells[8].content = ft.Text(f"{txt_add_product_colour.value}")
        
        # Clear fields again
        clear_addedit_controls()
        row_addedit_controls.visible = False
        btn_cancel.visible = False
        btn_delete.visible = False
        btn_add.visible = True
        btn_save.visible = False
        
        page.update()

    def cancel(e):
        """Cancels the current edit/add"""
        # clear the fields
        clear_addedit_controls()
        
        # show/hide the controls
        row_addedit_controls.visible = False
        btn_add.visible = True
        btn_save.visible = False
        btn_delete.visible = False
        btn_cancel.visible = False
        
        page.update()

    def delete_product(e):
        # Delete from dictionary
        manager.products.pop(int(lbl_product_id.value))
        manager.save_products_to_file()
        
        # Delete the row:
        print(f"Deleting product with id = {lbl_product_id.value}")
        del data_table_products.rows[int(lbl_datagrid_row_nr.value)]     # get row index from our invisible first column
 
        # Clear the fields
        clear_addedit_controls()
        
        # Hide the controls
        row_addedit_controls.visible = False
        btn_cancel.visible = False
        btn_delete.visible = False
        btn_save.visible = False
        btn_add.visible = True
 
		# THEN SHOW SNACK BAR for info
        page.snack_bar = ft.SnackBar(
			ft.Text(f"Successfuly deleted product with id  = {lbl_product_id.value}",color="white"),
			bgcolor="red",
			)
        page.snack_bar.open = True
        page.update()
  
    def search_product(e):
        """Filters the data table with the entered search"""
        search_text = txt_search.value.lower()
		
        for row in data_table_products.rows:
            if not (
                search_text in str(row.cells[1].content.value).lower()  # id
                or
                search_text in str(row.cells[2].content.value).lower()  # name
                or
                search_text in str(row.cells[6].content.value).lower()  # brand
                or
                search_text in str(row.cells[7].content.value).lower()  # category
                or
                search_text in str(row.cells[8].content.value).lower()  # colour
            ):
                row.visible = False
            else:
                row.visible = True
                
  
        page.update()
  
    #endregion
    
    #region CONTROL DEFINITIONS
    
    # LBL_HEADER
    lbl_header = ft.Text("Inventory Manager", size=50)
    
    # ROW_ADD_CONTROLS
    #region ROW_ADD_CONTROLS
    lbl_product_id = ft.Text("", visible=False)
    lbl_datagrid_row_nr = ft.Text("", visible=False)  #to make updates in the grid easier
    txt_add_product_name = ft.TextField(label="Name", height=45, width=200)
    txt_add_product_price = ft.TextField(label="Price", height=45, width=100, keyboard_type=ft.KeyboardType.NUMBER)  # set default keyboard for mobile and for validation checks later on
    txt_add_product_cost_price = ft.TextField(label="Cost Price", height=45, width=100, keyboard_type=ft.KeyboardType.NUMBER)  # set default keyboard for mobile and for validation checks later on
    txt_add_product_quantity = ft.TextField(label="Quantity", height=45, width=100, keyboard_type=ft.KeyboardType.NUMBER)  # set default keyboard for mobile and for validation checks later on
    txt_add_product_brand = ft.TextField(label="Brand", height=45, width=200)
    txt_add_product_category = ft.TextField(label="Category", height=45, width=200)
    txt_add_product_colour = ft.TextField(label="Colour", height=45, width=200, on_submit=submit_changes)
    
    row_addedit_controls = ft.Row(
        controls=[
            txt_add_product_name,
            txt_add_product_price,
            txt_add_product_cost_price,
            txt_add_product_quantity,
            txt_add_product_brand,
            txt_add_product_category,
            txt_add_product_colour]
        ,visible=False  # Will display when "Add" is clicked
        ,alignment="center"
    )
    #endregion ROW_ADD_CONTROLS
    
    # BTN_ADD
    btn_add =  ft.ElevatedButton("Add",
		bgcolor="blue",
		color="white",
		on_click=add_product
		)
    
    # BTN_DELETE
    btn_delete = ft.ElevatedButton("Delete",
		bgcolor="red",
		color="white",
		on_click=delete_product,
        visible=False  # will be revealed when we click a row
		)
 
	# BTN_SAVE
    btn_save = ft.ElevatedButton("Save",
		bgcolor="green",
		color="white",
		on_click=save_product,
        visible=False  # will be revealed when we click a row
		)
    
    # BTN_CANCEL
    btn_cancel = ft.ElevatedButton("Cancel",
		bgcolor="orange",
		color="white",
		on_click=cancel,
        visible=False  # will be revealed when we click a row
		)
    
    # TXT_SEARCH
    txt_search = ft.TextField(label="Search", height=45, width=200,
                              on_change=search_product)
    
    # DATA_TABLE_PRODUCTS
    data_table_products: ft.DataTable
    #region build DATA_TABLE_PRODUCTS
    # build list of data rows with each product per row:
    data_rows = []
    # load all entries into datarows
    for prod in manager.products.values():
        row = ft.DataRow(
            cells=[
                ft.DataCell(ft.Text(f"{len(data_rows)}"), visible=False),  # 0 - based rowid
                ft.DataCell(ft.Text(f"{prod.id}")),
                ft.DataCell(ft.Text(f"{prod.name}")),
                ft.DataCell(ft.Text(f"{prod.price}")),
                ft.DataCell(ft.Text(f"{prod.cost_price}")),
                ft.DataCell(ft.Text(f"{prod.quantity}")),
                ft.DataCell(ft.Text(f"{prod.brand}")),
                ft.DataCell(ft.Text(f"{prod.category}")),
                ft.DataCell(ft.Text(f"{prod.colour}"))
            ], on_select_changed=lambda e: change_product_selection(e, int(e.control.data))
            , data=prod.id  # primary key (get via e.control.data)
        )
        data_rows.append(row)
    # generate headers and add them and the datarows into our datatable
    data_table_products = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("RowNr"), numeric=True, visible=False),
            ft.DataColumn(ft.Text("ID"), numeric=True),
            ft.DataColumn(ft.Text("Name")),
            ft.DataColumn(ft.Text("Price"), numeric=True),
            ft.DataColumn(ft.Text("Cost Price"), numeric=True),
            ft.DataColumn(ft.Text("Quantity"), numeric=True),
            ft.DataColumn(ft.Text("Brand")),
            ft.DataColumn(ft.Text("Category")),
            ft.DataColumn(ft.Text("Colour"))
        ],
        rows=data_rows
    )
    #endregion build DATA_TABLE_PRODUCTS
    
    #endregion
    
    page.add(
        ft.Row([lbl_header], alignment="center"),
        row_addedit_controls,
        ft.Row([btn_add, btn_save, btn_delete, btn_cancel], alignment="center"),
        ft.Row([txt_search], alignment="center"),
        ft.Row([data_table_products], alignment="center")  # row entries must be iterable
    )
    
def page_initialisation(page: ft.Page):
    """Sets the basic screen properties"""
    page.title = "Inventory Manager"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

ft.app(main)