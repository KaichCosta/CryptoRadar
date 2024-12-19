import time
from datetime import datetime
import os
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from tkinter import *
import threading
import requests

#2 buscar preços bitcoin e ações atuais
def atualizar_preco():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    print(texto)

pegar_cotacoes()

# Variáveis globais
limite_max = []
limite_min = []
sistema_iniciado = False


#for symbol in symbols:
#print(tickers.tickers[symbol.upper()].history(period = '1d')['Close'][0])

#3 definir valor baixo para comprar e valor alto pra vender
# dar opcão do cliente escolher os valores max, min das criptos ex: limite =int(input'escolha valor min e max de eth e btc')    
limite_max = [105000, 3850]
limite_min = [103700, 3830]

while True:
    ultimo_preco = [
        round(float(tickers.tickers[symbol.upper()].history(period='1d')['Close'].iloc[0]), 2)#round, float e esse ,2 são pra formatar com 2 casas decimais os valores das criptos
        for symbol in symbols
    ]
    print(f'\033[1;32m{datetime.now()}\033[0m')
    print(ultimo_preco)
    print('\033[1;32m--BITCOIN--ETHEREUM\033[0m')
    time.sleep (5)


    janela = Tk()#janela aberta

    janela.title('Alertas compra e venda de criptos')

    janela.iconbitmap('icone-sistema.ico')

    info = Label(janela, text='Favor abrir Whatsapp Web antes de iniciar o programa',fg='red',font=("Helvetica", 12, "underline")).pack(pady = 5)

    infohora = Label(janela, text=f'{datetime.now()}',
        font=("Helvetica", 12,
        "underline")).pack(pady = 5)
        
    infopreco = Label(janela, text= ultimo_preco,
        font=("Times", 12,
        "underline")).pack(pady = 5)
    atualiza_preco = Button(janela,
                            text='',
                            font=('Times', 10), command=atualizar_preco).pack(pady=5)  
    #se clicar no botão posso fazer ativar uma função que é exatamente a busca de preço atual de crypto igaul o que ja tem
    Button(janela, text='Parar',bg='#a1a1a1' ).pack(pady = 5)

    janela.mainloop()

    if sistema_iniciado:
        print(f"Valores salvos:\nLimite Máximo: {limite_max}\nLimite Mínimo: {limite_min}")
        print('Sistema iniciado com sucesso!')
    else:
        print('Sistema não foi iniciado devido a erros nos valores.')
        break
