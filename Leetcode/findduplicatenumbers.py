def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dups = []
        a_set = set()
        for item in nums:
            l1 = len(a_set)
            a_set.add(item)
            l2 = len(a_set)
            if l1 == l2:
                dups.append(item)
        for i in dups:
            return i
        


'''
The answer:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
'''


nums = [3,1,3,4,2]
print(findDuplicate(nums))