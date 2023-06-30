from Class import *

# MENU TRÊN CONSOLE
while True:
    print("\nChương trình sắp xếp và tìm kiếm dữ liệu Python")
    print("******************MENU*******************\n")
    print("**  1. Manual Input.                   **")
    print("**  2. File input.                     **")
    print("**  3. Bubble sort.                    **")
    print("**  4. Selection sort.                 **")
    print("**  5. Insertion sort.                 **")
    print("**  6. Linear Search (Search > Value). **")
    print("**  7. Binary Search (Search = Value). **")
    print("**  0. Exit.                           **")
    print("\n*****************************************")
    print("**  Mời bạn nhập chức năng mong muốn:  **\n")
     
    key = int(input("Nhập tùy chọn: "))
    
    if (key == 1):
        print('\nChoice 1: Manual Input...\n')
        manual_input()
    elif (key == 2):
        print('\nChoice 2: File input...\n')
        file_input()
    elif (key == 3):
        print("\nChoice 3: Bubble sort...\n")
        bubbleSort(file_input())
    elif (key == 4):
        print('\nChoice 4: Selection sort...\n')
        selectionSort(file_input())
    elif (key == 5):
        print('\nChoice 5: Insertion sort...\n')
        insertionSort(file_input())
    elif (key == 6):
        print('\nChoice 6: Linear Search...\n')
        linearSearch(file_input())
    elif (key == 7):
        print('\nChoice 7: Binary Search...\n')
        result = binarySearch(file_input())
        if result != -1:
            print("Element is present at index " + str(result))
        else:
            print("Not found")
    elif (key == 0):
        print("\nThanks!!!")
        break
    else:
        print("\nKhông có chức năng này!")
        print("\nHãy chọn chức năng trong hộp menu.")