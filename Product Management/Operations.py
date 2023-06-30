import json
from queue import Queue
import os.path
from Class import *

DICT_PRODUCTS = {}
products_llist = LinkedList()
class OperationToProduct(): 
    def load_data_from_file_and_display(self):
        try:
            with open("Data.txt", "r") as file:
                content = file.read()
                if not content:
                    print("File is empty. Please add information.")
                    return None
                products = eval(content) # Turn string back to dictionary

                for key in products:
                    # Loop through each dictionary inside DICT_PRODUCTS
                    product = products[key] 
                    
                    # Asign data from text file to variables
                    product_id = product['product_id']
                    product_name = product['product_name']
                    product_quantity = product['product_quantity']
                    product_price = product['product_price']
                    
                    # Put all variables into class object
                    one_product = Product(product_id, product_name, product_quantity, product_price)
                    
                    # Append object to products_llist
                    products_llist.append(one_product)
                    
                # products_llist.print_list()
                return products_llist
                    
        except FileNotFoundError:
            print('File not yet exists, please enter 2 to create new file and add new information')
            
    def input_and_add_to_the_end(self):
        # Product Input
        product_id = input('Please enter the new product ID: ... ')
        product_name = input("Please enter the product's name: ... ")
        product_quantity = int(input("Please enter the product's quantity: ... "))
        product_price = float(input("Please enter the product's price: ... "))
        
        # Turn class object into dictionary, then save in txt file
        one_product = Product(product_id, product_name, product_quantity, product_price)
        DICT_PRODUCTS[product_id] = one_product.__dict__ 
        
        if os.path.isfile('Data.txt') and os.path.getsize('Data.txt') > 0:
            with open('Data.txt', 'r') as infile:
                data = json.load(infile)
            data.update(DICT_PRODUCTS)
            with open('Data.txt', 'w') as outfile:
                json.dump(data, outfile, indent=2)
        else:
            with open('Data.txt', 'w') as outfile:
                json.dump(DICT_PRODUCTS, outfile, indent=2)

        # Append object to products_llist
        products_llist.append(one_product)
        
    def display_data(self):
        print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
        return products_llist.print_list()
    
    def save_product_list_to_file(self):
        temp = products_llist.head
        with open('Outdata.txt', 'w') as outfile:
            while temp is not None:
                outfile.writelines([temp.value.product_id, ' | ', temp.value.product_name, ' | ', str(temp.value.product_quantity), ' | ', str(temp.value.product_price), '\n'])
                temp = temp.next
                
    def search_by_id(self):
        product_id_to_search = input('Please enter the ID: ... ')
        searched = products_llist.search(product_id_to_search)
        
        if searched:
            print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
            print("{:<5} | {:<10} | {:<10} | {}".format(searched.product_id, searched.product_name, searched.product_quantity, searched.product_price))
        else:
            print('ID is not in the dataset!')
        
    def delete_by_id(self):
        product_id_to_be_deleted = input('Please enter the ID: ... ')
        
        with open('Data.txt', 'r') as file:
            content = file.read()
            data = json.loads(content)

        # Get information of the employee to be deleted
        product_to_be_deleted = data.get(product_id_to_be_deleted)

        # Delete chosen product_id from Data.txt
        if product_id_to_be_deleted in data:
            del data[product_id_to_be_deleted]
            with open('Data.txt', 'w') as file:
                json.dump(data, file, indent=2)
                
        products_llist.deleteNode(product_id_to_be_deleted)
        
        if product_to_be_deleted:
            print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
            print("{:<5} | {:<10} | {:<10} | {}".format(product_to_be_deleted["product_id"], product_to_be_deleted["product_name"], product_to_be_deleted["product_quantity"], product_to_be_deleted["product_price"]))
            print('This product is removed from the dataset successfully!')
        else:
            print('ID is not in the dataset!')
            
    def sorted_by_id(self):
        with open('Data.txt', 'r') as file:
            content = file.read()
            data = json.loads(content)

        sorted_data = dict(sorted(data.items()))
        products = [] # an empty list products that will hold the Product objects that will be created
        
        # loops through each key in data and assigns the value for that key to product_data.
        for key in sorted_data: 
            product_data = sorted_data[key]
            
            # creates a Product object using the ** syntax to pass the product_data dictionary as keyword arguments.
            product = Product(**product_data)
            
            # adds the Product object to the products list.
            products.append(product)
            
        print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
        for product in products:
            print("{:<5} | {:<10} | {:<10} | {}".format(product.product_id, product.product_name, product.product_quantity, product.product_price))
        
        
    def convert_quantity_to_binary(self):
        product_id_to_search = input('Please enter the ID: ... ')
        searched = products_llist.search(product_id_to_search)
        
        if searched:
            print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
            print("{:<5} | {:<10} | {:<10} | {}".format(searched.product_id, searched.product_name, searched.product_quantity, searched.product_price))
            print('Convert quantity to binary:', int(bin(searched.product_quantity)[2:]))
        else:
            print('ID is not in the dataset!')
            
    def load_to_stack_and_display(self):
        with open('Data.txt', 'r') as file:
            content = file.read()
            data = json.loads(content)

        data = dict(data.items()) 
        products = [] # an empty list products that will hold the Product objects that will be created
        
        # loops through each key in data and assigns the value for that key to product_data.
        for key in data: 
            product_data = data[key]
            
            # creates a Product object using the ** syntax to pass the product_data dictionary as keyword arguments.
            product = Product(**product_data)
            
            # adds the Product object to the products list.
            products.append(product)
            
        print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
        for product in reversed(products):
            print("{:<5} | {:<10} | {:<10} | {}".format(product.product_id, product.product_name, product.product_quantity, product.product_price))
        
    def load_to_queue_and_display(self):
        with open('Data.txt', 'r') as file:
            content = file.read()
            data = json.loads(content)

        # Load data into a queue
        queue = Queue()
        for key, value in data.items():
            queue.put(value)
            
        # Print queue in the desired format
        print("{:<5} | {:<10} | {:<10} | {}".format("ID", "Name", "Quantity", "Price"))
        while not queue.empty():
            item = queue.get()
            print("{:<5} | {:<10} | {:<10} | {}".format(item["product_id"], item["product_name"], item["product_quantity"], item["product_price"]))
            