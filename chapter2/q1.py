import timeit


def test(i):
  k = x[i]


for i in range(1000, 10000, 100):
  x = list(range(i))
  pop_end = timeit.Timer("test(%d-1)"%i, "from __main__ import x,test")
  print "The time to compute is " +  repr(pop_end.timeit(number=1000)) + " milliseconds for length " + repr(i) 
  


  
  
