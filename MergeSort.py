import time


def mergeSort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

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

unsorted_list = [14.3, 42.6, 25.7, 1.4, 7.3, 2.6, 8.2, 12.5, 64.2, 9.5]

mergeSort(unsorted_list)

print(unsorted_list)


 # code used from school resources
def measure_sort_time(inputted_amount):
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    mergeSort(series) # execute the function with the series
    print("Input size=", inputted_amount, " Time taken=", time.time()-start_timer)


 # number of iterations
k = 1000;
measure_sort_time(20*k)
measure_sort_time(100*k)
measure_sort_time(500*k)
measure_sort_time(1000*k)
measure_sort_time(2000*k)


