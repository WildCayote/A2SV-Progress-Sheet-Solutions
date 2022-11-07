def insertionSort1(n, arr):
    num = arr[n - 1]
    for j in range(n-2 ,-1 , -1):
        if arr[j] > num:
            arr[j + 1] = arr[j]
            print(*arr)
            if j == 0:
                arr[j] = num
                print(*arr)
        else:
            arr[j + 1] = num
            print(*arr)
            break
