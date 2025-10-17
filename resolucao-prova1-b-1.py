# resolucao-prova1-b.py
# Resoluções das questões da Prova 1 - Grupo B

# ----------------------------------------------------------
# Questão 1
# Escreva uma função em Python que recebe dois números em ponto
# flutuante (float) e retorne se o primeiro é um múltiplo do segundo.
# Ex.: (5, 2) → False
# Ex.: (17, 3.4) → True
# ----------------------------------------------------------

def questao1(a: float, b: float) -> bool:
    """Retorna True se 'a' for múltiplo de 'b', caso contrário False."""
    if b == 0:
        return False  # evita divisão por zero
    return a % b == 0


# ----------------------------------------------------------
# Questão 2
# Escreva uma função que recebe um caractere e retorna
# “vogal”, “consoante” ou “não é letra”.
# Dica: use o pangrama "A quick brown fox jumps over the lazy dog"
# Ex.: 'a' → "vogal"
# Ex.: ':' → "não é letra"
# ----------------------------------------------------------

def questao2(c: str) -> str:
    """Classifica o caractere como vogal, consoante ou não é letra."""
    if len(c) != 1:
        return "não é letra"  # só deve receber um caractere

    letra = c.lower()
    if letra not in "abcdefghijklmnopqrstuvwxyz":
        return "não é letra"
    elif letra in "aeiou":
        return "vogal"
    else:
        return "consoante"


# ----------------------------------------------------------
# Questão 3
# Faça uma função que, dada uma palavra, inverta as letras que estão
# em posições consecutivas, de dois em dois.
# Caso o comprimento seja ímpar, a última letra deve ser mantida.
# Ex.: 'alfabeto' → 'laafebot'
# Ex.: 'onomatopeia' → 'nomotapoiea'
# ----------------------------------------------------------

def questao3(palavra: str) -> str:
    """Inverte as letras de uma palavra de dois em dois caracteres."""
    resultado = ""
    i = 0
    while i < len(palavra) - 1:
        resultado += palavra[i + 1] + palavra[i]
        i += 2
    if len(palavra) % 2 != 0:
        resultado += palavra[-1]
    return resultado


# ----------------------------------------------------------
# Testes rápidos (para rodar diretamente no terminal)
# ----------------------------------------------------------
if __name__ == "__main__":
    # Questão 1
    print(questao1(5, 2))        # False
    print(questao1(17, 3.4))     # True

    # Questão 2
    print(questao2('a'))         # vogal
    print(questao2(':'))         # não é letra
    print(questao2('g'))         # consoante

    # Questão 3
    print(questao3('alfabeto'))       # laafebot
    print(questao3('onomatopeia'))    # nomotapoiea
