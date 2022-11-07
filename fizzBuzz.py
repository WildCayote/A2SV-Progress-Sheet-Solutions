def fizzBuzz(num):
    soln = []
    for i in range(num):
        if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
            soln.append("FizzBuzz")
        elif (i + 1) % 3 == 0:
            soln.append("Fizz")
        elif (i + 1) % 5 == 0:
            soln.append("Buzz")
        else:
            soln.append(i+1)
    
    return soln

