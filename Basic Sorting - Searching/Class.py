def manual_input():
    # Enter the array
    n = int(input("Please enter input number of elements: ... ")) 
    a = input("Please enter {} elements, spaced: ... ".format(n)).split()
    array = [int(ai) for ai in a]

    # Displaying the array
    print('Initial array: ', array)
    file = open("INPUT.txt", "w+")
    
    # Saving the array in a text file
    content = ' '.join(str(e) for e in array)
    file.write(content)
    file.close()
    
def file_input():
    # Displaying the contents of the text file
    file = open("INPUT.txt", "r")
    content = file.read()

    # Displaying the array
    print("Content in INPUT.txt: ", content, '\n')
    file.close()
    
    return content

def bubbleSort(array):
    # Take list of string from the INPUT.txt file, turn it into string of integers
    array = array.split(' ')
    array = [int(i) for i in array]
    
    # Loop through each element of array:
    for i in range(len(array)):
        print('Begining of step', i, array)
        
        # Keep track of swapping
        swapped = False
        
        # Loop to compare array elements:
        for j in range(0, len(array) - i - 1):
            
            # compare two adjacent elements
            if array[j] > array[j + 1]:
                
                # swapping occurs if elements are not in the intented order
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                print('Swapping: ...', array, '\n')
                
        if not swapped:
            break
                
    print('Final Bubble Sort: ', array)
    
    # Saving the array in a text file
    file = open("OUTPUT1.txt", "w+")
    content = ' '.join(str(e) for e in array)
    file.write(content)
    file.close()
    
def selectionSort(array):
    # Take list of string from the INPUT.txt file, turn it into string of integers
    array = array.split(' ')
    array = [int(i) for i in array]
    
    for step in range(len(array)):
        min_index = step
        print('Begining of step', step, array)
        
        for i in range(step + 1, len(array)):
            # select the minium element in each loop
            if array[i] < array[min_index]:
                min_index = i
        
        # put min at the correct position
        array[step], array[min_index] = array[min_index], array[step]
        print('Swapping: ...', array, '\n')
        
    print('Final Selection Sort: ', array)

    # Saving the array in a text file
    file = open("OUTPUT2.txt", "w+")
    content = ' '.join(str(e) for e in array)
    file.write(content)
    file.close()
    
def insertionSort(array):
    # Take list of string from the INPUT.txt file, turn it into string of integers
    array = array.split(' ')
    array = [int(i) for i in array]
    
    for step in range(1, len(array)):
        key = array[step] # assuming the first element is sorted, the second element will be key
        j = step - 1
        print('Begining of step', step, array, '\n')
        
        # Compare key with each element on the left of it until an element smaller than it is found
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            print('Swapping: ...', array, 'key: ', key, '\n')
        
        # Place key at after the element just smaller than it
        array[j + 1] = key
        print('End of step', step, array, '\n')
    
    print('Final Insertion Sort: ', array)

    # Saving the array in a text file
    file = open("OUTPUT3.txt", "w+")
    content = ' '.join(str(e) for e in array)
    file.write(content)
    file.close()
    
def linearSearch(array):
    # Take list of string from the INPUT.txt file, turn it into string of integers
    array = array.split(' ')
    array = [int(i) for i in array]
    
    value = int(input('Please enter searched input value: ... '))
    
    # List comprehension
    result = [x for x in array if x > value]
    result = sorted(result)
    print('\nAll elements in array that greater than input value: ', result)
    
    # Saving the array in a text file
    file = open("OUTPUT4.txt", "w+")
    content = ' '.join(str(e) for e in result)
    file.write(content)
    file.close()
    
def binarySearch(array):
    # Take list of string from the INPUT.txt file, turn it into string of integers
    array = array.split(' ')
    array = [int(i) for i in array]
    array = sorted(array)
    print('Sorted array: ', array)
    
    x = int(input('Please enter searched input value: ... '))
    
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = low + (high- low) // 2
        
        if array[mid] == x:
            return mid
        
        elif array[mid] < x:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return -1