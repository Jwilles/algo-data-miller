
def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = int(f[0][:-1])
  points = [map(float,line[:-1].split(" ")) for line in f[1:]]

  return graph_info, points

def calc_euclid_distance(x, y):
  return ((x[0]-y[0])**2 + (x[1]+y[1])**2)**(1/2)
  
def create_graph(points):

  graph = []  

  for origin_idx, origin in enumerate(points):
    graph.append([])
    for destination_idx, destination in enumerate(points):
      if origin != destination:
        graph[origin_idx].append([ destination_idx, calc_euclid_distance(origin, destination)])
        
  return graph

def calc_opt_path(graph):

  A = []
  
  min_cost = 0;

  


  return min_cost 



def main():

  filename = 'tsp.txt'
  G_info, points = process_text(filename)
 
  print G_info

  graph = create_graph(points)

  min_cost = calc_opt_path(graph)

  print graph[0]



if __name__ == "__main__":
  main()
