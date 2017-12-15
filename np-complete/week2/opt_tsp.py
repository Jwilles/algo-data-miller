
def process_text(filename):
  
  f = open(filename, 'r').readlines()
  graph_info = int(f[0][:-1])
  points = [map(float,line[:-1].split(" ")) for line in f[1:]]

  return graph_info, points


def main():

  filename = 'tsp.txt'
  G_info, points = process_text(filename)
 
  print G_info
  print points 



if __name__ == "__main__":
  main()
