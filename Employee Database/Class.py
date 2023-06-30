import json
import os.path
from collections import deque

'''
HỒ SƠ NHÂN VIÊN & QUẢN LÍ THÔNG TIN
'''
class Employee:
    def __init__(self, employee_id, employee_name, employee_birthday, employee_birthplace):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_birthday = employee_birthday
        self.employee_birthplace = employee_birthplace

class Node:
    def __init__(self, employee):
        self.employee = employee
        self.left = None
        self.right = None
'''
CÂY NHỊ PHÂN TÌM KIẾM & CÁC CHỨC NĂNG CƠ BẢN
'''        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, employee):
        if self.root is None:
            self.root = Node(employee)
            return
        
        current_node = self.root
        
        while True:
            if employee.employee_id < current_node.employee.employee_id:
                if current_node.left is None:
                    current_node.left = Node(employee)
                    break
                current_node = current_node.left
            elif employee.employee_id > current_node.employee.employee_id:
                if current_node.right is None:
                    current_node.right = Node(employee)
                    break
                current_node = current_node.right
            else:
                # the employee with the same id already exists
                break

    def search(self, employee_id):
        current_node = self.root
        
        while current_node is not None:
            if current_node.employee.employee_id == employee_id:
                return current_node.employee
            elif employee_id < current_node.employee.employee_id:
                current_node = current_node.left
            else:
                current_node = current_node.right
                
        return None
    
    def delete(self, employee_id):
        # Initialize deleted_node as None
        deleted_node = None
        
        # If the root is None, return deleted_node
        if self.root is None:
            return deleted_node

        # Initialize parent_node as None and current_node as the root
        parent_node = None
        current_node = self.root
        
        # Traverse the BST to find the node with the given employee_id
        while current_node is not None:

            # If the current node has the given employee_id, set deleted_node to the current node and delete it
            if employee_id == current_node.employee.employee_id:
                deleted_node = current_node

                # If the current node has no children (leaf node), simply remove it
                if current_node.left is None and current_node.right is None:
                    if parent_node is None:
                        self.root = None
                    elif current_node == parent_node.left:
                        parent_node.left = None
                    else:
                        parent_node.right = None

                # If the current node has one child, replace it with that child
                elif current_node.left is None:
                    if parent_node is None:
                        self.root = current_node.right
                    elif current_node == parent_node.left:
                        parent_node.left = current_node.right
                    else:
                        parent_node.right = current_node.right

                elif current_node.right is None:
                    if parent_node is None:
                        self.root = current_node.left
                    elif current_node == parent_node.left:
                        parent_node.left = current_node.left
                    else:
                        parent_node.right = current_node.left

                # If the current node has two children, find the minimum node in the right subtree, replace the current node with it, and delete the minimum node
                else:
                    min_node = current_node.right
                    while min_node.left is not None:
                        min_node = min_node.left

                    current_node.employee = min_node.employee
                    employee_id = min_node.employee.employee_id
                    deleted_node = min_node
                    parent_node = current_node
                    current_node = current_node.right
                # Exit the loop
                break

            # If the given employee_id is less than the current node's employee_id, move to the left child
            elif employee_id < current_node.employee.employee_id:
                parent_node = current_node
                current_node = current_node.left

            # If the given employee_id is greater than the current node's employee_id, move to the right child
            else:
                parent_node = current_node
                current_node = current_node.right

        # Return the deleted employee or None if the employee was not found
        return deleted_node.employee if deleted_node else None
    
    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, current_node):
        if current_node is None:
            return 0
        else:
            left_height = self._get_height(current_node.left)
            right_height = self._get_height(current_node.right)
            return max(left_height, right_height) + 1

    def count_nodes(self):
        return self._count_nodes(self.root)

    def _count_nodes(self, current_node):
        if current_node is None:
            return 0
        else:
            left_count = self._count_nodes(current_node.left)
            right_count = self._count_nodes(current_node.right)
            return left_count + right_count + 1
        
    '''
    Duyệt theo chiều sâu (depth-first traversal)
    và duyệt theo chiều rộng (breadth-first traversal)
    '''
    def traverse_inorder(self):
        self._traverse_inorder(self.root)

    def _traverse_inorder(self, current_node):
        if current_node is not None:
            self._traverse_inorder(current_node.left)
            print("{:<5} | {:<7} | {:<12} | {}".format(current_node.employee.employee_id, current_node.employee.employee_name, current_node.employee.employee_birthday, current_node.employee.employee_birthplace))
            self._traverse_inorder(current_node.right)
            
    def traverse_breadth_first(self):
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            print("{:<5} | {:<7} | {:<12} | {}".format(current_node.employee.employee_id, current_node.employee.employee_name, current_node.employee.employee_birthday, current_node.employee.employee_birthplace))
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
                
    