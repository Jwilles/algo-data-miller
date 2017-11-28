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

  filename = 'g1.txt'
  G_info, G, edges = process_text(filename)
  n = G_info[0]

  A = np.full((n,n), 1000000000, dtype='uint64')

#  print edges

  print 'f1'

  for i in range(n):
    A[i, i] = 0

  print 'f2'

  for edge in edges:
    A[edge[0], edge[1]] = edge[2]

  print 'f3'

  for k in range(n):
    print k
    for i in range(n):
      for j in range(n):
        if A[i,j] > A[i,k] + A[k,j]:
          print A[i,k] + A[k,j]
          A[i,j] = A[i,k] + A[k,j]

  print 'f4'

  print A(n-1, n-1) 
#  A = np.zeros((n,n,n))
#
#  for k in range(n):
#    for i in range(n):
#      for j in range(n):
#        A[i,j,k] = min(A[i,j,k-1], (A[i,k,k-1] + A[k,j,k-1]))
#  print A
  
#  print G_info
#  print G[1]


if __name__ == '__main__':
  main()
