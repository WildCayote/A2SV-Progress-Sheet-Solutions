class Solution:
    def countRemaining(self , type1 , type2 , index2 , array):
        amount = 0
        if index2 >= len(array):
            return amount
        else:
            index2 += 1
            while index2 < len(array):
                if type1 == array[index2] or type2 == array[index2]:
                    amount += 1 
                    index2 += 1
                else:
                    return amount
            return amount
    def totalFruit(self , fruits):
        numOfTrees = 0
        if len(fruits) == 1:
            return 1
        for index1 in range(0 , len(fruits) - 1 , 1):
            tempAmount = 0
            if fruits[index1] == fruits[index1 + 1]:
                try:
                    tempAmount += 3 + self.countRemaining(fruits[index1 + 1] , fruits[index1 + 2] , index1 + 2 , fruits)
                    if tempAmount > numOfTrees:
                        numOfTrees = tempAmount
                except:
                    tempAmount += 2
                    if tempAmount > numOfTrees:
                        numOfTrees = tempAmount        
            else:
                tempAmount += self.countRemaining(fruits[index1] , fruits[index1 + 1] , index1 + 1 , fruits) + 2
                if tempAmount > numOfTrees:
                    numOfTrees = tempAmount
        
        return numOfTrees
