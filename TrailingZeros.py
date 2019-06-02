class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        
        t=n/5
        count=t
        while(t!=0):
            t=t/5
            count+=t
        return count
