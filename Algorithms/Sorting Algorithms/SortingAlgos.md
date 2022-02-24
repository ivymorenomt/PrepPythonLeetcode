## Insertion Sort

First, you have to split the list to compare values from right to left side.

Ex:
```
    [7,4,5,2] = position 0 has no left side so there is no change of position
    [7,4,5,2] = [4, 7, 5, 2] - 7 > 4 so 7 will be moved forward and 4 will be moved to 7's position.
    [4,7,5,2] = [4, 5, 7, 2] - 7 > 5, 7 will be moved forward but 4 < 5 so there will be no change in the position
    [4,5,7,2] = [2, 4, 5, 7] - as all the element on the left side of 2 are greater than 2, all the elements will be moved forward and 2 will be shifted to the position of 4.
```

It runs in Big O(n2) time. It is very slow. However, in real world, insertion sort is still being used specially for nearly sorted data.When a list is sorted, the time complexity is O(n), which is very efficient.

### Pseudocode:
```
   1. For each value index 1 to n - 1
   2. Compare with all elements to the left of the current value to determine new insertion point
   3. Hold current value in temp variable
   4. Shift elements from new insertion point right
   5. Insert value in temp variable
   6. Break

    for r in range(1, len(arr)): # start from index 1 to the length of array
        for l in range(r):
            if arr[r] < arr[l]:
                temp = arr[r]
                arr[l+1:r+1] = arr[l:r]
                arr[l] = temp
```
#### Constraints
Always use these following constraints:
1. Is a naive solution sufficient? Yes
2. Are duplicates allowed? Yes
3. Can we assume the input is valid? No
4. Can we assume this fits memory? Yes

#### Test Cases
* None -> Exception
* Empty input -> []
* One element -> [element]
* Two or more elements