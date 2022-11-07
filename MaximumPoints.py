class Solution:
    def sum(self , array):
        sum = 0
        for i in array:
            sum += i
        return sum
    
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return self.sum(cardPoints)
        else:
            fromStart = self.sum(cardPoints[0 : k])
            fromEnd = self.sum(cardPoints[len(cardPoints) - k : len(cardPoints)])
            if fromStart > fromEnd:
                return fromStart
            else:
                return fromEnd
