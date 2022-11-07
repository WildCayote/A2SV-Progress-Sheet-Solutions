class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result  = 0
        hasZero = False
        a,b = 0,0
        for x in nums:
            if not x:
                hasZero = True
                a,b = b,0
            else:
                b += 1
                if (a+b)>result:
                    result = a+b
        #
        if result and not hasZero:
            result -= 1
        return result
