import heapq

def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = int(f[0][:-1])

  graph = {} 

  for line in f[1:]:
    split_line = line[:-2].split(" ")
    graph[int(split_line[0])] = [float(x) for x in split_line[1:]]

  return graph_info, graph

def calc_squared_euclid_distance(a, b):
  squared_euclid_distance = (a[0]-b[0])**2 + (a[1]-b[1])**2
  return squared_euclid_distance

def generate_tsp_path(nodes, graph):
  print nodes
  print calc_squared_euclid_distance(graph[1], graph[2])
  return 0
  

def main():

  filename = 'nn.txt'
  G_info, G = process_text(filename)
  tsp_path = generate_tsp_path(G_info, G)

if __name__ == '__main__':
  main()
