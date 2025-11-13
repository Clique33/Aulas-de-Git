import string

def pangrama(frase: str) -> bool:
    alfabeto = set(string.ascii_lowercase)
    
    letras_na_frase = set(frase.lower())
    
    return alfabeto.issubset(letras_na_frase)


print(pangrama("a quick brown fox jumps over the lazy dog"))  
print(pangrama("the five boxing wizards jump quickly"))  


