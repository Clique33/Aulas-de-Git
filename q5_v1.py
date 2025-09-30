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