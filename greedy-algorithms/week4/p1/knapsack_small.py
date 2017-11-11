import heapq

def process_text(filename):
  f = open(filename, 'r').readlines()
  size, num_items  = map(int, (f[0][:-1]).split(" "))
  items = [map(int, (line[:-1]).split(" ")) for line in f[1:]]

  return size, num_items, items 



def optimal_knapsack(size, num_items, items):

  A = [[0 for i in range(0, size)] for j in range(0,num_items)]

  for i in range(0, num_items):
    for j in range(0, size):
      if items[i][1] > j:
        A[i][j] = A[i-1][j]
      else:
        A[i][j] = max(A[i-1][j], A[i-1][j-items[i][1]] + items[i][0])

  return A[num_items-1][size-1] 


def main():

  filename = 'knapsack1.txt'
  size, num_items, items  = process_text(filename)

  max_val = optimal_knapsack(size, num_items, items)

#  print size  
#  print num_items 
  print max_val 


if __name__ == '__main__':
  main()
