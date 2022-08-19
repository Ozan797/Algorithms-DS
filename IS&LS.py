 # imports needed libraries
import numpy as np
import time


def InsertionSort(unordered_list): # Insertion Sort
    for i in range(1, len(unordered_list)): # for every element
        element_sort = unordered_list[i]

        while unordered_list[i-1] > element_sort and i > 0: # if the list is still unsortred
            unordered_list[i], unordered_list[i-1] = unordered_list[i-1], unordered_list[i]
            i = i-1

    return unordered_list # returns the new sorted list

unordered_list =  [6.2, 5.7, 2.4, 1.1, 43.5, 23.2, 7.2, 0.4, 12.3, 11.7] # items in the list
print("this is the unsorted list: ", unordered_list)
sorted_list = InsertionSort(unordered_list) # runs the sorting algoirthm result into a sorted list variable
print("this is the sorted list: ", sorted_list) 
arr = np.array(sorted_list) # converts list to an array
print("this is the list converted into an array: ", arr)

number = float(input("Enter number you want to search for: ")) # float number input

def LinearSearch(number): # Linear Search Algorithm
    found = False # flag
    attempts = 0 # counter
    while (attempts < len(sorted_list)) and (found == False): # attempts less than list length
        if sorted_list[attempts] == number: # if element is found
            found = True # True flag
            print(number, "is in the list at index", attempts) # outputs result
        attempts += 1 # increment attempt counter
    if found == False: # if element isnt found
        print(number, "is not in the list") 

LinearSearch(number) # runs search algorithm

 # code used from school resources
def measure_sort_time(inputted_amount): # 
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    InsertionSort(series)
    # execute the function with the series
    print("Insertion Sort Time Complexity:"," Input size=", inputted_amount, " Time taken=", time.time()-start_timer)


def measure_search_time(inputted_amount): # searching algorithm time taken
    series = [i for i in range(inputted_amount)]
    start_timer = time.time() # starts the timer
    LinearSearch(series)
    # execute the function with the series
    print("Linear Search Time Complexity:","Input size=", inputted_amount, " Time taken=", time.time()-start_timer)

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
