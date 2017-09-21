
def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = map(int, f[0][:-1].split(" "))
  sorted_edges = sorted([map(int, line[:-1].split(" ")) for line in f[1:]], key = lambda edge: edge[-1])
  return graph_info, sorted_edges

def find():
  return

def union():
  return

def init_nodes(node_num):
  node_set = {x: x for x in range(1, node_num+1)}
  return node_set

def calc_max_spacing(max_clusters, clusters, node_set, sorted_edges)
  return 2 

def main():

  filename = 'clustering1.txt'
  G_info, sorted_edges  = process_text(filename)

  max_clusters = 4
  clusters = G_info[0]

  node_set = init_nodes(clusters)

  print clusters
  print node_set
  print sorted_edges[0:100]

  max_spacing = calc_max_spacing(max_clusters, clusters, node_set, sorted_edges)


if __name__ == '__main__':
  main()
