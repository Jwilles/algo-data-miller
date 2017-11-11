import heapq

def process_text(filename):
  f = open(filename, 'r').readlines()
  
  size, num_items  = map(int, (f[0][:-1]).split(" "))
  items = [map(int, (line[:-1]).split(" ")) for line in f[1:]]
#  symbols_dict = {ind: int(x[:-1]) for ind, x in enumerate(f[1:])}
#  symbols = {int(x[:-1]): ind  for ind, x in enumerate(f[1:])}
  return size, num_items, items 

def main():

  filename = 'knapsack1.txt'
  size, num_items, items  = process_text(filename)

  print size  
  print num_items 
  print items[0]


if __name__ == '__main__':
  main()
