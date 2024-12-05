
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
import pywhatkit
#from winotify import Notification, audio

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

    #tem que ver se aparece separado pra btc e eth( TO TENTANDO ARRUMAR KKKK, E TEM QUE QUANDO MANDAR MENSAGEM APARECER QUAL CRIPTO TEM QUE COMPRAR E VENDER)
    if ultimo_preco > limite_max:#ALERTA DE VENDA
        print('========ALERTA DE VENDA========')

        agora = datetime.now()
        hora = agora.hour
        minutos = agora.minute + 1  # Adiciona 1 minuto para evitar atraso
        pywhatkit.sendwhatmsg('+5537998460473', 'Hora de vender', hora, minutos)
        break

    if ultimo_preco < limite_min:#ALERTA DE COMPRA
        print('========ALERTA DE COMPRA========')
        agora = datetime.now()
        hora = agora.hour
        minutos = agora.minute + 1  # Adiciona 1 minuto para evitar atraso
        pywhatkit.sendwhatmsg('+5537998460473', 'Hora de comprar', hora, minutos, 5)
        break



