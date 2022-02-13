#https://www.cryptomuseum.com/crypto/enigma/wiring.htm

def enigmaI(i, ii, iii, reflectorType):
  I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  V = "VZBRGITYUPSDNHLXAWMJQOFECK"
  rotors = [I, II, III, IV, V]
  reflectors = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
  return rotors[i - 1], rotors[ii - 1], rotors[iii - 1], reflectors[reflectorType]

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


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



plugboard = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
used_pb = []
plugboard_setup = False
while not plugboard_setup:
  pb1 = input("Establish plugboard connection (Press Enter to skip): ")

  if (len(pb1) == 1) and (pb1 in alphabet) and (pb1 not in used_pb):
    pb2 = input("Establish plugboard connection 2 (Press Enter to skip): ")

    if (len(pb2) == 1) and (pb2 in alphabet) and (pb2 not in used_pb):
      print('Establishing...')
      used_pb.extend([pb1, pb2])
      plugboard = list(plugboard)
      index1 = plugboard.index(pb1)
      index2 = plugboard.index(pb2)
      plugboard[index1] = pb2
      plugboard[index2] = pb1
      plugboard = "".join(plugboard)
    elif pb2 == "":
      break
    else:
      print("Invalid input. Please try again: ")

  elif pb1 == "":
    break

  else:
    print("Invalid input. Please try again: ")

print(plugboard)

refType = input("""
Choose Reflector:
1) UKW-A
2) UKW-B
3) UKW-C
> """)

while refType not in ["1", "2", "3"]:
  refType = input("Invalid. Please choose a reflector type: ")
refType = int(refType) -1

r1 = int(input("Please choose the first rotor: "))
r2 = int(input("Please choose the second rotor: "))
r3 = int(input("Please choose the third rotor: "))

rotor1, rotor2, rotor3, reflector = enigmaI(r1, r2, r3, refType)

out = ""

print(f"""
rotor 1: {rotor1}
rotor 2: {rotor2}
rotor 3: {rotor3}
reflector: {reflector}
""")

starting_pos = input("Set r1 as: ")
if starting_pos in alphabet:
  rotor1 = set_rotor(rotor1, starting_pos)

starting_pos = input("Set r2 as: ")
if starting_pos in alphabet:
  rotor2 = set_rotor(rotor2, starting_pos)

starting_pos = input("Set r3 as: ")
if starting_pos in alphabet:
  rotor3 = set_rotor(rotor3, starting_pos)

print(f"""
rotor 1: {rotor1}
rotor 2: {rotor2}
rotor 3: {rotor3}
reflector: {reflector}
""")

sentence = input("> ")

sentence = sentence.upper()



rotor_names = ["rotor1", "rotor2", "rotor3", "reflector"]
rotor_names2 = ["rotor3", "rotor2", "rotor1"]

for char in sentence:
  if char in alphabet:
    print("Char: " + char)
    char = plugboard[alphabet.index(char)]
    rotor1 = rotate_rotor(rotor1)
    rotor_sequence1 = [rotor1, rotor2, rotor3, reflector]
    rotor_sequence2 = [rotor3, rotor2, rotor1]
    for i in range(len(rotor_sequence1)):
      print(f"""{rotor_names[i]}:
      {char}
  {alphabet}
  {rotor_sequence1[i]}""")
      char = pass_through(char, rotor_sequence1[i])
      print(char)
    for i in range(len(rotor_sequence2)):
      print(f"""{rotor_names2[i]}:
      {char}
  {alphabet}
  {rotor_sequence2[i]}""")
      char = back_through(char, rotor_sequence2[i])
      print(char)
    char = plugboard[alphabet.index(char)]
    out += char
  else:
    out += char
print(f"OUTPUT: {out}")
