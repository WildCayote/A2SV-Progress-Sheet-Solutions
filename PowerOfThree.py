class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3 and n != 1:
            return False
        elif n ==3 or n == 1:
            return True
        else:
            return self.isPowerOfThree(n/3)
