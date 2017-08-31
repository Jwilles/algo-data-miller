
def process_text(filename):
  f = open(filename, 'r').readlines()
  
  line_dict = {int(line[:-1]): '' for line in f}
  line_list = [int(line[:-1]) for line in f]
  return line_dict, line_list


def main():

  filename = 'int_2_sum.txt'
  #filename = 'median_test_1.txt'
  int_dict, int_list = process_text(filename)


  target_count = 0

  for t in range(-10000, 10000):
#    print t
    for x in int_list:
      y = (t-x)
      if y in int_dict and (x != y):
        target_count += 1 
        break


  print target_count

if __name__ == '__main__':
  main()
