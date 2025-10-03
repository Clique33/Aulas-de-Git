import tkinter as tk
from tkinter import messagebox
import importlib.util
import inspect
import os

funcoes = {}
entradas = {}

def carregar_arquivos():
    global funcoes
    funcoes.clear()
    lista_questoes.delete(0, tk.END)

    # pega todos os arquivos que começam com 'q' e terminam com '.py'
    arquivos = [f for f in os.listdir() if f.startswith("q") and f.endswith(".py")]

    if not arquivos:
        messagebox.showwarning("Aviso", "Nenhum arquivo de questão encontrado na pasta!")
        return

    for arquivo in arquivos:
        nome_modulo = arquivo.replace(".py", "")
        spec = importlib.util.spec_from_file_location(nome_modulo, arquivo)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)

        # pega todas as funções do arquivo
        for name, f in inspect.getmembers(modulo, inspect.isfunction):
            funcoes[name] = f
            lista_questoes.insert(tk.END, name)

def selecionar_questao():
    selecao = lista_questoes.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione uma função primeiro!")
        return
    nome_funcao = lista_questoes.get(selecao[0])
    funcao = funcoes[nome_funcao]

    parametros = inspect.signature(funcao).parameters
    label_questao.config(text=f"Selecionada: {nome_funcao}({', '.join(parametros)})")

    # limpar campos antigos
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    entradas.clear()

    # criar entradas para cada parâmetro
    for p in parametros:
        lbl = tk.Label(frame_inputs, text=p)
        lbl.pack()
        entry = tk.Entry(frame_inputs)
        entry.pack()
        entradas[p] = entry

def calcular():
    selecao = lista_questoes.curselection()
    if not selecao:
        messagebox.showwarning("Aviso", "Selecione uma função primeiro!")
        return
    
    nome_funcao = lista_questoes.get(selecao[0])
    funcao = funcoes[nome_funcao]

    try:
        # tenta converter para float, se der erro usa string
        args = []
        for entry in entradas.values():
            valor = entry.get()
            try:
                valor = float(valor)
            except ValueError:
                pass  # mantém string
            args.append(valor)

        resultado = funcao(*args)
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao executar: {e}")

# --- GUI ---
root = tk.Tk()
root.title("Frontend Questões - Python")

btn_carregar = tk.Button(root, text="Carregar Questões", command=carregar_arquivos)
btn_carregar.pack()

lista_questoes = tk.Listbox(root, width=50, height=10)
lista_questoes.pack()

btn_selecionar = tk.Button(root, text="Selecionar Função", command=selecionar_questao)
btn_selecionar.pack()

label_questao = tk.Label(root, text="Selecionada: Nenhuma")
label_questao.pack()

frame_inputs = tk.Frame(root)
frame_inputs.pack()

btn_calcular = tk.Button(root, text="Executar", command=calcular)
btn_calcular.pack()

root.mainloop()
