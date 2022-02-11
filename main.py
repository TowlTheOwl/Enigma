#https://www.cryptomuseum.com/crypto/enigma/wiring.htm

def enigmaI(reflectorType):
  I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  IV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  V = "VZBRGITYUPSDNHLXAWMJQOFECK"
  reflectors = ["EJMZALYXVBWFCRQUONTSPIKHGD", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "FVPJIAOYEDRZXWGCTKUQSBNMHL"]
  return I, II, III, IV, V, reflectors[reflectorType]

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

refType = input("""
Choose Reflector:
1) UKW-A
2) UKW-B
3) UKW-C
> """)

while refType not in ["1", "2", "3"]:
  refType = input("Invalid. Please choose a reflector type: ")
refType = int(refType) -1

rotor1, rotor2, rotor3, rotor4, rotor5, reflector = enigmaI(refType)

out = ""

print(f"""
rotor 1: {rotor1}
rotor 2: {rotor2}
rotor 3: {rotor3}
rotor 4: {rotor4}
rotor 5: {rotor5}
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

starting_pos = input("Set r4 as: ")
if starting_pos in alphabet:
  rotor4 = set_rotor(rotor4, starting_pos)

starting_pos = input("Set r5 as: ")
if starting_pos in alphabet:
  rotor5 = set_rotor(rotor5, starting_pos)

print(f"""
rotor 1: {rotor1}
rotor 2: {rotor2}
rotor 3: {rotor3}
rotor 4: {rotor4}
rotor 5: {rotor5}
reflector: {reflector}
""")

sentence = input("> ")

sentence = sentence.upper()



rotor_names = ["rotor1", "rotor2", "rotor3", "rotor4", "rotor5", "reflector"]
rotor_names2 = ["rotor5", "rotor4", "rotor3", "rotor2", "rotor1"]

for char in sentence:
  if char in alphabet:
    print("Char: " + char)
    rotor1 = rotate_rotor(rotor1)
    rotor_sequence1 = [rotor1, rotor2, rotor3, rotor4, rotor5, reflector]
    rotor_sequence2 = [rotor5, rotor4, rotor3, rotor2, rotor1]
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
    out += char
  else:
    out += char
print(f"OUTPUT: {out}")
