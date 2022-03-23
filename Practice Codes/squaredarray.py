def squared(nums):
    arr = [x**2 for x in nums]
    return sorted(arr)

arr = [-4, -3, 0, 1, 10]
print(squared(arr))