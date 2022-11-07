def countingValleys(steps, path):
    # Write your code here
    value = {'U':1 , 'D':-1}
    level = 0
    inValey = False
    valeys = 0
    for i in path:
        if i == 'D':
            if inValey:
                level += value['D']
            else:
                level += value['D']
                if level < 0:
                    inValey = True
                    valeys += 1   
        else:
            if inValey:
                level += value['U']
                if level == 0:
                    inValey = False
            else:
                level += value['U']
    
    return valeys
