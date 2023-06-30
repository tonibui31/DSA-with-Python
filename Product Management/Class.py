class Product:
    def __init__(self, product_id, product_name, product_quantity, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_quantity = product_quantity
        self.product_price = product_price
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
'''
{
    "value": value,
    "next": None
}

'''
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        temp = self.head
        while temp is not None:
            print("{:<5} | {:<10} | {:<10} | {}".format(temp.value.product_id, temp.value.product_name, temp.value.product_quantity, temp.value.product_price))
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def search(self, key):
        current = self.head # Store head node
        while current is not None:
            
            if current.value.product_id == key:
                return current.value
            current = current.next
            
        return False # if key was not present in linked list        
    
    def deleteNode(self, key):
        current_node = self.head
        previous_node = None

        while current_node:
            
            if current_node.value.product_id == key:
                if previous_node: 
                    previous_node.next = current_node.next
                else: # current_node is head node of LinkedList
                    self.head = current_node.next
                    
                deleted_node = current_node # saved deleted node before deleting it
                current_node = None
                return deleted_node.value
            
            else: # current_node.value.product_id != key
                previous_node = current_node
                current_node = current_node.next
                
        return None # no node found