
#   PASSOS
#4 criar sistema de envio de notificação pro windows               
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

for symbol in symbols:
    print(tickers.tickers[symbol.upper()].history(period = '1d')['Close'][0])

#3 definir valor baixo para comprar e valor alto pra vender    
limite_max = [584079, 22366]
limite_min = [568926, 21511]

while True:
    ultimo_preco = [tickers.tickers[symbol.upper()].history(period = '1d')['Close'][0] for symbol in symbols]
    print(datetime.now())
    print(ultimo_preco)
    time.sleep (2)
    if ultimo_preco >= limite_max:
        break
    #tem que ver se aparece separado pra btc e eth
    if ultimo_preco >= limite_max:
        pywhatkit.sendwhatmsg('+5537998460473', 'Hora de comprar', datetime.now())



