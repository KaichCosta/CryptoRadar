from datetime import datetime
import time
import yfinance as yf
symbols = ['btc-usd', 'eth-usd']
tickers = yf.Tickers(','.join(symbols))
limite_max = [105000, 3850]
limite_min = [103700, 3830]
ultimo_preco = [
    round(float(tickers.tickers[symbol.upper()].history(period='1d')['Close'].iloc[0]), 2)#round, float e esse ,2 são pra formatar com 2 casas decimais os valores das criptos
    for symbol in symbols
]
print(f'\033[1;32m{datetime.now()}\033[0m')
print(ultimo_preco)
print('\033[1;32m--BITCOIN--ETHEREUM\033[0m')

time.sleep (5)

    #4 criar sistema de envio de notificação pro zap CRIAR UM GRUPO E POR MEU PAI E EU PRA RECEBER ESSAS NOTIFICAÇÕES  

    #tem que ver se aparece separado pra btc e eth
for i, preco in enumerate(ultimo_preco):
    simbolo = symbols[i].upper()
    max = limite_max[i]
    min = limite_min[i]

    if preco > max:
        print(f'\033[1;31m=== ALERTA DE VENDA===\033[0m')
        print(f'\033[1;31m{simbolo}: Preço atual ({preco}) ultrapassou o limite máximo ({max}).\033[0m')
    
    elif preco < min:
        print(f'\033[1;31m=== ALERTA DE COMPRA===\033[0m')
        print(f'\033[1;31m{simbolo}: Preço atual ({preco}) ultrapassou o limite máximo ({min}).\033[0m')
    
    else:
        print(f'\033[1;32m{simbolo} está dentro do limite esperado.\033[0m')

time.sleep(5)