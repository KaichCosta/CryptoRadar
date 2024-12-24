import tkinter as tk
import requests
from datetime import datetime

# Função para buscar os preços e atualizar o Label
def atualizar_preco():
    global infopreco, u  # Declaração de variável global

    requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD")
    requisicao_dic = requisicao.json()

    preco_btc = round(float(requisicao_dic['BTCUSD']['bid']), 2)
    preco_eth = round(float(requisicao_dic['ETHUSD']['bid']), 2)
    u =datetime.now()
    texto = f'''
    BTC: {preco_btc}
    ETH: {preco_eth}
    {u.strftime("%H:%M:%S")}
    '''
    print(texto)

    # Atualiza o texto no Label
    infopreco.config(text=texto)

# Criação da interface Tkinter
janela = tk.Tk()
janela.title("Preço das Criptomoedas")
janela.geometry("300x200")

# Label inicial para exibir as informações dos preços
infopreco = tk.Label(janela, text="Clique no botão para atualizar os preços", font=("Helvetica", 12), justify="left")
infopreco.pack(pady=20)

# Botão para atualizar os preços manualmente
botao_atualizar = tk.Button(janela, text="Atualizar Preços", command=atualizar_preco)
botao_atualizar.pack(pady=10)

# Inicializando o loop da interface
janela.mainloop()
