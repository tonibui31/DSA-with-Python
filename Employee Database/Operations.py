from Class import *
'''
CÁC CHỨC NĂNG YÊU CẦU ĐỀ BÀI
'''
DICT_EMPLOYEES = {}
employee_bst = BinarySearchTree()
class OperationsToEmployee():
    def load_data_from_file_and_display(self):
        try:
            with open("Employee.txt", "r") as file:
                content = file.read()
                if not content:
                    print("File is empty. Please add information.")
                    return None

                employees = eval(content) # Turn string back to dictionary

                for key in employees:
                    # Loop through each dictionary inside DICT_EMPLOYEES
                    employee = employees[key]
                    
                    # Asign data from text file to variables
                    employee_id = employee['employee_id']
                    employee_name = employee['employee_name']
                    employee_birthday = employee['employee_birthday']
                    employee_birthplace = employee['employee_birthplace']
                    
                    # Put all variables into class object
                    one_employee = Employee(employee_id, employee_name, employee_birthday, employee_birthplace)
                    
                    # Append object to employee_bst
                    employee_bst.insert(one_employee)
                    
                return employee_bst
                    
        except FileNotFoundError:
            print('File not yet exists, please enter 2 to create new file and add new information')
            
    def insert_a_new_person(self):
        # Employee Input
        employee_id = input('Please enter new employee ID: ... ')
        while employee_id in DICT_EMPLOYEES:
            print('The employee ID is already in the dictionary.')
            employee_id = input('Please enter a different employee ID: ... ')
            
        employee_name = input("Please enter new employee's name: ... ")
        employee_birthday = input("Please enter new employee's birthday (e.g: 25/09/98 ): ... ")
        employee_birthplace = input("Please enter new employee's birthplace: ... ")
        
        # Turn class object into dictionary, then save in txt file
        one_employee = Employee(employee_id, employee_name, employee_birthday, employee_birthplace)
        DICT_EMPLOYEES[employee_id] = one_employee.__dict__ 
        
        if os.path.isfile('Employee.txt') and os.path.getsize('Employee.txt') > 0:
            with open('Employee.txt', 'r') as infile:
                data = json.load(infile)
            data.update(DICT_EMPLOYEES)
            with open('Employee.txt', 'w') as outfile:
                json.dump(data, outfile, indent=2)
        else: # if file not exists or there is no infile
            with open('Employee.txt', 'w') as outfile:
                json.dump(DICT_EMPLOYEES, outfile, indent=2)

        # Append object to employee_bst
        employee_bst.insert(one_employee)
            
    def inorder_traversal(self):
        print("{:<5} | {:<7} | {:<12} | {}".format("ID", "Name", "Day of Birth", "Birthplace"))
        return employee_bst.traverse_inorder()
    
    def breadth_first_traversal(self):
        print("{:<5} | {:<7} | {:<12} | {}".format("ID", "Name", "Day of Birth", "Birthplace"))
        return employee_bst.traverse_breadth_first()
    
    def search_by_person_id(self):
        employee_id_to_search = input('Please enter the employee ID: ... ')
        searched = employee_bst.search(employee_id_to_search)
        
        if searched:
            print("{:<5} | {:<7} | {:<12} | {}".format("ID", "Name", "Quantity", "Price"))
            print("{:<5} | {:<7} | {:<12} | {}".format(searched.employee_id, searched.employee_name, searched.employee_birthday, searched.employee_birthplace))
        else:
            print('The searched ID is not valid')
            
    def delete_by_person_id(self):
        employee_id_to_be_deleted = input('Please enter the employee ID: ... ')

        # Delete employee from BST
        employee_bst.delete(employee_id_to_be_deleted)
        
        with open('Employee.txt', 'r') as file:
            content = file.read()
            data = json.loads(content)
            
        # Get information of the employee to be deleted
        employee_to_be_deleted = data.get(employee_id_to_be_deleted)

        # Delete chosen product_id from Employee.txt
        if employee_id_to_be_deleted in data:
            del data[employee_id_to_be_deleted]
            with open('Employee.txt', 'w') as file:
                json.dump(data, file, indent=2)

        # Print the deleted employee
        if employee_to_be_deleted:
            print("{:<5} | {:<7} | {:<12} | {}".format("ID", "Name", "Birthday", "Birthplace"))
            print("{:<5} | {:<7} | {:<12} | {}".format(employee_to_be_deleted["employee_id"], employee_to_be_deleted["employee_name"], employee_to_be_deleted["employee_birthday"], employee_to_be_deleted["employee_birthplace"]))
            print('This employee is removed from the dataset successfully!')
        else:
            print('The searched ID is not valid')

