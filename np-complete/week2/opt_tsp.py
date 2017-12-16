from itertools import combinations 
from math import factorial 

def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = int(f[0][:-1])
  points = [map(float,line[:-1].split(" ")) for line in f[1:]]

  return graph_info, points

def calc_euclid_distance(x, y):
 return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(0.5)

def n_choose_k(n, k):

  if n < k:
    return 0
  else:
    return factorial(n) / (factorial(k) * factorial(n-k))

def n_choose_k_table(num_points):
  
  table = {}

  for n in range(num_points):
    for k in range(1, n+2):
      table[(n,k)] = n_choose_k(n, k)
  return table

def comb_index(comb_start, comb, nck_table):
  return sum([nck_table[(y - comb_start, x+1)] for x, y in enumerate(comb)])
  
def create_graph(points):

  graph = []  

  for origin_idx, origin in enumerate(points):
    graph.append([])
    for destination_idx, destination in enumerate(points):
      if origin != destination:
        graph[origin_idx].append([ destination_idx, calc_euclid_distance(origin, destination)])
        
  return graph

def create_dist_dict(points):

  dist_dict = {}

  for i, j in combinations(range(1, len(points)), 2):
    dist_dict[(i, j)] = calc_euclid_distance(points[i], points[j])
    dist_dict[(j, i)] = dist_dict[(i, j)]

  return dist_dict
    

def calc_opt_path(num_points, points):

  dist_dict = create_dist_dict(points)
  nck_table = n_choose_k_table(num_points)

  A = [[0 for i in range(num_points + 1)] for j in range(2, num_points + 1)]

  print dist_dict

  for point in range(2, num_points + 1):
    A[comb_index(2, (point,), nck_table)][point] = dist_dict[(1, point)] 

  print A
  
  min_cost = 0;

  return min_cost 



def main():

  filename = 'tsp.txt'
  num_points, points = process_text(filename)

  min_cost = calc_opt_path(num_points, points)



if __name__ == "__main__":
  main()
