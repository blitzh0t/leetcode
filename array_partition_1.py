class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() #this is faster than using sorted(nums) 
        return sum(nums[::2])