import numpy as np
import operator

def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = map(int, f[0][:-1].split(" "))
  edge_list = [map(operator.sub, map(int, line[:-1].split(" ")), [1,1,0]) for line in f[1:]]

  graph = {}

  for edge in edge_list:
    graph.setdefault(edge[0],[]).append(edge[1:])
    graph.setdefault(edge[1],[]).append([edge[0], edge[2]])

  return graph_info, graph, edge_list


def main():

  filename = 'g3.txt'
  G_info, G, edges = process_text(filename)
  n = G_info[0]

  A = [[100000000000000000 for x in range(n)] for y in range(n)]

  for i in range(n):
    A[i][i] = 0


  for edge in edges:
    A[edge[0]][edge[1]] = edge[2]

  for k in range(n):
    print k
    for i in range(n):
      for j in range(n):
        if A[i][j] > A[i][k] + A[k][j]:
          A[i][j] = A[i][k] + A[k][j]

  for i in range(n):
    if A[i][i] < 0:
      print 'neg_cycle'

  min_path = 100000000000000000

  for i in range(n):
    for j in range(n):
      if A[i][j] < min_path:
        min_path = A[i][j]

  print min_path


if __name__ == '__main__':
  main()
