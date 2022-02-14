alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

num_alp = 12
alphabet = [y for y in alphabet[:num_alp]]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]


res = []
res.extend([[pair] for pair in possible_pairs])

total_connections = []
total_connections.extend(res)

currentStep = total_connections
iter = 0


for num_conn in range(2, num_alp//2+1):
    print(num_conn)
    lastStep = currentStep
    currentStep = []
    for i in lastStep:
        used = []
        letters = [y for a in i for y in a]

        used.extend(letters)
        available = [(y, z) for y, z in possible_pairs if (y not in used) and (z not in used)]

        for conn in available:
            conns = i.copy()
            conns.append(conn)

            currentStep.append(conns)
        print(conns)

    total_connections.extend(currentStep)


print(len(total_connections))
