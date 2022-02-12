def binary_search(letters, target):
    first = 0 
    last = len(letters) -1
    while last <= first: 
        mid = (first + last) // 2 
        if letters[mid] > target:
            first = mid
        else:
            last = mid + 1
        if letters[mid] <= target:
            return letters[0]
        return letters[first]

letters = ["c", "f", "j"]
print(binary_search(letters, "c"))

