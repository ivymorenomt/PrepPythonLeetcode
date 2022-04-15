def movezero(nums):
    l = 0
    counter = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        if nums[counter] > 0:
            counter +=1
    return nums, counter

nums = [0,1,0,0,0]
print('This returns the array with moved zeros and count the number of items that are greater than 0')
print(movezero(nums))