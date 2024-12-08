
#   PASSOS
            
#5 criar um executavel pra isso tudo                               
#6 criar sistema pra enviar pro celular
#    o1 qualquer coisa criar outro arquivo pra criar um apk pro celular do meu pai e executar tudo pelo celular do meu pai e fazer ele receber as notificaçoes
#    o2 no apk, ter opção de parar a procura de preço  
#7 enviar notificação pelo email é melhor ou por zap

#1 importar bibliotecas  
import time
from datetime import datetime
import os
import yfinance as yf
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui


#2 buscar preços bitcoin e ações atuais
symbols = ['btc-usd', 'eth-usd']
tickers = yf.Tickers(','.join(symbols))

#for symbol in symbols:
#    print(tickers.tickers[symbol.upper()].history(period = '1d')['Close'][0])

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

    #4 criar sistema de envio de notificação pro zap CRIAR UM GRUPO E POR MEU PAI E EU PRA RECEBER ESSAS NOTIFICAÇÕES  
    for i, preco in enumerate(ultimo_preco):
        simbolo = symbols[i].upper()

        max = limite_max[i]

        min = limite_min[i]

    if preco > max:
        print(f'\033[1;31m=== ALERTA DE VENDA===\033[0m')
        print(f'\033[1;31m{simbolo}: Preço atual ({preco}) ultrapassou o limite máximo ({max}).\033[0m')
        #EU IRIA POR TODA ESSA PARTE DE ANÁLISE DE NOME E TELEFONE FORA DO (IF), MAS ISSO FARIA QUE SE REPETISSE TODA HORA POR CAUSA DO (WHILE) E NÃO SOMENTE NA COMPRA OU VENDA
        hora = datetime.now()

        webbrowser.open('https://web.whatsapp.com/')
        time.sleep(10)

        workbook = openpyxl.load_workbook('contatos-notificados.xlsx')
        pagina_contatos = workbook['Plan1']

        for linha in pagina_contatos.iter_rows(min_row=5):
            #nome, telefone
            nome = linha[2].value    
            telefone = linha[3].value

            #mensagem que será enviada aos contatos
            msg = f'Olá {nome}, hora de vender {simbolo}, {hora.strftime('%d/%m/%Y, %H:%M')}'

            #link que abrirá o zap
            link_mensagem_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'

            webbrowser.open(link_mensagem_zap)

            time.sleep(15)
            pyautogui.press('enter')
            time.sleep(5)

            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)

            pyautogui.hotkey('ctrl', 'w')
            time.sleep(5)

            print('FINALIZADO')
            break
    #==============================================
    #==============================================
    elif preco < min:
        print(f'\033[1;31m=== ALERTA DE COMPRA===\033[0m')
        print(f'\033[1;31m{simbolo}: Preço atual ({preco}) ultrapassou o limite máximo ({min}).\033[0m')
        hora = datetime.now()

        webbrowser.open('https://web.whatsapp.com/')
        time.sleep(10)

        workbook = openpyxl.load_workbook('contatos-notificados.xlsx')
        pagina_contatos = workbook['Plan1']

        for linha in pagina_contatos.iter_rows(min_row=5):
            #nome, telefone
            nome = linha[2].value    
            telefone = linha[3].value

            #mensagem que será enviada aos contatos
            msg = f'Olá {nome}, hora de comprar {simbolo}, {hora.strftime('%d/%m/%Y, %H:%M')}'

            #link que abrirá o zap
            link_mensagem_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'

            webbrowser.open(link_mensagem_zap)

            time.sleep(15)
            pyautogui.press('enter')
            time.sleep(5)

            pyautogui.hotkey('ctrl', 'w')
            time.sleep(2)

            pyautogui.hotkey('ctrl', 'w')
            time.sleep(5)

            print('FINALIZADO')
            break
    #E TEM QUE QUANDO MANDAR MENSAGEM APARECER QUAL CRIPTO TEM QUE COMPRAR E VENDER)
