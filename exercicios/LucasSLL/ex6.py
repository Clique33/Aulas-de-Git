def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def eh_semiprimo(n: int) -> bool:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:   # achou divisor
            j = n // i   # o outro fator
            if eh_primo(i) and eh_primo(j):
                return True
    return False


# Testes
print(eh_semiprimo(10))   
print(eh_semiprimo(18))    
print(eh_semiprimo(27))    
print(eh_semiprimo(77))   
print(eh_semiprimo(8000)) 
