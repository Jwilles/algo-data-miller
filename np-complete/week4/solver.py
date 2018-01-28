import math

def process_text(filename):
  
  f = open(filename, 'r').readlines()
  S_info = int(f[0][:-1])

  clauses = [] 

  for line in f[1:]:
    split_line = line[:-2].split(" ")
    clauses.append((split_line[0], split_line[1]))

  return S_info, clauses


def main():

  filename = '2sat1.txt'
  S_info, clauses = process_text(filename)
  #tsp_path_sum = generate_tsp_path(G_info, G)

  print S_info
  print clauses

if __name__ == '__main__':
  main()
