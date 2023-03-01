string1 = input("Informe a string que deseja inverter: ")
string_invertida = []

i = len(string1)-1

while i >= 0:
    string_invertida.append(string1[i])
    i -= 1

print(''.join(string_invertida))