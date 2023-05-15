from SortingFile import Sorting


class Searching(Sorting):

    def __init__(self, array):
        self.arr = array
        self.pos = -1
        self.size = len(array)

    def DisplayPosition(self, query):
        if self.pos == -1:
            print("The element", query, "is not present in the array")
        else:
            print("The element", query, "is present at", self.pos + 1, "position")
    
    def LinearSearch(self, query):
        # Valid for all types of arrays
        for iter in range(self.size):
            if self.arr[iter] == query:
                self.pos = iter
                break

        self.DisplayPosition(query)
        return self.pos


    def BinarySearch(self, query, isSorted=False):
        # Valid only for a Sorted array
        if isSorted == True:
            if self.arr[0] <= self.arr[-1]:
                isAscending = True
            else:
                isAscending = False
    
            low = 0
            high = self.size
            mid = (low + high) // 2

            while low < high:
                mid = (low + high) // 2
                if self.arr[mid] == query:
                    self.pos = mid
                    break
                elif ((self.arr[mid] < query and isAscending == True) 
                        or (self.arr[mid] > query and isAscending == False)):
                    low = mid + 1
                else:
                    high = mid - 1
            
            self.DisplayPosition(query)
            return self.pos
        
        else:
            print("Binary Search is only possible for Sorted arrays. Try linear search for other arrays")
            self.LinearSearch(query)


if __name__ == "__main__":
    
    obj1 = Searching([2, 5, 3, 8,4,1,21,4])
    obj1.BubbleSort()
    obj1.DisplayArray()
    obj1.BubbleSort(isDescending = True)
    obj1.DisplayArray()
    
    obj1 = Searching([2, 5, 3, 8,4,1,21,4])
    obj1.SelectionSort()
    obj1.DisplayArray()
    obj1.SelectionSort(isDescending = True)
    obj1.DisplayArray()
    
    obj1.CreateArray([2, 5, 3, 8,4,1,21,4])
    obj1.InsertionSort()
    obj1.DisplayArray()
    obj1.InsertionSort(isDescending = True)
    obj1.DisplayArray()
    
    obj1.CreateArray([2, 5, 3, 8,4,1,21,4])
    obj1.QuickSort()
    obj1.DisplayArray()
    obj1.QuickSort(isDescending = True)
    obj1.DisplayArray()
    
    obj1.CreateArray([2, 5, 3, 8,4,1,21,4])
    obj1.MergeSort()
    obj1.DisplayArray()
    obj1.MergeSort(isDescending = True)
    obj1.DisplayArray()

    obj1.CreateArray([2, 5, 3, 8,4,1,21,4])
    obj1.LinearSearch(5)
    
    obj1.CreateArray([2, 5, 3, 8,4,1,21,4])
    obj1.MergeSort()
    obj1.DisplayArray()
    obj1.BinarySearch(4, isSorted = True)
