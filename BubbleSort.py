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

# list of floating point numbers
unsorted_list = [0.4, 2.6, 2.5, 9.2, 142.4, 12.1, 5.7, 1.5, 13.9, 16.2]
sorted_list = unsorted_list  # ordered list

# prints unsorted and sorted list
print("Unsorted: ", unsorted_list)
print("Sorted: ", bubble_sort(sorted_list))

def measure_time(input_size):
    sequence = [i for i in range(input_size)] # input = a list [0,1,2,...]
    #print(sequence)
    start = time.time() # start timer
    print(bubble_sort(sequence)) # execute the function with the sequence
    print("Input size=", input_size, " Time taken=", time.time()-start)


# Now, we make input size larger, 2k, 10k,50k, 200k,1000k 


k = 100;
measure_time(2*k)
measure_time(10*k)
measure_time(50*k)
measure_time(100*k)
measure_time(200*k)
