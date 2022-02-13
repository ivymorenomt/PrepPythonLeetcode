def mountainArray(arr):
    for x in range(len(arr)): # run through the range of the size of array
        if arr[x] > arr[x+1]: # comparing the pair of arrays to each other
            return x # this is going to return the peak index/largest of the array
    
arr = [0,50,20,0,2]
print(mountainArray(arr))

