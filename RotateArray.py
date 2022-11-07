class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for rotate in k:
            counter = 0
            result = [None] * len(nums)
            while counter < len(nums):
                try:
                    result[counter + 1] = nums[counter]
                    counter += 1
                except:
                    result[0] = nums[counter]
                    counter += 1
        nums = result
