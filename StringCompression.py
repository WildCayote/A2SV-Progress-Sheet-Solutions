class Solution:
    def compress(self, chars: List[str]) -> int:
        
        chars_copy = chars.copy() 
        sumVal = 0 
        delSum = 0 
        inSum = 0 
        
        if len(chars_copy) == 1:
            return len(chars)
        
        for i in range(len(chars_copy)):
            u = i - delSum + inSum
            if i < len(chars_copy) - 1:
                temp = chars_copy[i] 
                if chars_copy[i] == chars_copy[i+1]:
                    sumVal += 1

                    del chars[u]
                    delSum += 1
                else:
                    sumVal += 1
                    
                    N = len(str(sumVal))
                    if sumVal > 1:
                        chars[u+1:u+1] = list(str(sumVal))
                        inSum += N
                    sumVal = 0
            else:
                if chars[u] == temp:
                    sumVal += 1
                    if sumVal > 1:
                        chars[u+1:u+1] = list(str(sumVal))
        
        return len(chars)
