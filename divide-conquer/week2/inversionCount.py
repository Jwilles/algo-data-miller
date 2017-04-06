intfile = open('IntegerArray.txt', 'r')
intArr = intfile.read().split('\r\n')
intArr.pop()
intArr = map(int, intArr) 


testArr = [1,3,5,2,4,6]
testArr2 = [6,5,4,3,2,1]

def countSplitInversions(left, right):
  n = len(left)
  m = len(right)
  r = n+m
  i = 0
  j = 0
  inv = 0
  result = []
  for k in range(r):
    if i == n or j == m:
      result.extend(right[j:] or left[i:])
      break
    if left[i] < right[j]:
      result.append(left[i])
      i = i + 1
    elif left[i] > right[j]:
      result.append(right[j])
      inv = inv + n - i
      j = j + 1
  return [inv, result]

def countInversions(arr):
  n = len(arr)/2
  if 2*n < 2:
    return [0, arr] 
  else:
    Left = countInversions(arr[:n])
    Right = countInversions(arr[n:])
    Split = countSplitInversions(Left[1], Right[1])
  inversions =  Left[0] + Right[0] + Split[0]
  return [inversions, Split[1]]  

print countInversions(intArr)[0]
