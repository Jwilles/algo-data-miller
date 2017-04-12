intfile = open('QuickSortInput.txt', 'r')
intArr = intfile.read().split('\r\n')
intArr.pop()
intArr = map(int, intArr) 


testArr = [1,3,5,2,4,6]
testArr2 = [6,5,4,3,2,1]

def choosePivot(arr):
  return arr[0]

def chooseLastPivot(arr):
  n = len(arr)
  pivot = arr[n-1]
  arr = swap(arr, 0, n-1)
  return [pivot, arr]

def chooseMedianPivot:

  
def swap (arr, i, j):
  temp = arr[j]
  arr[j] = arr[i]
  arr[i] = temp
  return arr

def quickSort(arr):
  n = len(arr)
  comparisons = n-1

  if n < 2:
    return [0, arr]
  
  p = chooseLastPivot(arr)
  pivot = p[0]
  arr = p[1]
  i = 1
  for j in range(1,n):
    if arr[j] < arr[0]: 
     arr = swap(arr, i ,j)
     i += 1
  smallSort = quickSort(arr[1:(i)])
  bigSort = quickSort(arr[(i):])
  comparisonTotal = comparisons + smallSort[0] + bigSort[0]
  sortedArr = smallSort[1] + [arr[0]] + bigSort[1]
  return [comparisonTotal, sortedArr]
    
 
print quickSort(intArr) 

