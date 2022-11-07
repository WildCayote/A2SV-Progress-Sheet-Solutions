def countSwaps(n , a):
    swapCount = 0
    #bubble sort
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                #swap
                a[j] , a[j+1] = a[j+1] , a[j] 
                swapCount += 1
    
    print("Array is sorted in" , swapCount , "swaps.")
    print("First Element:" , a[0])
    print("Last Element:" , a[n-1])
