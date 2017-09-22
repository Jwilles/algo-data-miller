
def process_text(filename):
  f = open(filename, 'r').readlines()
  graph_info = map(int, f[0][:-1].split(" "))
  sorted_edges = sorted([map(int, line[:-1].split(" ")) for line in f[1:]], key = lambda edge: edge[-1])
  return graph_info, sorted_edges

def find(node, node_set):
  if node != node_set[node][0]:
    node_set[node][0] = find(node_set[node][0], node_set) 
  return node_set[node][0]

def union(min_edge, node_set):
  x_root = find(min_edge[0], node_set)
  y_root = find(min_edge[1], node_set)
  if node_set[x_root][1] > node_set[y_root][1]:
    node_set[y_root][0] = x_root
  else:
    if node_set[x_root][1] == node_set[y_root][1]:
       node_set[y_root][1] +=1 
    node_set[x_root][0] = y_root

def init_nodes(node_num):
  node_set = {x: [x, 0] for x in range(1, node_num+1)}
  return node_set

def is_different_set(edge, node_set):
  if find(edge[0], node_set) == find(edge[1], node_set):
    return False
  else:
    return True

def calc_max_spacing(max_clusters, clusters, node_set, sorted_edges):
  while max_clusters < clusters:
    min_edge = sorted_edges.pop(0)
    if is_different_set(min_edge, node_set):
      union(min_edge, node_set)
      clusters -= 1

  min_edge = sorted_edges.pop(0)
  while not is_different_set(min_edge, node_set):
    min_edge = sorted_edges.pop(0)

  return min_edge

def main():

  filename = 'clustering1.txt'
  G_info, sorted_edges  = process_text(filename)

  max_clusters = 4
  clusters = G_info[0]

  node_set = init_nodes(clusters)

#  print clusters
#  print node_set[1][0]
#  print sorted_edges[0:100]

  max_spacing = calc_max_spacing(max_clusters, clusters, node_set, sorted_edges)

  print max_spacing 

if __name__ == '__main__':
  main()
