import time
from datetime import datetime
import os
import yfinance as yf
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from tkinter import *
import requests

#2 buscar preços bitcoin e ações atuais

def atualizar_preco():
        
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD")

        requisicao_dic = requisicao.json()
        preco_btc = requisicao_dic['BTCUSD']['bid']
        preco_eth = requisicao_dic['ETHUSD']['bid']
        texto = f'''
        BTC: {preco_btc}
        ETH: {preco_eth}
        '''
        ultimo_preco = [("BTC", preco_btc), ("ETH", preco_eth)]
        print(f'\033[1;32m{datetime.now()}\033[0m')
        print(ultimo_preco)
        print('\033[1;32m--BITCOIN--ETHEREUM\033[0m')
        print(texto)
atualizar_preco()
def manter_sistema():
    while True:
        if sistema_iniciado: 
            print('SISTEMA ESTÁ SENDO MANTIDO COM SUCESSO!')
        else:
            print('SISTEMA DESLIGADO COM SUCESSO')
            break     
        time.sleep(10)