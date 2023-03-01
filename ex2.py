a = 0
b = 1
lista = []
lista.append(a)

for i in range(80):
    a, b = b, a + b
    lista.append(a)

num = int(input("Informe um número para verificar se ele está entre os 80 primeiros números da escala Fibonacci: "))

if (num in lista):
    print(f"\nO número {num} está entre os 80 primeiros números da escala")
else:
    print(f"\nO número {num} não está na escala Fibonacci")