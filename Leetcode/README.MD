## Leetcode Practice

This list came from [patterns](https://seanprashad.com/leetcode-patterns/)
Also using this [list](https://docs.google.com/spreadsheets/d/1A2PaQKcdwO_lwxz9bAnxXnIQayCouZP6d-ENrBz_NXc/edit#gid=0).

Some problem [solving strategies](https://dev.to/moresaltmorelemon/algorithm-problem-solving-strategies-21cp).

**NOTE**: Before solving, do the following:
#### Think
1. Analyze the problem
2. Restate the problem
3. Write out examples of input and output.
4. Create positive test cases to cover possibilities 
5. Break the problem into its component parts
6. OUtline a solution in pseudo-code
7. Step through your example data with your pseudo-code

#### Execute
1. Code
2. Test your solutions against your test case
3. Refactor

#### Legend:
:no_entry_sign: : Needs some work 
:white_check_mark: : Completed
:white_large_square: : Not Completed



|Status | Difficulty | Title | Category | Code | Link | Notes | Time Taken |
| --- | --- | --- | --- | --- | --- | --- | --- |
| :no_entry_sign: | Easy | Two Sum | Arrays | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/twosum.py)  |[Leetcode Two Sum](https://leetcode.com/problems/two-sum/)| use hash map to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice| 30mins |
| :white_large_square: | Easy | Merge Two Sorted Lists | Linked Lists | | [Leetcode Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Join two sorted linked list together and the output is the final sorted linked list. |  |
| :no_entry_sign: | Easy | Find Smallest Letter Greater Than Target | Binary Search | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/findsmallestletter.py) | [Leetcode Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target) |  Followed binary search for numbers however I get incorrect results. | 30 mins |
| :white_check_mark: | Easy | Peak Index in a Mountain Array | Binary Search | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/mountainArray.py) | [Leetcode Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/) |  Search for the largest number in the array. | 10 mins |
| :white_check_mark: | Easy | Contains Duplicate | Arrays | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/containsDuplicate.py) | [Leetcode Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) |  Use set and compare if lesser than the current array. | 5 mins |
| :white_check_mark: | Easy | Binary Search | Binary Search | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/binarysearch.py) | [Leetcode Binary Search](https://leetcode.com/problems/binary-search/) |  Binary Search algorithm used | 5 mins |
| :white_large_square: | Medium | Product of array except Self | Arrays | []() | [Leetcode Product of Array except self](https://leetcode.com/problems/product-of-array-except-self/) |  |  |
| :white_large_square: | Easy | Best Time to Buy and Sell Stock | Greedy | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/besttimestock.py) | [Leetcode Binary Search](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) |  Find local minimum and max, then used Sliding Window | 1 hour |
| :white_check_mark: | Medium | Find the duplicate Number | Arrays, Binary Search, Two Pointers | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/findduplicatenumbers.py) | [Leetcode Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) |  Use Sets and add duplicate to set once seen. | 10mins |
| :white_check_mark: | Medium | Odd Even Linked List | Linked List, Two Pointers | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/linkedlistoddeven.py) | [Leetcode Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/) |  Use two pointers to indicate which is even and which is odd. | 30mins |
| :white_check_mark: | Medium | Find Peak Element | Arrays | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/findpeakelem.py) | [Leetcode Find Peak Element](https://leetcode.com/problems/find-peak-element/) |  Use binary search and return index of the highest element | 10mins |
| :white_check_mark: | Easy | Maximum Subarray | Dynamic Programming, Arrays | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/maxsubarray.py) | [Leetcode Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |  Use Sliding Window Approach. If negative values, set it to zero. | 10mins |
| :white_check_mark: | Easy | Reverse a Linked List | Linked Lists | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/reverselinkedlist.py) | [Leetcode Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |  Use Two Pointers approach | 30mins |
| :white_check_mark: | Easy | Linked List Cycle | Linked Lists | [My Solution](https://github.com/ivymorenomt/PrepPythonLeetcode/blob/master/Leetcode/detectcycle.py) | [Leetcode Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) |  Use slow and fast Pointers approach | 45mins |