# resolucao_prova1b.py — arquivo consolidado
# (gerado por merge_resolucoes.py)

# ===== Início: q1_v1.py =====

def q1(numero1:float, numero2:float):
	return numero1 - numero2

print (q1(5.0,2.0))
print (q1(42.0,42.0))
print (q1(3.3,17.5))
# ===== Fim: q1_v1.py =====

# ===== Início: q4_v1.py =====
def vogais_pares(str1:str, str2:str):
    vogais = 'aeiouAEIOU'
    
    def contar_vogais_pares(s):
        count = 0
        for i in range(0, len(s), 2):
            if s[i] in vogais:
                count += 1
        # O return deve estar AQUI, fora do loop 'for'
        return count
    
    # As chamadas das funções e o retorno final devem estar AQUI,
    # dentro da função principal 'vogais_pares', mas fora da função aninhada.
    count1 = contar_vogais_pares(str1)
    count2 = contar_vogais_pares(str2)
    
    # Se os contadores forem iguais, retorna str1 (conforme sua lógica original)
    return str1 if count1 >= count2 else str2
        
print(vogais_pares('casamento','processo'))
print(vogais_pares('manufacturer','headquarters'))
# ===== Fim: q4_v1.py =====

# ===== Início: q5_v1.py =====
def vogais_pares(str1:str, str2:str):
    vogais = 'aeiouAEIOU'
    
    def contar_vogais_pares(s):
        count = 0
        for i in range(0, len(s), 2):
            if s[i] in vogais:
                count += 1
        # O return deve estar AQUI, fora do loop 'for'
        return count
    
    # As chamadas das funções e o retorno final devem estar AQUI,
    # dentro da função principal 'vogais_pares', mas fora da função aninhada.
    count1 = contar_vogais_pares(str1)
    count2 = contar_vogais_pares(str2)
    
    # Se os contadores forem iguais, retorna str1 (conforme sua lógica original)
    return str1 if count1 >= count2 else str2
        
print(vogais_pares('casamento','processo'))
print(vogais_pares('manufacturer','headquarters'))
# ===== Fim: q5_v1.py =====

# ===== Início: exercicios/LucasSLL/ex2.py =====
def paridade(a: int, b: int) -> str:
    pa, pb = (a % 2 == 0), (b % 2 == 0)
    if pa and pb:
        return "ambos são pares"
    if not pa and not pb:
        return "ambos são ímpares"
    return "um é par e o outro é ímpar"

if __name__ == "__main__":
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite outro número inteiro: "))
    print(paridade(a, b))
# ===== Fim: exercicios/LucasSLL/ex2.py =====

# ===== Início: exercicios/LucasSLL/ex6.py =====

# ===== Fim: exercicios/LucasSLL/ex6.py =====

if __name__ == "__main__":
    # Você pode testar aqui chamando as funções importadas acima.
    # Ex.: print(compara(5,2)) ou print(eh_semiprimo(77))
    pass
