
# def binary_search(letters, target):
#     first = 0 
#     last = len(letters) -1
#     while last <= first: 
#         mid = (first + last) // 2 
#         if letters[mid] > target:
#             first = mid
#         else:
#             last = mid + 1
#         if letters[mid] <= target:
#             return letters[0]
#         return letters[first]

def nextGreatestLetter(letters, target):
    seen = set(letters)
    for i in range(1, 26):
        cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
        if cand in seen:
            return cand


letters = ["a", "b"]
print(nextGreatestLetter(letters, "z"))

# Find the target in letters
# If found, compare to 
