def insertionsort(arr):
    if arr is None:
        raise TypeError('data cannot be None')
    if len(arr) < 2:
        return arr
    for r in range(1, len(arr)): # start from index 1 to the length of array
        for l in range(r):
            if arr[r] < arr[l]:
                temp = arr[r]
                arr[l+1:r+1] = arr[l:r]
                arr[l] = temp
    return arr

if __name__ == '__main__':
    tests = [
        [7, 8, 5, 4, 9, 2],
        [9, 7],
        [29, 29, 28],
        [],
        [6]    
    ]
    for elements in tests:
        insertionsort(elements)
        print(f'Sorted Array: {elements}')    
        
    # to convert into string:     listToStr = ' '.join([str(elem) for elem in element ])