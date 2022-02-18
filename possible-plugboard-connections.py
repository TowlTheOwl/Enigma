import numpy as np
from collections import Counter
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num_alp = 26
alphabet = [y for y in alphabet[:num_alp]]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]

total_connections = [[pair] for pair in possible_pairs]

s = 0

for i in range(len(possible_pairs)):
  connection2 = []
  pair = possible_pairs[i]

  if len(possible_pairs) - i >= 2:
    connection2 = [[pair, possible_pairs[i:][b]] for b in range(len(possible_pairs[i:]))]
    #print(connection2)
    

  # if len(possible_pairs) - i >= 3:
  #   connection3 = [[pair, possible_pairs[i:][b], possible_pairs[b+1:][c]] for b in range(len(possible_pairs[i:])) for c in range(len(possible_pairs[b+1:]))]
  #   connection3 = np.array(connection3)
  temp = connection2.copy()
  temp2 = []
  delete_list = []
  for i in range(len(temp)):
    item = temp[i]
    
    used = [letter for tup in item for letter in tup]
    unique, counts = np.unique(used, return_counts=True)
    if max(counts) == 1:
      temp2.append(temp[i])
    
  connection2 = temp2.copy()
  
  for _ in range(len(connection2)):
    s += 1
    #print(connection2[_])
    #time.sleep(10)
    
  

print(s)
