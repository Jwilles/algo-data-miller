

# find shortest path distances to the following vertices from source
# 7,37,59,82,99,115,133,165,188,197

def process_graph(filename):

  graph = {}

  f = open(filename, 'r')
  line_list = f.readlines()#.split('\n')

  for line in line_list:

    split_line = line.split()
    edges = {}

    for edge in split_line[1:]:

      split_edge = edge.split(',')
      edges[int(split_edge[0])] = int(split_edge[1])
      
    graph[int(split_line[0])] = edges

  return graph 

def dijkstra(graph):
 
  processed_vertices = []
  shortest_paths = {}
  
  source_vertex = 1

  processed_vertices.append(source_vertex)
  shortest_paths[source_vertex] = 0

  vertices = set(range(1,201))
  #vertices = set(range(1,8))


  while vertices != set(processed_vertices):
   
    djk_criterion = {}

    for tail in processed_vertices:
      for head in graph[tail].keys():
        if head not in processed_vertices:
          djk_criterion[head] = shortest_paths[tail] + graph[tail][head]
  
    print djk_criterion
    min_criterion = min(djk_criterion.items(), key=lambda x: x[1])     
    print min_criterion
    processed_vertices.append(min_criterion[0])
    shortest_paths[min_criterion[0]] = min_criterion[1]   
#    print processed_vertices
    
  
  return shortest_paths

def main():

  graph_filename = 'dijkstra_data.txt'
#  graph_filename = 'test_djk.txt'
  graph = process_graph(graph_filename)

  goal_distances = [7,37,59,82,99,115,133,165,188,197]
#  goal_distances = [1,2,3,4,5,6,7,8]

  
  shortest_paths = dijkstra(graph)
  print shortest_paths
 
  for i in range(0, len(goal_distances)):
    #print goal_distances[i]
    print shortest_paths[goal_distances[i]]
    #print '-'*50

if __name__ == '__main__':
  main()
