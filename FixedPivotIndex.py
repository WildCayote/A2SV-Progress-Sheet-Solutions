class Solution:
    #sum to the right
    def sumRight(self , index , array):
        sum = 0
        if index == len(array) - 1:
            return sum
        else:
            count = index + 1
            while count < len(array):
                sum += array[count]
            return sum
    #sum to the left
    def sumLeft(self , index , array):
        sum = 0
        if index == 0:
            return sum
        else:
            count = index + 1
            while count > -1:
                sum += array[count]
            return sum        
    #soln
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(nums):
            if self.sumRight(i , nums) == self.sumLeft(i , nums):
                return i
        return -1
