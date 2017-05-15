class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor_result = 0
        for x in nums:
            xor_result ^= x
        return xor_result