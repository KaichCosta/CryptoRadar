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
if ultimo_preco > limite_max:#ALERTA DE VENDA
    print('========ALERTA DE VENDA========')
    if symbols(0) > limite_max(0):
        print('==BITCOIN==')
    if symbols(1) > limite_max(1):
        print('==ETHEREUM==')

if ultimo_preco < limite_min:#ALERTA DE COMPRA
    print('========ALERTA DE COMPRA========')
    if symbols(0) > limite_min(0):
        print('==BITCOIN==')
    if symbols(1) > limite_min(1):
        print('==ETHEREUM==')

