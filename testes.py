from datetime import datetime
import time
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from tkinter import *

def iniciar_sistema():
    global sistema_iniciado  # Define uma flag global para controle
    sistema_iniciado = True  # Altera o estado da flag
    janela.destroy()         # Fecha a janela e permite o restante do código ser executado

def salvar_valores():
    # Lê os valores inseridos pelo usuário
    valores_max = entrada_max.get().split(',')
    valores_min = entrada_min.get().split(',')
    
    # Converte os valores para float e os armazena nas variáveis
    limite_max = [float(valores_max[0]), float(valores_max[1])]
    limite_min = [float(valores_min[0]), float(valores_min[1])]

    # Exibe os valores no terminal (ou pode usá-los conforme necessário)
    print(f"Limite Máximo: {limite_max}")
    print(f"Limite Mínimo: {limite_min}")

#----ajuda na descrição da label do valor max
def on_focus_in(event):
    """Remove o texto padrão quando o campo recebe foco"""
    if entrada_max.get() == "Preço Mínimo (BTC, ETH)":
        entrada_max.delete(0, END)

def on_focus_out(event):
    """Restaura o texto padrão quando o campo perde foco e está vazio"""
    if entrada_max.get() == "":
        entrada_max.insert(0, "Preço Mínimo (BTC, ETH)")  

#----ajuda na descrição da label do valor min
def on_focus_in(event):
    """Remove o texto padrão quando o campo recebe foco"""
    if entrada_min.get() == "Preço Mínimo (BTC, ETH)":
        entrada_min.delete(0, END)

def on_focus_out(event):
    """Restaura o texto padrão quando o campo perde foco e está vazio"""
    if entrada_min.get() == "":
        entrada_min.insert(0, "Preço Mínimo (BTC, ETH)")  

#JANELA ABERTA
janela = Tk()
janela.title('Preços máximos e mínimos venda e compra de criptos')

comando =Label(janela, text='Digite os valores pedidos abaixo no formato (105000.00, 3850.00)')
comando.pack(pady = 5)

info1 = Label(janela, text='Digite o Preço que deseja ser notificado para venda de (BTC, ETH):')
info1.pack(pady = 1)
entrada_max = Entry(janela)#caixa de digitação
entrada_max.insert(0, "Preço Máximo (BTC, ETH)")  # Texto padrão
entrada_max.bind("<FocusIn>", on_focus_in)  # Remove o texto quando o campo for clicado
entrada_max.bind("<FocusOut>", on_focus_out)  # Restaura o texto se estiver vazio
entrada_max.pack()

info2 = Label(janela, text='Digite o Preço que deseja ser notificado para compra de (BTC, ETH):')
info2.pack(pady = 1)
entrada_min = Entry(janela)#caixa de digitação
entrada_min.insert(0, "Preço Mínimo (BTC, ETH)")  # Texto padrão
entrada_min.bind("<FocusIn>", on_focus_in)  # Remove o texto quando o campo for clicado
entrada_min.bind("<FocusOut>", on_focus_out)  # Restaura o texto se estiver vazio
entrada_max.pack()

#botão de confirmação
confirmacao = Button(janela, text='OK',command = iniciar_sistema)
confirmacao.pack(pady = 5)

# Instrução
info3 =Label(janela, text='Clique em OK pra iniciar o sistema')
info3.pack(pady = 10)

janela.mainloop()

if sistema_iniciado:
    print('-'*60)
    print('-'*60)
    print('-'*60)


