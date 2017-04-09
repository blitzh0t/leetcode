class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        They key to make this efficient as possible is to reduce the number of
        times we check if an integer is a factor of the input number.
        Number Theory:
        Composite Number has Prime Factor not Greater Than its Square Root
        
        We will only check until the square root of the input integer , and add 1
        for it to be included. 
        e.g for x in range(1,int(sqrt(input_int))+1)
        
        The resulting list will only give you the result of factors not greater
        than the square root of the input integer. To get the other factors , divide
        each of the elements on the first list with the input integer. Compare the two list
        and add criteria to remove any duplicate and elements equal to the input integer
        """
        if num < 0:
            return False
        limit = int(num ** 0.5) + 1
        sqrt_list = [(x if x != num else 0) for x in range(1,limit) if num % x == 0]
        sqrt_factor_list = [(num / x if x != num / x and x != 1 else 0) for x in sqrt_list if x != 0]
        return ((sum(sqrt_list) + sum(sqrt_factor_list)) == num) if num > 0 else False