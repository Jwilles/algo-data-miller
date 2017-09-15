
def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = map(int, f[0][:-1].split(" "))
  edge_list = [map(int, line[:-1].split(" ")) for line in f[1:]]

  graph = {}

  for edge in edge_list:
    graph.setdefault(edge[0],[]).append(edge[1:])
    graph.setdefault(edge[1],[]).append([edge[0], edge[2]])

  return graph_info, graph


def main():

  filename = 'edges.txt'
#  filename = 'edges_test_1.txt'
  G_info, G  = process_text(filename)

  V = [1]
  vertices = set(range(1,G_info[0]+1))
  total_min_cost = 0

  print vertices

  while vertices != set(V): 
    min_cost = 100000000000
    min_edge = []
    for tail in V:
      for head in G[tail]:
        if head[0] not in V and head[1] < min_cost:
          min_cost = head[1]
          min_edge = head

    total_min_cost += min_cost 
    V.append(min_edge[0])
        
    
  print total_min_cost


if __name__ == '__main__':
  main()
