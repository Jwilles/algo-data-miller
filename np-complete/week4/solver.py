import math
from sets import Set
from random import *


def process_text(filename):
  
  f = open(filename, 'r').readlines()
  S_info = int(f[0][:-1])

  clauses = [] 

  for line in f[1:-1]:
    split_line = line[:-1].split(" ")
    clauses.append((int(split_line[0]), int(split_line[1])))

  return S_info, clauses


def reduce_clauses(clauses):

  T_set = Set()
  N_set = Set()
  
  for clause in clauses:
    for element in clause:
      if element < 0:
        N_set.add(abs(element))
      else:
        T_set.add(element)

  TN_sym_set = T_set.symmetric_difference(N_set)

  reduced_clauses = [clause for clause in clauses if ((abs(clause[0]) not in TN_sym_set) and (abs(clause[1]) not in TN_sym_set))]

  return reduced_clauses


def random_assignment(node_hash):

  for key in node_hash.keys():
    random_num = random()
    if random_num < 0.5:
      node_hash[key] = True
    else:
      node_hash[key] = False

  return node_hash

def is_satisfiability(clauses):
  
  node_hash = {}

  for clause in clauses:
    node_hash[abs(clause[0])] = True
    node_hash[abs(clause[1])] = True

  n = len(node_hash.keys())

  print n
  print node_hash

  for i in range(0, int(math.log(n, 2))):
    solution = random_assignment(node_hash)
    for k in range(0, 2*n*n):
      check_computabilty 
      ## check computability here
      for clause in clauses:
        
      
  return True

def compute_satisfiability(solution, clauses):


def main():

  filename = '2sat1.txt'
  S_info, clauses = process_text(filename)

  num_clauses = S_info + 1
  reduced_num_clauses = S_info

  while (num_clauses != reduced_num_clauses):
    num_clauses = reduced_num_clauses
    clauses = reduce_clauses(clauses)
    reduced_num_clauses = len(clauses)

  print len(clauses)
  print clauses

  satisfied = check_satisfiability(clauses)

if __name__ == '__main__':
  main()
