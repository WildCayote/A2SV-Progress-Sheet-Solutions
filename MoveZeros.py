class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        zeroCounter = 0
        while counter < len(nums):
            if nums[counter] == 0:
                zeroCounter +=1
            counter += 1
        for i in range(zeroCounter):
            nums.remove(0)
            nums.append(0)
            
