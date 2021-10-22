def binary_search(input_array, value):
    """Your code goes here."""
    input_array = sorted(input_array)
    # set the hgh and low pointer 
    low_poiter = 0
    high_pointer = len(input_array) 
    if input_array[0] > value or input_array[-1] < value:
        return -1
    else: 
        while low_poiter <= high_pointer:
            mid = (low_poiter + high_pointer)//2
            if input_array[mid] == value:
                return mid
            elif input_array[mid] < value:
                low_poiter = mid +1
            else: 
                high_pointer = mid -1
        return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))