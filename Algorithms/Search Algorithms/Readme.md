## Search Algorithms
It is a fundamental algorithm that a programmer needs to know, specially if they are working with the data.

### Linear Search
You iterate through every element in a data set and compare it to the target number/data. If your comparison finds a match, the number is in the list. If your algorithm ends without finding a match, then the number is not on the list.

**When to Use:** Consider using this algorithm when your data is not sorted. The algo's time complexity is O(n). Worst case, in a list of 10 items, the algorithm will take 10 steps. The best case is O(1) because the item you are looking for could be the first item in the list, so your algo will take only one step because it stops as soon as it finds a match. On average, a linear search will take n/2 steps.

In **real** world, specially Python, you can use the built-in **IN** function, instead of creating your own.

### Binary Search
Binary search cannot be used on every data set because it only works when the data is sorted.
It searchs for an element in a list by dividing it into halves. Suppose you have a list of numbers sorted from lowest to highest and you are 
looking for number 19. The first step is to locate the middle number.

```
    numbers = [10, 12, 13, 14, 15, 18, 19]
```
here it shows 14 is the middle number. Since 14 is not what you are looking for, it will continue searching. The next step is to determine whether the number you are looking for is greater than or less than the middle number. The number 19, is greater than 14, so there is no need to search the bottom half of the list.

```
    numbers = [15, 18, 19]
```
next is to repeat the process by locating the middle number, which is 18. Since we are not searching for 18, you again determine whether you keep the lower half or upper half. Because 19 is greater than 18, you keep the upper half and eliminate the lower half.

Then it leaves only one number 19, which is the number you are searching for.

Binary search is more efficient than Linear Search becasue you don't have to search an entire list. It makes an enormous difference when you are dealing with large amounts of data. 
In a binary search, the first time you halve your list, you will have n/2 items left in it. After the second iteration, it is n/2/2(which is n/2**1)