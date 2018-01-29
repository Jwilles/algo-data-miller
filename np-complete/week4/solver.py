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

def is_satisfiable(clauses):
  
  node_hash = {}

  for clause in clauses:
    node_hash[abs(clause[0])] = True
    node_hash[abs(clause[1])] = True

  n = len(node_hash.keys())

  print n
  print node_hash
  
  satisfied = False

  for i in range(0, int(math.log(n, 2))):
    solution = random_assignment(node_hash)
    for k in range(0, 2*n*n):
      satisfied, failed_clause = check_satisfiability(solution, clauses)
      if (satisfied == False):
        solution = flip_clause(solution, failed_clause)
      elif (satisfied == True):
        return satisfied

  return satisfied 
        

def check_satisfiability(solution, clauses):
 
  total_sat = True
  failed_clause = ()

  for clause in clauses:
    clause_sat = False
    for element in clause:
      sol = solution[abs(element)]
      if (element < 0 and sol == False):
        clause_sat = True 
      elif (element > 0 and sol == True):
        clause_sat = True
    if (clause_sat == False):
      total_sat = False
      failed_clause = clause
      break

  return total_sat, failed_clause

def flip_clause(solution, failed_clause):

  rand_num = random()
  if rand_num < 0.5:
    solution[abs(failed_clause[0])] = not solution[abs(failed_clause[0])]
  else:  
    solution[abs(failed_clause[1])] = not solution[abs(failed_clause[1])]

  return solution
    


def main():

  filename = '2sat6.txt'
  S_info, clauses = process_text(filename)

  num_clauses = S_info + 1
  reduced_num_clauses = S_info

  while (num_clauses != reduced_num_clauses):
    num_clauses = reduced_num_clauses
    clauses = reduce_clauses(clauses)
    reduced_num_clauses = len(clauses)

  print len(clauses)
  print clauses

  satisfied = is_satisfiable(clauses)

  print satisfied

if __name__ == '__main__':
  main()
