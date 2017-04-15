import math 
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

print x*y

def multiply(x,y):

  if len(str(x)) == 1 or len(str(y)) == 1:
    return x*y 
  else:

    n = max(len(str(x)), len(str(y)))/2

    a = x / 10**(n)
    b = x % 10**(n)
    c = y / 10**(n)
    d = y % 10**(n) 
    
    ac = multiply(a, c)    
    ad = multiply(a, d)
    bc = multiply(b, c)
    bd = multiply(b, d)

    return (10**(2*n))*ac + (10**(n))*(ad+bc) + bd

print multiply(x,y)
