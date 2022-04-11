def findPeakElement(nums):
        leftind = 0
        rightind = len(nums)-1
        while leftind < rightind:
            mid = (leftind +rightind) //2
            if nums[mid] > nums[mid + 1]:
                rightind = mid
            else:
                leftind = mid + 1
        return leftind
nums = [1,2,3,1]
print(findPeakElement(nums))