def countingSort(n , arr):

    result = [0] * 100

    # counting the number of appearances
    for i in arr:
        result[i] += 1
    
    return result
