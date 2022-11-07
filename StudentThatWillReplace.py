class Solution:
    def findTotal(self , li):
        tot = 0
        for i in li:
            tot += i
        return tot
    
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        #total chalk for one round
        total = self.findTotal(chalk)
        
        if total > k:
            i = 0
            while True:
                if i >= len(chalk):
                    i = 0
                else:
                    if chalk[i] > k:
                        return i
                    else:
                        k -= chalk[i]
                        i += 1
        else:
            remainder = k % total
            i = 0
            while True:
                if chalk[i] > remainder:
                    return i
                else:
                    remainder -= chalk[i]
                    i += 1
