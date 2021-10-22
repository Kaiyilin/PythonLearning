"""
Sorting: change the postion of the array
you can definitely using Brute Force! 
But, you should always consider is there any clever way!
"""
class Sorting():
    def __init__(self, array) -> None:
        super().__init__()
        self.array = array
    def insertionSort(self):
        length = len(self.array)
        sorted_array = self.array.copy()
        for i in range(1, length):
            currentPointer = sorted_array[i]

            #comparison started with previous one
            j = i - 1
            #print(f"Current i = {i}")
            #print(f"Current j = {j}")
            print(f"Current pointer {currentPointer}")

            # while the compaarison is not ended
            # and the value of current pointer is smaller
            # than the previous one, do swap.
            while j>=0 and currentPointer < sorted_array[j]:
                sorted_array[j+1] = sorted_array[j]
                j-=1
                print(f"Inside while{sorted_array}")
                print(f"After processed j = {j}")
            sorted_array[j+1] = currentPointer
            print(f"Origin: {self.array}")
            print(f"Sorted: {sorted_array}\n")

        return sorted_array


    def binaryInsertionSort(self):

        def binarySearch(array, value, start, end):
            # to get insert position
            if start == end:
                if array[start] > value:
                    return start
                else: 
                    return start+1

            if start > end:
                return start  

            mid = (start+end)//2
            if array[mid] > value:
                # search the l't branch
                return binarySearch(array, value, start, mid-1)
            elif array[mid] < value:
                # search the r't branch
                return binarySearch(array, value, mid+1, end)
            else: 
                print(f"insert position: {mid}\n")
                return mid

        length = len(self.array)
        for i in range(1, length):
            value = self.array[i]
            #find insert position
            insertPosition = binarySearch(self.array, value, 0, i-1)
            print(f"The insert Position for {value} is {insertPosition+1}")
            self.array = self.array[:insertPosition] + [value] + self.array[insertPosition:i]+ self.array[i+1:]
            print(f"Sorted Array {self.array} \n\n")
        return self.array



# InsertionSort O(n**2)

def insertionSort(array):
    length = len(array)
    sorted_array = array.copy()
    for i in range(1, length):
        currentPointer = sorted_array[i]

        #comparison started with previous one
        j = i - 1
        #print(f"Current i = {i}")
        #print(f"Current j = {j}")
        print(f"Current pointer {currentPointer}")

        # while the compaarison is not ended
        # and the value of current pointer is smaller
        # than the previous one, do swap.
        while j>=0 and currentPointer < sorted_array[j]:
            sorted_array[j+1] = sorted_array[j]
            j-=1
            print(f"Inside while{sorted_array}")
            print(f"After processed j = {j}")
        sorted_array[j+1] = currentPointer
        print(f"Origin: {array}")
        print(f"Sorted: {sorted_array}\n")

    return sorted_array

# binaryInsertionSort O(nlog(n))
def binaryInsertionSort(array):

    def binarySearch(array, value, start, end):
        # to get insert position
        if start == end:
            if array[start] > value:
                return start
            else: 
                return start+1

        if start > end:
            return start  

        mid = (start+end)//2
        if array[mid] > value:
            # search the l't branch
            return binarySearch(array, value, start, mid-1)
        elif array[mid] < value:
            # search the r't branch
            return binarySearch(array, value, mid+1, end)
        else: 
            print(f"insert position: {mid}\n")
            return mid

    length = len(array)
    for i in range(1, length):
        value = array[i]
        #find insert position
        insertPosition = binarySearch(array, value, 0, i-1)
        print(f"The insert Position for {value} is {insertPosition+1}")
        array = array[:insertPosition] + [value] + array[insertPosition:i]+ array[i+1:]
        print(f"Sorted Array {array} \n\n")
    return array




# BubbleSort

# MergeSort
# Divide and Conquer 

## my version 
def merge(Lbranch, Rbranch):
    """
    the given input should be a sorted array
    """
    bufferlength = len(Lbranch)+len(Rbranch)
    buffer_array = [0]*bufferlength
    k = 0
    while len(Lbranch)>0 and len(Rbranch)>0:
        if Lbranch[0] < Rbranch[0]:
            buffer_array[k] = Lbranch[0]
            Lbranch.pop(0)
            #print(buffer_array)
        else:
            buffer_array[k] = Rbranch[0]
            Rbranch.pop(0)
            #print(buffer_array)
        k+=1
    while len(Lbranch)>0:
        buffer_array[k] = Lbranch[0]
        #print(buffer_array)
        Lbranch.pop(0)
        k+=1
    while len(Rbranch)>0:
        buffer_array[k] = Rbranch[0]
        #print(buffer_array)
        Rbranch.pop(0)
        k+=1
    #print(buffer_array)
    return buffer_array

def mergeSort(array):
    # the base case is one number only
    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    Lbranch = array[:mid]
    Rbranch = array[mid:]
    # print(Rbranch)
    # Recursively getting the base
    Lbranch = mergeSort(Lbranch)
    Rbranch = mergeSort(Rbranch)
    
    #print(f"Merge result {merge(Lbranch, Rbranch)}")
    return merge(Lbranch, Rbranch)

## The version that similar to Geeks for Geeks
def mergeSortGfG(array):
    # the base case is one number only
    if len(array) > 1:
        mid = len(array)//2
        Lbranch = array[:mid]
        Rbranch = array[mid:]
        # Recursively getting the base
        mergeSortGfG(Lbranch)
        mergeSortGfG(Rbranch)

        # Start to merge

        ## create the pointers, 
        ## one for the L one for the R branch
        i = 0 # LeftPointer
        j = 0 # RightPointer
        k = 0 # SortedPointer 
        while i<len(Lbranch) and j<len(Rbranch):
            if Lbranch[i] < Rbranch[j]:
                array[k] = Lbranch[i]
                i+=1
                #print(f"Left Pointer: {i}")
            else:
                array[k] = Rbranch[j]
                j+=1
            k+=1
            #print(f"Sorted Pointer: {k}")
        
        # Left branch has element left, take it to the latest in the array    
        while i < len(Lbranch):
            array[k] = Lbranch[i]
            i += 1
            k += 1
        while j < len(Rbranch):
            array[k] = Rbranch[j]
            j += 1
            k += 1
        return array



# QuickSort 
def partion(array, low, high):
    
    pivot = array[-1] 

def quicksort(array):
    """Divide amd Conquer"""

    if len(array) == 1:
        return array
        
    else:
        quicksort()



test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
test2 = [21, 2, 3]
print(insertionSort(test))
print(binaryInsertionSort(test))
print(mergeSort(test))
print(mergeSortGfG(test))
#print(quicksort(test))

