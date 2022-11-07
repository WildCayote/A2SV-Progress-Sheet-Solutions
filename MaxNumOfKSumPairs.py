class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations = 0
        added = []
        for num in range(len(nums)-1):
            if num in added:
                continue
            for second in range(num+1 , len(nums)):
                sm = nums[num] + nums[second] 
                if sm == k and num not in added and second not in added:
                    operations += 1
                    added.append(num)
                    added.append(second)
                    continue
        
        return operations
            
