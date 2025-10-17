from random import randint

def questao1(a,b):
    if b==0:
        return False
    return a%b==0

def questao2(c):
    frase="A quick brown fox jumps over the lazy dog"
    if len(c)!=1:
        return "não é letra"
    l=c.lower()
    if l<'a' or l>'z':
        return "não é letra"
    if l in "aeiou":
        return "vogal"
    return "consoante"

def questao3(p):
    i=0
    r=""
    while i<len(p):
        if i+1<len(p):
            r+=p[i+1]+p[i]
            i+=2
        else:
            r+=p[i]
            i+=1
    return r

def questao4(s1,s2):
    def contar(s):
        i=0
        c=""
        while i<len(s):
            l=s[i].lower()
            if l>='a' and l<='z' and l not in "aeiou":
                if l not in c:
                    c+=l
            i+=1
        return len(c)
    n1=contar(s1)
    n2=contar(s2)
    if n1>=n2:
        return s1
    return s2

def questao5(s):
    def outra_vogal(v):
        while True:
            i=randint(0,4)
            nv="aeiou"[i]
            if nv!=v:
                return nv
    r=""
    i=0
    while i<len(s):
        c=s[i]
        l=c.lower()
        if l in "aeiou":
            nv=outra_vogal(l)
            if c.isupper():
                nv=nv.upper()
            r+=nv
        else:
            r+=c
        i+=1
    return r

def questao6(n):
    if n==0:
        return False
    if n<0:
        n=-n
    i=2
    while i*i<=n:
        if n%(i*i)==0:
            return False
        i+=1
    return True

