import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def enigmaI(i, ii, iii):
  I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  V = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotors = [I, II, III, IV, V]
  return rotors[i], rotors[ii], rotors[iii]

def rotate_rotor(rotor):
  return rotor[1:] + rotor[0]

def set_rotor(rotor, pos):
  while rotor[0] != pos:
    rotor = rotor[1:] + rotor[0]
  return rotor

def pass_through(char, rotor):
  return rotor[alphabet.index(char)]

def back_through(char, rotor):
  return alphabet[rotor.index(char)]

word_set = False

while not word_set:
    word1 = input("Encoded string: ")
    word1 = word1.upper()
    word2 = input("Decode to: ")
    word2 = word2.upper()
    if len(word1) == len(word2):
        break
    if (word1 == "") or (word2 == ""):
        quit()


rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotor4 = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotor5 = "VZBRGITYUPSDNHLXAWMJQOFECK"
reflectors = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
ref_names = ["UKW-A", "UKW-B", "UKW-C"]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

plugboard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
used_pb = []

LENGTH = 6591000
found_combinations = 0
completed = 0
found_combs = []
percentage_display = []
for i in range(0, 1001):
  percentage_display.append(i/10)

for ref in range(len(reflectors)):
    for i in alphabet:
        for ii in alphabet:
            for iii in alphabet:
                for r1 in range(5):
                    for r2 in range(5):
                        for r3 in range(5):
                            out = ""
                            rotor1, rotor2, rotor3 = enigmaI(r1, r2, r3)
                            rotor1 = set_rotor(rotor1, i)
                            rotor2 = set_rotor(rotor2, ii)
                            rotor3 = set_rotor(rotor3, iii)
                            reflector = reflectors[ref]

                            #COMPUTE
                            for char in word1:
                                if char in alphabet:
                                    char = plugboard[alphabet.index(char)]
                                    rotor1 = rotate_rotor(rotor1)
                                    rotor_sequence1 = [rotor1, rotor2, rotor3, reflector]
                                    rotor_sequence2 = [rotor3, rotor2, rotor1]
                                    for j in range(len(rotor_sequence1)):
                                        char = pass_through(char, rotor_sequence1[j])
                                    for j in range(len(rotor_sequence2)):
                                        char = back_through(char, rotor_sequence2[j])
                                    char = plugboard[alphabet.index(char)]
                                    out += char
                                else:
                                    out += char
                            completed += 1
                            if completed % 1000 == 0:
                              print(f"{int(completed/1000)}/{int(LENGTH/1000)} | {round((completed/LENGTH)*100, 2)} %")
                            if out == word2:
                                found_combs.append(f"Reflector: {ref_names[ref]}, rotor1: {r1 + 1}, rotor2: {r2 + 1}, rotor3: {r3+1}, r1 start pos: {i}, r2 start pos: {ii}, r3 start pos: {iii}")
                                found_combinations += 1
print(f"TOTAL COMBINATIONS: {found_combinations}")

for setting in found_combs:
  print(setting)
print("COMPLETED!")
