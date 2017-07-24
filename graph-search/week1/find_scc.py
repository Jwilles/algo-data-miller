from resource import setrlimit
from sys import setrecursionlimit
setrecursionlimit(4000000)
#setrlimit(resource.RLIMIT_STACK, (10**10, 10**10))

#f = open('SCC.txt', 'r')
#line_list = f.read().split(' \n')
#list_master = {int(line.split()[0]): [int(val) for val in line.split()[1:] if val] for line in line_list if line}
#print line_list[-1]
# last vertex = 875714
explored_vertices = []
t = 1
finishing_time = {}

def dfs(graph, start):
  global t
  explored_vertices.append(start)
 
  if start in graph:
    for edge in graph[start]:
      if edge not in  explored_vertices:
        dfs(graph, edge) 

  finishing_time[start] = t
  t = t + 1

def dfs_loop(graph):
  s = 0
  vertex_num = 875714
  
  #explored_vertices = []

  for vertex in range(vertex_num, 0, -1):
    if vertex not in explored_vertices: 
      dfs(graph, vertex)
  print finishing_time

def main():

  f = open('SCC.txt', 'r')
  line_list = f.read().split(' \n')
  del line_list[-1]

  print line_list[0:10]

  graph = {}
  graph_rev = {}

  t = 0
  for line in line_list:
    if line:
      split_line = line.split()
      vertex = int(split_line[0])
      edge = int(split_line[1])
      if vertex in graph:
        graph[vertex].append(edge)
      else:
        graph[vertex] = [edge]
      if edge in graph_rev:
        graph_rev[edge].append(vertex)
      else:
        graph_rev[edge] = [vertex]


  print graph[17365]
  print graph_rev[1]

  dfs_loop(graph)
      
    
  
    
    
    


#  G = {1: [2,3,3], 2:[1,3], 3:[1,1,2]}
#  for i in range(1, 200*200):
#    G = List_master
#    while len(G.keys()) > 2:
#      n1 = rand.choice(G.keys())
#      n2 = rand.choice(G[n1])
#      #n1 = 1
#      #n2 = 3
#      G[n1].extend(G[n2])
#      del G[n2]
#      for vertex in G.keys():
#        for edge in G[vertex]:
#          if edge == n2:
#            G[vertex][G[vertex].index(edge)] = n1
#      # Remove self loops
#      G[n1] = [edge for edge in G[n1] if edge != n1]
#      cut = len(G[G.keys()[0]])
#    if min_cut and cut < min_cut:
#      print min_cut
#      min_cut = cut  
#  print min_cut
#  
if __name__ == '__main__':
  main()
