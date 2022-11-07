class Solution:
    operators = ("+" , "-" , "/" , "*")
    
    def evalRPN(self, tokens):
        i = 0
        size = len(tokens)
        while i < size:
            result , a , b = 0 ,0 ,0
            if tokens[i] in Solution.operators:
                a , b = int(tokens[i-2]) , int(tokens[i-1])
      
                if tokens[i] == "*":
                    result = a * b
                elif tokens[i] == "/":
                    result = a / b
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == '+':
                    result = a + b
                
                tokens[i - 2] = result
                del tokens[i-1]
                del tokens[i-1]
                i -= 1
                size = len(tokens)
            else:
                i += 1
        
        return int(tokens[0])  
