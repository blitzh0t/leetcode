class Solution(object):
    def checkString(self,myString):
        tmp_list = list()
        tmp_dict = dict()
        i = 0
        for x in myString:
            if x not in tmp_dict:
                if myString.count(x) > 1:
                    i += 1
                    tmp_dict[x] = i
                    tmp_list.append(i)
                else:
                    tmp_list.append(0)
            else:
                tmp_list.append(tmp_dict[x])
        return tmp_list
                
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_s = self.checkString(s)
        str_t = self.checkString(t)
        return str_s == str_t  