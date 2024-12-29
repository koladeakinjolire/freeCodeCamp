def merge_sort(array):
    if len(array) <= 1:
        return
    
    middle_point = len(array) // 2 # absolute middle of array
    left_part = array[:middle_point] #split from index 0 to middle index(skips middle index)
    right_part = array[middle_point:] #split from middle index to last 

    merge_sort(left_part) #recursion on left side array
    merge_sort(right_part) #recursion on right side array

    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    while left_array_index < len(left_part) and right_array_index < len(right_part): #check if the length of the left and right side arrays are greater than 0
        if left_part[left_array_index] < right_part[right_array_index]: # if the first item of the left array is greater than the first item in the right array
            array[sorted_index] = left_part[left_array_index] #add item to the first index of sorted version of array 
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
            
        sorted_index += 1

    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
