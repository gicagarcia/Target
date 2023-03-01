#Definindo os valores informados
SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53
soma = SP + RJ + MG + ES + outros

def percentual(valor1, valor2):
        percentual = (valor1 * 100) / valor2
        return percentual

perc_sp = percentual(SP, soma)
perc_rj = percentual(RJ, soma)
perc_mg = percentual(MG, soma)
perc_es = percentual(ES, soma)
perc_outros = percentual(outros, soma)

print(f"Lista dos estados e seus respectivos percentuais: \nSP: {perc_sp:.2f}% \nRJ: {perc_rj:.2f}% \nMG: {perc_mg:.2f}% \nES: {perc_es:.2f}% \nOutros: {perc_outros:.2f}%")