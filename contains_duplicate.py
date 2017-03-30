class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tmpset = set(nums)
        if len(tmpset) == len(nums):
            return False
        else:
            return True