def checkDups(arr):
    a = set(arr)
    b = arr
    if(len(set(arr)) < len(arr)): # set checks for duplicates
        return True
nums = [1,2,3,1]
print(checkDups(nums))