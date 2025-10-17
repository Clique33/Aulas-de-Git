# Resolução Prova - Frontend Python

Interface gráfica em **Tkinter** para executar funções presentes em arquivos Python com o nome padrão `resolucao-prova`, como `resolucao-prova1-a.py`, `resolucao-prova1-b.py` etc.

## Descrição

O projeto fornece uma interface que permite carregar automaticamente qualquer arquivo Python na pasta cujo nome comece com `resolucao-prova`, listar as funções nele contidas e executá-las com argumentos definidos pelo usuário.

O sistema foi criado para facilitar o teste e a organização de questões resolvidas em Python dentro de um ou mais arquivos com o mesmo padrão de nome.

---

## Estrutura do projeto

```
/ (pasta do projeto)
├─ frontend.py              # Interface Tkinter para executar funções
├─ resolucao-prova1-a.py    # Exemplo de arquivo com as resoluções
├─ resolucao-prova1-b.py    # Outro arquivo opcional
├─ README.md                # Este arquivo
└─ (outros arquivos opcionais)
```

---

## Requisitos

* Python 3.8+
* Tkinter (instalado por padrão no Python)

Para garantir que o Tkinter esteja instalado no Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-tk
```

---

## Como usar

1. Copie os arquivos `frontend.py` e seus arquivos de resolução (`resolucao-provaX.py`) para a mesma pasta.
2. Execute o frontend:

```bash
python3 frontend.py
```

3. Na interface:

   * Clique em **Carregar Questões** para detectar automaticamente todos os arquivos que começam com `resolucao-prova`;
   * Selecione o arquivo e a função desejada;
   * Insira os argumentos necessários e clique em **Executar**;
   * O resultado será exibido em uma janela de saída.

---

## Padrão dos arquivos `resolucao-prova*.py`

Cada arquivo deve conter as resoluções organizadas como funções. Por exemplo:

```python
# resolucao-prova1-b.py

def questao1(a, b):
    return a + b

def questao2(x):
    return x ** 2

if __name__ == "__main__":
    print(questao1(2, 3))
    print(questao2(5))
```

A interface detectará automaticamente todas as funções definidas nos arquivos encontrados.

---

## Ajuste no `frontend.py`

A busca foi configurada para encontrar qualquer arquivo com o padrão **`resolucao-prova`**, por exemplo:

```python
if filename.startswith("resolucao-prova") and filename.endswith(".py"):
```

Dessa forma, o sistema funciona com múltiplas versões e provas diferentes (ex.: `resolucao-prova1-a.py`, `resolucao-prova1-b.py`, etc.).

---

## Segurança

O script executa código Python importado dinamicamente, portanto:

* Execute apenas arquivos de fontes seguras;
* Evite incluir código que modifique o sistema ou faça chamadas externas não controladas.

---

## Contribuindo

1. Faça um fork do repositório;
2. Crie uma branch para sua alteração (`git checkout -b minha-alteracao`);
3. Faça o commit e envie um pull request.

---

## Licença

Projeto licenciado sob a **MIT License**. Pode ser usado e modificado livremente.

```text
MIT License
Copyright (c) 2025
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions: ...
```

---

## Próximos passos sugeridos

* Garantir que o `frontend.py` suporte múltiplos arquivos simultaneamente.
* Criar funções padronizadas (ex.: `questao1()`, `questao2()`, etc.) dentro de cada arquivo.
* Adicionar suporte a argumentos nomeados e validação automática de tipos (opcional).


