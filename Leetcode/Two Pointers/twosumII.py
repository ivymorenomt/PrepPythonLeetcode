def twosum(arr, target):
    
   p1, p2 = 0, len(arr)-1 # p1 is 0 index, and p2 is starting from the end.
   while True:
 
       numbertofind = arr[p1] + arr[p2]
       if numbertofind == target:
           return p1, p2
       elif numbertofind < target:
           p1 += 1 # p1 to decrease
       else:
           p2 -= 1 # p1 to move
       return None