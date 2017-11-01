def process_text(filename):
  f = open(filename, 'r').readlines()
  num_symbols = int(f[0][:-1])
  symbols = {ind: int(x[:-1]) for ind, x in enumerate(f[1:])}
#  symbols = dict(f[1:])
  return num_symbols, symbols

def main():

  filename = 'huffman.txt'
  num_symbols, symbols = process_text(filename)

#  print symbols
  print num_symbols

if __name__ == '__main__':
  main()
