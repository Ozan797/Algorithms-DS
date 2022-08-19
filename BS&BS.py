import numpy as np  # import library
import time 

# Bubble Search Algorithm
def bubble_sort(unsorted_list):  # bubble sort algorithm
    for x in range(0, len(unsorted_list) - 1):
        for i in range(len(unsorted_list) - 1):
            if unsorted_list[i] > unsorted_list[i + 1]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[i + 1]
                unsorted_list[i + 1] = temp
    return unsorted_list

# Binary Search Algorithm
def binary_search(sorted_list, low, high, e):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle
        if sorted_list[mid] == e:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left sublist
        elif sorted_list[mid] > e:
            return binary_search(sorted_list, low, mid - 1, e)
        # Else the element can only be present in right sublist
        else:
            return binary_search(sorted_list, mid + 1, high, e)
    else:
        # Element is not present in the list
        return -1

# list of floating point numbers
unsorted_list = [0.4, 2.6, 2.5, 9.2, 142.4, 12.1, 5.7, 1.5, 13.9, 16.2]
sorted_list = unsorted_list  # ordered list

# prints unsorted and sorted list
print("Unsorted: ", unsorted_list)
print("Sorted: ", bubble_sort(sorted_list))

e = 13.9  # element to be found at index 7
# calls the binary search function
searched_item = binary_search(sorted_list, 0, len(sorted_list) - 1, e)

# condition for the result of the search
if searched_item != -1:
    print("Element found at index:", str(searched_item))
else:
    print("Element not found")

 # code used from school resources
def measure_sort_time(inputted_amount):
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    bubble_sort(series) # execute the function with the series
    print("Bubble Sort Time Complexity:","Input size=", inputted_amount, " Time taken=", time.time()-start_timer)


 # number of iterations
k = 10
measure_sort_time(20*k) # 200
measure_sort_time(100*k) # 1000
measure_sort_time(500*k) # 5000
measure_sort_time(1000*k) # 10,000
measure_sort_time(2000*k) # 20,000


# function to convert list into a array using numpy
def array_conversion(lst):
    arr = np.array(lst)
    print("Converted into a Array:", arr)

# calls array function
array_conversion(sorted_list)
