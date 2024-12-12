from datetime import datetime
import time
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from tkinter import *

# Variáveis globais
limite_max = []
limite_min = []
#AGORA É FAZER UM TRATAMENTO DE ERRO DECENTE to fazendo kkk
def salvar_valores():
    # Lê os valores inseridos pelo usuário
    global limite_max, limite_min
    valores_max = entrada_max.get()
    valores_min = entrada_min.get()
    #validação, deu um erro que fechou a janela antes de aparecer o erro escrito na interface
    try:
        valores_max = entrada_max.get().split(',')
        valores_min = entrada_min.get().split(',')
        if len(valores_max) == 2 and len(valores_min) == 2:
            limite_max = [float(valores_max[0]), float(valores_max[1])]
            limite_min = [float(valores_min[0]), float(valores_min[1])]
            print(f"Limite Máximo: {limite_max}")
            print(f"Limite Mínimo: {limite_min}")
        else:
            info_erro1 = Label(janela, text='Certifique-se de fornecer exatamente dois valores primeiro para BTC e o segundo para ETH')
            info_erro1.pack(pady = 1)
            print("Erro: Certifique-se de fornecer exatamente dois valores para cada limite.")
    except (ValueError, IndexError):
            info_erro2 = Label(janela, text='Digite os Preços no formato pedido')
            info_erro2.pack(pady = 1)
            print("Erro: Certifique-se de digitar os valores no formato correto (ex: 105000.00, 3850.00)")
            # Converte os valores para float e os armazena nas variáveis

def iniciar_sistema():
    salvar_valores() 
    global sistema_iniciado  # Define uma flag global para controle
    sistema_iniciado = True  # Altera o estado da flag
    janela.destroy()         # Fecha a janela e permite o restante do código ser executado

#JANELA ABERTA
janela = Tk()
janela.title('Preços máximos e mínimos venda e compra de criptos')

comando =Label(janela, text='Digite os valores pedidos abaixo no formato (105000.00, 3850.00)')
comando.pack(pady = 5)

info1 = Label(janela, text='Digite o Preço que deseja ser notificado para venda de (BTC, ETH):')
info1.pack(pady = 1)
entrada_max = Entry(janela)#caixa de digitação
entrada_max.pack()

info2 = Label(janela, text='Digite o Preço que deseja ser notificado para compra de (BTC, ETH):')
info2.pack(pady = 1)
entrada_min = Entry(janela)#caixa de digitação
entrada_min.pack()

#botão de confirmação
Button(janela, text='OK',command = iniciar_sistema).pack(pady = 5)

# Instrução
info3 =Label(janela, text='Clique em OK pra continuar o sistema')
info3.pack(pady = 10)

janela.mainloop()

if sistema_iniciado:
    print('-----------------------FDGEREG--------------------')

