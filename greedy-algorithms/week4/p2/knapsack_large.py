#import heapq

#import sys

#sys.setrecursionlimit(10000)



def process_text(filename):
  f = open(filename, 'r').readlines()
  size, num_items  = map(int, (f[0][:-1]).split(" "))
  items = [map(int, (line[:-1]).split(" ")) for line in f[1:]]

  return size, num_items, items 


def optimal_knapsack(size, num_items, items):

  A = [[0 for i in range(0, size)] for j in range(0,2)]

  for i in range(0, num_items):
    
    print i
    A[0] = A[1]

    for j in range(0, size):
      if items[i][1] > j:
        A[1][j] = A[0][j]
      else:
        A[1][j] = max(A[0][j], A[0][j-items[i][1]] + items[i][0])

  return A[1][size-1] 

def recursive_knapsack(size, num_items, items):

  if len(items) == 1:
    return items[0][0]
  else:
    next_item = items[0]
    next_items = items[1:]
    next_num_items = num_items - 1 

    return max(recursive_knapsack(size, num_items, items), recursive_knapsack((size - next_item[1]), next_num_items, next_items) + next_item[0])


def main():

  filename = 'knapsack_big.txt'
  size, num_items, items  = process_text(filename)

  max_val = optimal_knapsack(size, num_items, items)
#  max_val = recursive_knapsack(size, num_items, items)

#  print size  
#  print num_items 
  print max_val 


if __name__ == '__main__':
  main()
