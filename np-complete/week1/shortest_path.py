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

  filename = 'g1.txt'
  G_info, G  = process_text(filename)

  min_shortest_path = shortest_path()

  
  print G_info
  print G[1]


if __name__ == '__main__':
  main()
