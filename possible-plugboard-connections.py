from itertools import permutations

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num_alp = 26
alphabet = [y for y in alphabet[:num_alp]]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]

total_connections = [[pair] for pair in possible_pairs]

currentStep = total_connections.copy()
iter = 0

num_conns = len(total_connections)

for num_conn in range(2, 10):
    num_conns = 0
    lastStep = currentStep
    currentStep = []
    for i in lastStep:
        used = [y for a in i for y in a]
        
        available = [(y, z) for y, z in possible_pairs if (y not in used) and (z not in used)]
        perms = permutations(range(num_conn))
        for conn in available:
            conns = i.copy()
            conns.append(conn)
            for perm in perms:
              a_list = [conns[i] for i in perm]
              if a_list in currentStep:
                break
            else:
              num_conns += 1
              currentStep.append(conns)
        #print(conns)

    #total_connections.extend(currentStep)
    with open('combinations.txt', 'a') as f:
      for line in currentStep:
        f.write(str(line) + '\n')

    x = 0
    # for conn in currentStep:
    #   print(conn, x)
    #   perms = permutations(range(2))
    #   for perm in perms:
    #     a_list = [conn[i] for i in perm]
    #     if a_list in currentStep:
    #       x += 1
    # print(x)
    print(num_conn, num_conns)


#print(len(total_connections))
