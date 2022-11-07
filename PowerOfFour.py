class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 4 and n != 1:
            return False
        elif n == 4 or n == 1:
            return True
        else:
            return self.isPowerOfFour(n/4)
