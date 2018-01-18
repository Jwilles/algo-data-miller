import heapq
import math

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

def calc_euclid_distance(a, b):
  euclid_distance = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
  return euclid_distance


def find_min(curr, remaining, graph):
  min_distance = 10000000000000000000000
  min_key = 5000000000
  for key in remaining:
    if (key != curr):
      distance = calc_squared_euclid_distance(graph[curr], graph[key])
      if (distance < min_distance):
	min_distance = distance
        min_key = key
      elif (distance == min_distance and key < min_key):
	min_distance = min_distance
	min_key = key

  return min_key

def calc_path_sum(path, graph):
  path_sum = 0
  for i in range(1, len(path)):
    step = calc_euclid_distance(graph[path[i-1]], graph[path[i]])
    path_sum = path_sum + step

  return path_sum
  
    
def generate_tsp_path(nodes, graph):

  path = []
  node_set = set(range(1, nodes+1))
  remaining_set = set(range(1, nodes+1))
 
  remaining_set.remove(1)
  visited_set = set([1])
  
  current_node = 1
  path.append(1)

  while (len(remaining_set) > 0):
    min_key = find_min(current_node, remaining_set, graph)
    path.append(min_key)
    visited_set.add(min_key)
    remaining_set.remove(min_key)

    current_node = min_key

  path.append(1)

  return calc_path_sum(path, graph)

def main():

  filename = 'nn.txt'
  G_info, G = process_text(filename)
  tsp_path_sum = generate_tsp_path(G_info, G)

  print tsp_path_sum

if __name__ == '__main__':
  main()
