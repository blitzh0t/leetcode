class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ctr = 0
        maxlist = list()
        for x in nums:
            if x == 1:
                ctr += 1
            else:
                maxlist.append(ctr)
                ctr = 0
        if ctr > 0:
            maxlist.append(ctr)
        if len(maxlist) > 0:
            return max(maxlist)
        else:
            return 0