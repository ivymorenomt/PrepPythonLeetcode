#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# get the list
# run thru the list and save in temporary storage
# if temporary storage is equal to what we have in the original list, then
# return true
#else return false


def duplicates(nums):
    if len(set(nums)) < len(nums):
        print('There is a duplicate')
        return True
    else:
        print('There are no duplicate values')
        return False
    
nums = [1,2,3,4,1]
duplicates(nums)

