import time


def measure_time(input_size):
    sequence = [i for i in range(input_size)] # input = a list [0,1,2,...]
    #print(sequence)
    start = time.time() # start timer
    #LinearSearch(sequence) # execute the function with the sequence
    print("Input size=", input_size, " Time taken=", time.time()-start)


# Now, we make input size larger, 2k, 10k,50k, 200k,1000k 


k = 1000;
measure_time(20*k)
measure_time(100*k)
measure_time(500*k)
measure_time(1000*k)
measure_time(2000*k)