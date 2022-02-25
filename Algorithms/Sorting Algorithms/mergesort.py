def mergesort(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    
    while i < len_a and j < len_b:  # you want to stop at the end of either of the list
        if a[i] <= b[j]: #Element higher than first list
            sorted_list.append(a[i])
            i+=1 # inserting element to sorted lis. J pointer is static.
        else:
            sorted_list.append(b[j])
            j+=1
    
    
    return sorted_list

if __name__ == '__main__':
    a = [5, 8, 12, 56]
    b = [7, 9, 45, 51]
    
    print(mergesort(a,b))