def maxSubArray(nums):
    maxSub = nums[0] 
    curSum = 0 # constantly computing the sum
    
    for n in nums:
        if curSum < 0:
            curSum = 0 # this is to remove the zero
        curSum += n # this is to keep adding the current sum of the sub array
        maxSub = max(maxSub, curSum) # it will determine the highest
    return maxSub   

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))