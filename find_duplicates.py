class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp_list = []
        prev = ""
        #need to revise in the future 
        for x in sorted(nums):
            if x == prev:
                tmp_list.append(x)
            else:
                prev = x
        return tmp_list