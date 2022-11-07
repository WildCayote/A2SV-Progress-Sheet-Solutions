class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            j = nums2.index(i)
            try:
                f = j+1
                while f < len(nums2):
                    if i < nums2[f]:
                        ans.append(nums2[f])
                        break
                if f == len(nums2) - 1:
                    ans.append(-1)
            except:
                ans.append(-1)
                        
        return ans            
                
