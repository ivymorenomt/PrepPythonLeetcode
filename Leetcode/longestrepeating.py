''' Given a string, find the length of the longest
substring without repeating characters.

"abccabbb" - 3
abc, cab

- Is the string contiguous?
substring vs subsequence
'abcbbd'
substring is: abc
subsequence is: abcd - note that it skipped bb 
- does case sensitivity matter?

Step 2: Test cases
"abccabbb" - 3
"cccccc" - 1
"" - 0
"abcbda" - overlaps  - 4

'''

def substring():
    longest = 0
    