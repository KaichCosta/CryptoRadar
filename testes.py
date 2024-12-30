import time
from datetime import datetime
import os
import yfinance as yf
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from tkinter import *
from tkinter import messagebox
import threading
import requests


#2 buscar preços bitcoin e ações atuais
precos = {
    "BTC": {"compra": 0, "venda": 0},  # Armazena preço de compra e venda do Bitcoin
    "ETH": {"compra": 0, "venda": 0}   # Armazena preço de compra e venda do Ethereum
}
def atualizar_preco():
    def tarefa():
        global precos, infohora
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD")
        requisicao_dic = requisicao.json()
        precos["BTC"]["compra"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        precos["BTC"]["venda"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        precos["ETH"]["compra"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        precos["ETH"]["venda"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        
        texto = f'''
        BTC - Compra: {precos["BTC"]["compra"]}, Venda: {precos["BTC"]["venda"]}]
        ETH - Compra: {precos["ETH"]["compra"]}, Venda: {precos["ETH"]["venda"]}]
        '''
        print(texto)
        infopreco.config(text=texto)
        hora = datetime.now()
        infohora.config(text=f'{hora.strftime("%H:%M:%S")}')
    threading.Thread(target=tarefa).start()

# Variáveis globais
sistema_iniciado = False

#TRATAMENTO DE ERRO DECENTE
limites = {
    "BTC": {"compra_min": 0, "venda_max": 0},
    "ETH": {"compra_min": 0, "venda_max": 0}
}
def salvar_valores():
# Limpa qualquer mensagem de erro anterior
    try:
        # Obtém os valores das entradas e atualiza os limites
        limites["BTC"]["compra_min"] = float(entry_btc_compra_min.get())
        limites["BTC"]["venda_max"] = float(entry_btc_venda_max.get())
        limites["ETH"]["compra_min"] = float(entry_eth_compra_min.get())
        limites["ETH"]["venda_max"] = float(entry_eth_venda_max.get())
        
        messagebox.showinfo("Sucesso", "Limites salvos com sucesso!")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos!")

    print(f"Limite Mínimo: ==compra {limites['BTC']['compra_min']}==, //compra {limites['ETH']['compra_min']}//")
    
    print(f"Limite Máximo: ==venda {limites['BTC']['venda_max']}==, //venda {limites['ETH']['venda_max']}//")
    
def iniciar_sistema():
    def tarefa():
        if salvar_valores():
            global sistema_iniciado  # Define uma flag global para controle
            sistema_iniciado = True  # Altera o estado da flag
            ultimo_preco = [("BTC", preco_btc), ("ETH", preco_eth)]
            
            print(f'\033[1;32m{datetime.now()}\033[0m')
            print(ultimo_preco)
            print('\033[1;32m--BITCOIN--ETHEREUM\033[0m')

            for i, (moeda, preco) in enumerate(ultimo_preco):
                max = limite_max[i]
                min = limite_min[i]

            if preco > max:
                print(f'\033[1;31m=== ALERTA DE VENDA===\033[0m')
                print(f'\033[1;31m{moeda}: Preço atual ({preco}) ultrapassou o limite máximo ({max}).\033[0m')

                hora = datetime.now()

                #webbrowser.open('https://web.whatsapp.com/')
                time.sleep(10)

                workbook = openpyxl.load_workbook('contatos-notificados.xlsx')
                pagina_contatos = workbook['Plan1']
    #4 CRIAR UM GRUPO E POR MEU PAI E EU PRA RECEBER ESSAS NOTIFICAÇÕES
                for linha in pagina_contatos.iter_rows(min_row=5):
                    #nome, telefone
                    nome = linha[2].value    
                    telefone = linha[3].value

                    #mensagem que será enviada aos contatos
                    msg = f'Olá {nome}, hora de vender {moeda}, {hora.strftime('%d/%m/%Y, %H:%M')}'

                    #link que abrirá o zap
                    link_mensagem_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'

                    webbrowser.open(link_mensagem_zap)

                    time.sleep(20)
                    pyautogui.press('enter')
                    time.sleep(5)

                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(5)

                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(5)

                    print('FINALIZADO')

            #==============================================
            #==============================================
            elif preco < min:
                print(f'\033[1;31m=== ALERTA DE COMPRA===\033[0m')
                print(f'\033[1;31m{moeda}: Preço atual ({ultimo_preco}) ultrapassou o limite máximo ({min}).\033[0m')
                hora = datetime.now()

                #webbrowser.open('https://web.whatsapp.com/')
                time.sleep(10)

                workbook = openpyxl.load_workbook('contatos-notificados.xlsx')
                pagina_contatos = workbook['Plan1']

                for linha in pagina_contatos.iter_rows(min_row=5):
                    #nome, telefone
                    nome = linha[2].value    
                    telefone = linha[3].value

                    #mensagem que será enviada aos contatos
                    msg = f'Olá {nome}, hora de comprar {moeda}, {hora.strftime('%d/%m/%Y, %H:%M')}'

                    #link que abrirá o zap
                    link_mensagem_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'

                    webbrowser.open(link_mensagem_zap)

                    time.sleep(20)
                    pyautogui.press('enter')
                    time.sleep(5)

                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(5)

                    pyautogui.hotkey('ctrl', 'w')
                    time.sleep(5)

                    print('FINALIZADO')
                    
            else:
                time.sleep(300)
            threading.Thread(target=manter_sistema).start()
            
            print('SISTEMA INICIADO COM SUCESSO!')
    threading.Thread(target=tarefa).start()

def fechar_sistema():
    global sistema_iniciado
    sistema_iniciado = False
    print('SISTEMA FECHADO COM SUCESSO')
    janela.destroy()

def manter_sistema():
    def tarefa():
        if sistema_iniciado: 
            print('SISTEMA ESTÁ SENDO MANTIDO COM SUCESSO!')
            janela.after(300000, manter_sistema)#Chama de novo após 300 segundos
            iniciar_sistema()
        else:
            print('SISTEMA DESLIGADO COM SUCESSO arruma isso Kaich')
    threading.Thread(target=tarefa).start()

#JANELA ABERTA
janela = Tk()#janela aberta
janela.title('Alertas compra e venda de criptos  v2.0')
janela.iconbitmap('icone-sistema.ico')
janela.configure(bg='#f7f7f7')#cor de fundo da janela

info = Label(janela,
    text='Favor abrir Whatsapp Web antes de iniciar o programa',
    fg='red',font=("Times New Roman", 12, "underline")
    ).pack(pady = 5)

hora = datetime.now()

infohora = Label(janela, text=f'{hora.strftime('%H:%M:%S')}',
    font=("Helvetica", 12,
    "underline"))
infohora.pack(pady=1)

infopreco = Label(janela, text="Clique no botão para atualizar os preços", font=("Helvetica", 12), justify="left")
infopreco.pack(pady=5)

atualiza_preco = Button(janela,
    text='Atualizar e salvar preços',
    bg='#a1a1a1',
    font=('Times', 10), command=atualizar_preco)
atualiza_preco.pack(pady=5)  
#se clicar no botão posso fazer ativar uma função que é exatamente a busca de preço atual de crypto igaul o que ja tem

#3 definir valor baixo para comprar e valor alto pra vender
comando =Label(janela,
    text='Digite os valores pedidos abaixo no formato (105000.00, 3850.43)',
    font=("Cambria", 11))
comando.pack(pady = 5)

#label e entry btc
Label(janela, text="BTC - Compra:",
    font=("Cambria", 11)).pack()
entry_btc_compra_min = Entry(janela)
entry_btc_compra_min.pack()

#label e entry btc
Label(janela, text="BTC - Venda :",
    font=("Cambria", 11)).pack()
entry_btc_venda_max = Entry(janela)
entry_btc_venda_max.pack()

#label e entry eth
Label(janela, text="ETH - Compra:",
    font=("Cambria", 11)).pack()
entry_eth_compra_min = Entry(janela)
entry_eth_compra_min.pack()

#label e entry eth
Label(janela, text="ETH - Venda :",
    font=("Cambria", 11)).pack()
entry_eth_venda_max = Entry(janela)
entry_eth_venda_max.pack()

#botão de confirmação
iniciar = Button(janela,
    text='OK',bg='#a1a1a1',
    command = iniciar_sistema).pack(pady = 5)

# Instrução
info3 =Label(janela,
    text='Clique em OK pra continuar o sistema',
    font=("Cambria", 11)).pack(pady = 5)

info4= Label(janela,
    text='Caso queira parar o programa clique no botão abaixo',
    font=("Cambria", 11)).pack(pady = 5)

parar = Button(janela,
    text='Parar',
    bg='#a1a1a1',
    command = fechar_sistema).pack(pady = 5)

janela.protocol("WM_DELETE_WINDOW", fechar_sistema)

# Executar a interface gráfica em paralelo ao loop principal contido em manter sistema
janela.after(100, manter_sistema)  # Executa o loop principal depois de 100ms = 10s
janela.mainloop()
