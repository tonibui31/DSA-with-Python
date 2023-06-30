from Operations import *

class ASM2_Main():
    def run(self):
        while True:
            print("\n   Product Management System - Python    ")
            print("******************MENU*********************\n")
            print("**  1. Load data from file and display   **")
            print("**  2. Input & add to the end            **")
            print("**  3. Display data                      **")
            print("**  4. Save product list to file         **")
            print("**  5. Search by ID                      **")
            print("**  6. Delete by ID                      **")
            print("**  7. Sort by ID                        **")
            print("**  8. Convert to Binary                 **")
            print("**  9. Load to stack and display         **")
            print("**  10. Load to queue and display        **")
            print("**  0. Exit.                             **")
            print("\n*******************************************")
            print("**  Enter desired option:                **\n")
            print("**  Please always enter 1 first, and after updating Data.txt:     **")
            print("**  If use 6, please remember to enter 4 afterwards to save new data to Outdata.txt   **\n")

            key = input("Nhập tùy chọn: ")

            if (key == '1'):
                print('\nChoice 1: Load data from file and display...')
                OperationToProduct.load_data_from_file_and_display(self)
                print('\nProduct loaded successfully, please proceed to other option(s)')
            elif (key == '2'):
                print('\nChoice 2: Input & add to the end...\n')
                OperationToProduct.input_and_add_to_the_end(self)
                print('\nProduct entered successfully, then saved to Data.txt')
            elif (key == '3'):
                print("\nChoice 3: Display data...\n")
                OperationToProduct.display_data(self)
            elif (key == '4'):
                print('\nChoice 4: Save product list to file...\n')
                OperationToProduct.save_product_list_to_file(self)
                print('\nProduct list saved to Outdata.txt')
            elif (key == '5'):
                print('\nChoice 5: Search by ID...\n')
                OperationToProduct.search_by_id(self)
            elif (key == '6'):
                print('\nChoice 6: Delete by ID...\n')
                OperationToProduct.delete_by_id(self)
            elif (key == '7'):
                print('\nChoice 7: Sort by ID...\n')
                OperationToProduct.sorted_by_id(self)
            elif (key == '8'):
                print('\nChoice 8: Convert to Binary...\n')
                OperationToProduct.convert_quantity_to_binary(self)
            elif (key == '9'):
                print('\nChoice 9: Load to stack and display...\n')
                OperationToProduct.load_to_stack_and_display(self)
            elif (key == '10'):
                print('\nChoice 10: Load to queue and display...\n')
                OperationToProduct.load_to_queue_and_display(self)
            elif (key == '0'):
                print("\nThanks!!!")
                break
            else:
                print("\nKhông có chức năng này!")
                print("\nHãy chọn chức năng trong hộp menu (nhập số từ 1 -> 10).")
        
if __name__ == "__main__":
    ASM2_Main().run()