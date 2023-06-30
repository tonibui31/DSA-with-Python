from Class import *
from Operations import *
'''
BẢNG ĐIỀU KHIỂN CHÍNH
'''
class ASM3_Main():
    def run(self):
        while True:
            print("\n   Employee Management System - Python   ")
            print("              Person Tree                \n")
            print("******************MENU*********************\n")
            print("**  1. Load the data from the file       **")
            print("**  2. Insert a new Person               **")
            print("**  3. Inorder Traversal                 **")
            print("**  4. Breadth-First Traversal           **")
            print("**  5. Search by Person ID               **")
            print("**  6. Delete by Person ID               **")
            print("**  0. Exit                              **")
            print("\n*******************************************")
            print("**  Enter desired option:                **\n")
            print("**  Please always enter 1 (loading file) first, then do other tasks later:     **")

            key = input("Nhập tùy chọn: ")

            if (key == '1'):
                print('\nChoice 1: Load the data from the file...')
                OperationsToEmployee.load_data_from_file_and_display(self)
            elif (key == '2'):
                print('\nChoice 2: Insert a new Person...\n')
                OperationsToEmployee.insert_a_new_person(self)
            elif (key == '3'):
                print("\nChoice 3: Inorder Traversal...\n")
                OperationsToEmployee.inorder_traversal(self)
            elif (key == '4'):
                print('\nChoice 4: Breadth-First Traversal...\n')
                OperationsToEmployee.breadth_first_traversal(self)
            elif (key == '5'):
                print('\nChoice 5: Search by Person ID...\n')
                OperationsToEmployee.search_by_person_id(self)
            elif (key == '6'):
                print('\nChoice 6: Delete by Person ID...\n')
                OperationsToEmployee.delete_by_person_id(self)
            elif (key == '0'):
                print("\nThanks!!!")
                break
            else:
                print("\nKhông có chức năng này!")
                print("\nHãy chọn chức năng trong hộp menu (nhập số từ 1 -> 6).")
        
if __name__ == "__main__":
    ASM3_Main().run()