class Solution: 
    def select(self, arr, i):
        arr[self.min] , arr[i] = arr[i] , arr[self.min]
        

    def selectionSort(self, arr,n):
        for i in range(len(arr)):
           self.min = i
           for j in range(i+1 , len(arr)):
              if arr[self.min] > arr[j]:
                self.min = j

           self.select(arr , i) 
        
        return arr
