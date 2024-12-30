import tkinter as tk
from tkinter import messagebox

# Dicionário para armazenar os limites
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
    

# Criação da janela principal
janela = tk.Tk()
janela.title('Alertas compra e venda de criptos  v2.0')
janela.iconbitmap('icone-sistema.ico')
janela.configure(bg='#f7f7f7')#cor de fundo da janela

# Labels e Entrys para Bitcoin
tk.Label(janela, text="BTC - Compra:").pack()
entry_btc_compra_min = tk.Entry(janela)
entry_btc_compra_min.pack()

tk.Label(janela, text="BTC - Venda:",
    font=("Cambria", 11)).pack()
entry_btc_venda_max = tk.Entry(janela)
entry_btc_venda_max.pack()

# Labels e Entrys para Ethereum
tk.Label(janela, text="ETH - Compra:").pack()
entry_eth_compra_min = tk.Entry(janela)
entry_eth_compra_min.pack()

tk.Label(janela, text="ETH - Venda:").pack()
entry_eth_venda_max = tk.Entry(janela)
entry_eth_venda_max.pack()

# Botão para salvar os limites
btn_salvar = tk.Button(janela, text="Salvar Limites", command=salvar_valores)
btn_salvar.pack()

janela.mainloop()

