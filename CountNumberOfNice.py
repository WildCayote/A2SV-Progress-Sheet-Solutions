class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # num of 0 odd num: 1
        prefix = {0: 1}
        total = ans = 0
        for num in nums:
            if num % 2 == 1:
                total += 1
            if total-k in prefix:
                ans += prefix[total-k]
            prefix[total] = prefix.get(total, 0) + 1
        return ans
