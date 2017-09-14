
def process_text(filename):

  f = open(filename, 'r').readlines()
  
  #line_dict = {int(line[:-1]): '' for line in f}
  event_list = [map(int, line[:-1].split(" ")) for line in f[1:]]
  return event_list


def cost(event):
  cost = event[0]-event[0]
  return cost

def compare(event_a, event_b):
  cost_a = cost(event_a)
  cost_b = cost(event_b)

  if cost_a == cost_b:
    if event_a[0] < event_b[0]:
      return 1
    else:
      return -1
  elif cost_a < cost_b:
    return -1
  else:
    return 1
    

def main():

  filename = 'jobs.txt'
  event_list = process_text(filename)
  
  event_list.sort(compare)

  print event_list

  i = 0
  completion_sum = 0

  for event in event_list:
    i += event[1]
    completion_sum += event[0]*i
  
  print completion_sum

if __name__ == '__main__':
  main()
