#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

nums = [1,2,3,1]

def containsDuplicate(self, nums):
    for i in nums:
        if i == nums:
            return True
    
    return False

test = {
      'input': {
        'nums': [1, 2, 3, 1]
      }
}
      
result = containsDuplicate(test['nums'])
print(result)