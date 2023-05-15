class Sorting:
    
    arr = []
    size = 0
    
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
    
    def InsertIntoArray(self, num):
        self.arr.append(num)
        self.size += 1

    def CreateArray(self, array):
        self.arr = array
        self.size = len(array)

    def EmptyArray(self):
        self.arr = []
        self.size = 0

    def DisplayArray(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print("")

    def BubbleSort(self, isDescending=False):
        # Only use for small arrays
        for iter1 in range(self.size):
            for iter2 in range(self.size-iter1-1):

                if isDescending == True:
                    if self.arr[iter2] < self.arr[iter2+1]:
                        self.arr[iter2], self.arr[iter2+1] = self.arr[iter2+1], self.arr[iter2]
                    else:
                        pass
                else:
                    if self.arr[iter2] > self.arr[iter2+1]:
                        self.arr[iter2], self.arr[iter2+1] = self.arr[iter2+1], self.arr[iter2]
                    else:
                        pass  

        return


    def SelectionSort(self, isDescending=False):
        # Only use for small arrays
        ind = 0
        for iter1 in range(self.size):
            ind = iter1
            for iter2 in range(iter1+1, self.size):

                if isDescending == True:
                    if self.arr[iter2] > self.arr[ind]:
                        ind = iter2
                    
                else:
                    if self.arr[iter2] < self.arr[ind]:
                        ind = iter2

            self.arr[ind], self.arr[iter1] = self.arr[iter1], self.arr[ind]

        return


    def InsertionSort(self, isDescending=False):
        # Only use for small arrays
        
        for iter1 in range(1, self.size):
            iter2 = iter1 - 1
            key = self.arr[iter1]

            while iter2 >=0:
                if isDescending==True and self.arr[iter2] > key:
                    break
                elif isDescending==False and self.arr[iter2] < key:
                    break
                else:
                    self.arr[iter2], self.arr[iter2+1] = self.arr[iter2+1], self.arr[iter2]
                    iter2 -= 1

        return


    def Partition(self, low, high, isDescending=False):
        # Only For Quick Sorting Mechanism
        pivot = self.arr[high]
        index = low - 1

        for iter in range(low, high):
            if isDescending == False and self.arr[iter] <= pivot:
                index += 1
                self.arr[iter], self.arr[index] = self.arr[index], self.arr[iter]
            elif isDescending == True and self.arr[iter] >= pivot:
                index += 1
                self.arr[iter], self.arr[index] = self.arr[index], self.arr[iter]

        index += 1
        self.arr[index], self.arr[high] = self.arr[high], self.arr[index]
        return index


    def QuickSort(self, isDescending=False, low=0, high=-2):
        # Not Efficient for more corner cases in long arrays
        if high == -2:
            high = self.size - 1
        
        if low < high:
            pivot = self.Partition(low, high, isDescending)
            self.QuickSort(isDescending, low, pivot-1)
            self.QuickSort(isDescending, pivot+1, high)
        else:
            return


    def MergeSort(self, isDescending= False, array= "Empty"):
        # Most efficient as a stable method for all cases
        if array == "Empty":
            array = self.arr

        if len(array) > 1:
            mid = len(array) // 2
            leftArr = array[:mid]
            rightArr = array[mid:]
            self.MergeSort(isDescending, leftArr)
            self.MergeSort(isDescending, rightArr)

            leftInd = rightInd = iter = 0

            while leftInd < len(leftArr) and rightInd < len(rightArr):
                if isDescending == True:
                    if leftArr[leftInd] >= rightArr[rightInd]:
                        array[iter] = leftArr[leftInd]
                        leftInd += 1
                    else:
                        array[iter] = rightArr[rightInd]
                        rightInd += 1
                else:
                    if leftArr[leftInd] <= rightArr[rightInd]:
                        array[iter] = leftArr[leftInd]
                        leftInd += 1
                    else:
                        array[iter] = rightArr[rightInd]
                        rightInd += 1
                iter += 1
            
            while leftInd < len(leftArr):
                array[iter] = leftArr[leftInd]
                leftInd += 1
                iter += 1 
            
            while rightInd < len(rightArr):
                array[iter] = rightArr[rightInd]
                rightInd += 1
                iter += 1
            
            if len(array) == self.size:
                self.arr = array
    