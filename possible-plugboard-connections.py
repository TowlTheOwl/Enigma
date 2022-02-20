from itertools import permutations
import time

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num_alp = 26
alphabet = [y for y in alphabet[:num_alp]]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]

total_connections = [[pair] for pair in possible_pairs]

currentStep = total_connections.copy()
iter = 0

num_conns = len(total_connections)
print(1, num_conns)

for num_conn in range(2, 10):
    start = time.perf_counter()
    num_conns = 0
    lastStep = currentStep.copy()
    currentStep = []
    perms = permutations(range(num_conn))
    perms = list(perms)
    for i in lastStep:
        used = [y for a in i for y in a]
        available = [(y, z) for y, z in possible_pairs if (y not in used) and (z not in used)]
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

    # with open('combinations.txt', 'a') as f:
    #     for line in currentStep:
    #         f.write(str(line) + '\n')
    end = time.perf_counter()
    print(num_conn, num_conns, str(end-start))

# print(len(total_connections))
