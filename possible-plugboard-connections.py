alphabet = [y for y in "ABCDEFG"]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]

print(possible_pairs)
print(len(possible_pairs))

res = []
res.extend([[pair] for pair in possible_pairs])

total_connections = []
total_connections.extend(res)

currentStep = total_connections
iter = 0


for num_conn in range(2, 14):
    print(num_conn)
    lastStep = currentStep
    currentStep = []
    for i in lastStep:
        used = []
        letters = [y for a in i for x in a for y in x]

        used.extend(letters)
        available = [(y, z) for y, z in possible_pairs if (y not in used) and (z not in used)]

        for conn in available:
            conns = i.copy()
            conns.append(conn)
            iter += 1

            currentStep.append(conns)
            if iter == 10000000:
                print(conns)
                iter = 0

    total_connections.extend(currentStep)

print(total_connections)
