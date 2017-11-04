def process_text(filename):
  f = open(filename, 'r').readlines()
  num_symbols = int(f[0][:-1])
#  symbols = [(int(weight[:-1]), [ind]) for ind, weight in enumerate(f[1:])]
  symbols = {(ind+1): int(x[:-1]) for ind, x in enumerate(f[1:])}
#  symbols = {int(x[:-1]): ind  for ind, x in enumerate(f[1:])}
  return num_symbols, symbols


def main():

  filename = 'mwis.txt'
  num_symbols, symbols = process_text(filename)

  A = []
  A.append(0)
  A.append(symbols[1])

  for i in range (2, (num_symbols)):
    A.append(max(A[i-1], (A[i-2] + symbols[i])))

  i = len(A) 
  S = []
  while i >= 1:
    if A[i-1] >= (A[i-2] + symbols[i]):
      i -= 1
    else:
      S.append(i)
      i -= 2

  print S
  vert_check = [1, 2, 3, 4, 17, 117, 517, 997]
  ans = []

  for vertex in vert_check:
    if vertex in S:
      ans.append(1)
    else:
      ans.append(0)
      
  print ans

if __name__ == '__main__':
  main()
