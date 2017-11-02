import heapq

def process_text(filename):
  f = open(filename, 'r').readlines()
  num_symbols = int(f[0][:-1])
  symbols = [(int(weight[:-1]), ind) for ind, weight in enumerate(f[1:])]
  symbols_dict = {ind: int(x[:-1]) for ind, x in enumerate(f[1:])}
#  symbols = {int(x[:-1]): ind  for ind, x in enumerate(f[1:])}
  return num_symbols, symbols, symbols_dict



def main():

  filename = 'huffman.txt'
  num_symbols, symbols, symbols_dict = process_text(filename)

  heapq.heapify(symbols)

#  print heapq.heappop(symbols)
#  print heapq.heappop(symbols)

  print symbols
#  print num_symbols
#  print weights

if __name__ == '__main__':
  main()
