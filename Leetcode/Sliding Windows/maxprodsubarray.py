class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_cur = max_global = nums[0]
        # for i in range(1, len(nums)-1):
        #     if nums[i] < 0:
        #         max_cur, max_global = max_global, max_cur
        #     max_cur = max(nums[i], max_cur * nums[i])
        #     if max_cur > max_global:
        #         max_global = max_cur
        # return max_global
    
    # Their answer
        res=nums[0] #Store first index value result
        max_cur=res
        min_cur=res
        for i in range(1,len(nums)):
            if nums[i]<0:
                max_cur,min_cur=min_cur,max_cur   #If curr_element is negative then swap max and min
            min_cur=min(nums[i],min_cur*nums[i])
            max_cur=max(nums[i],max_cur*nums[i])
            res=max(res,max_cur)
        return res