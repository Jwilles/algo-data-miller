import heapq as hq


def process_text(filename):
  f = open(filename, 'r').readlines()
  line_list = [int(line[:-1]) for line in f]
  return line_list


def find_median(heap_low, heap_high):
  return

  

def main():

  filename = 'Median.txt'
#  filename = 'median_test_1.txt'
  num_stream = process_text(filename)
  median_sum = 0

  heap_low = []
  heap_high = []

  hq.heapify(heap_low)
  hq.heapify(heap_high)

  for num in num_stream:
    try:
      if num > (-heap_low[0]):
        hq.heappush(heap_high, num)
      elif num < heap_high[0]:
        hq.heappush(heap_low, -num)
    except:
      hq.heappush(heap_low, -num)
   
    low_length = len(heap_low)
    high_length = len(heap_high)
 
    if abs(low_length - high_length) > 1:
      if (low_length < high_length):
        hq.heappush(heap_low, -hq.heappop(heap_high))
      else:
        hq.heappush(heap_high, -hq.heappop(heap_low))


    low_length = len(heap_low)
    high_length = len(heap_high)
#    print heap_high
#    print heap_low
#    print low_length
#    print high_length

    
 
    if low_length == high_length:
      print -heap_low[0]
      median_sum += (-heap_low[0])    
    elif low_length < high_length:
      print heap_high[0]
      median_sum += heap_high[0]
    elif low_length > high_length:
      print -heap_low[0]
      median_sum += (-heap_low[0])    
    

  print median_sum % 10000    
  print len(heap_low)
  print len(heap_high)

if __name__ == '__main__':
  main()
