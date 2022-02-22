'''
Test Cases:
1. [1,3,7,9,2] t = 11 [3,4]
2. [1,3,7,9,2] t = 25 null
3. [] t=1 null
4. [5] t=5 null
5. [1,6] t=7 [0,1]
Use brute force solution, or two pointer - 

from index 0, add this to each of the elements.

The two pointer solution approach only works with numbers that are positive.

'''
import enum


def twosum(arr, target):
#    p1, p2 = 0, len(arr)-1 # p1 is 0 index, and p2 is starting from the end.
#    while True:
 
#        numbertofind = arr[p1] + arr[p2]
#        if numbertofind == target:
#            return p1, p2
#        elif numbertofind < target:
#            p1 += 1 # p1 to decrease
#        else:
#            p2 -= 1 # p1 to move
#        return None
 
    h = {}
    for i, num in enumerate(arr):
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]
        
arr = [3,2,4]
target = 6
print(twosum(arr, target))