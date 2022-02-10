from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
		return list(set(range(1, len(nums)+1))-set(nums))

nums = [1,3,5,7]

result = findDisappearedNumbers(nums)
print(result)