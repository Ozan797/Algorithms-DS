import math
import time

def MergeSort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]
        # Recursive call on each half
        MergeSort(left)
        MergeSort(right)
        # Two iterators for traversing the two halves
        i = 0
        j = 0
        # Iterator for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              unsorted_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_list[k]=right[j]
            j += 1
            k += 1

def JumpSearch( sorted_list , e , n ):
    # Finding block size to be jumped
    step = math.sqrt(n)
    # Finding the block where element is present (if it is present)
    prev = 0
    while sorted_list[int(min(step, n)-1)] < e:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    # Doing a linear search for x in block beginning with prev.
    while sorted_list[int(prev)] < e:
        prev += 1
        # If we reached next block or end of array, element is not present.
        if prev == min(step, n):
            return -1
    # If the element is found
    if sorted_list[int(prev)] == e:
        return prev
     
    return -1

 # Unsorted list
unsorted_list = [14.3, 42.6, 25.7, 1.4, 7.3, 2.6, 8.2, 12.5, 64.2, 9.5]
print("The Unsorted List:",unsorted_list)
 # Runs MergeSort function
MergeSort(unsorted_list)
sorted_list = unsorted_list
 # Prints sorted list
print("The Sorted List:",sorted_list)
 # Targeted element
e = 25.7
n = len(sorted_list)

# Find the index of x using Jump Search
index = JumpSearch(sorted_list, e, n)
# Print the index where x is located
print("Number", e, "is at index" ,"%.0f"%index)

 # code used from school resources
def measure_sort_time(inputted_amount):
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    MergeSort(series)
    # execute the function with the series
    print("Merge Sort Time Complexity:"," Input size=", inputted_amount, " Time taken=", time.time()-start_timer)

def measure_search_time(inputted_amount):
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    JumpSearch(series, e, n)
    # execute the function with the series
    print("Jump Search Time Complexity:","Input size=", inputted_amount, " Time taken=", time.time()-start_timer)

 # number of iterations
k = 1000
measure_sort_time(20*k) # 20,000
measure_sort_time(100*k) # 100,000
measure_sort_time(500*k) # 500,000
measure_sort_time(1000*k) # 1,000,000
measure_sort_time(2000*k) # 2,000,000
measure_search_time(20*k) # 20,000
measure_search_time(100*k) # 100,000
measure_search_time(500*k) #  500,000
measure_search_time(1000*k) # 1,000,000
measure_search_time(2000*k) # 2,000,000
