import json

# Parseando o arquivo json em uma lista
with open('dados.json', encoding= 'utf-8') as meu_json:
    faturamento = json.load(meu_json)

# Criando uma lista somente com valores positivos para encontrar o valor mínimo diferente de zero
faturamento_positivo = []
i = 0
soma = 0
for i in range(len(faturamento)):
    if faturamento[i]['valor'] != 0:
        faturamento_positivo.append(faturamento[i])
        soma = soma + faturamento[i]['valor'] #Aproveitando a repetição para somar o valor total de faturamento, será usado para calcular a média


menor = min(faturamento_positivo, key=lambda faturamento_positivo : faturamento_positivo['valor'])
maior = max(faturamento, key=lambda faturamento : faturamento['valor'])
media = soma / len(faturamento)

contador = 0
for i in range(len(faturamento)):
    if faturamento[i]['valor'] > media:
        contador = contador + 1

print(f"Para o faturamento informado: \n1. O menor valor de faturamento foi R${menor['valor']:.2f}. \n2. O maior valor de faturamento foi R${maior['valor']:.2f}.")
print(f"3. A média mensal de faturamento foi de R${media:.2f} e o faturamento de {contador} dias foi superior à essa média.")
print("**Valores formatados para apenas 2 casas após a vírgula. Os cálculos foram feitos considerando o valor inteiro.")