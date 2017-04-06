class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
    # a gotcha on list comprehension
        nums[:] = [x for x in nums if x != val]
        return len(nums)