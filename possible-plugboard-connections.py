from itertools import combinations

alphabet = [y for y in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

possible_pairs = [(a, b) for idx, a in enumerate(alphabet) for b in alphabet[idx + 1:]]

total_combinations = []

for i in range(1,14):
    total_combinations.extend([j for j in combinations(possible_pairs, i)])

res = []
print(total_combinations)
print(len(total_combinations))
print(len(res))
for k in range(len(total_combinations)):
    comb = total_combinations[k]
    used = []
    letters = [y for a in comb for x in a for y in x]
    for letter in letters:
        if letters.count(letter) > 1:
            break
    else:
        res.append(total_combinations[k])

print(res)
print(len(res))
