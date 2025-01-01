from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Dicionário para armazenar os limites
limites = {
    "BTC": {"compra_min": 0, "venda_max": 0},
    "ETH": {"compra_min": 0, "venda_max": 0}
}

def atualizar_preco():
    print('atoa1')
def manter_sistema():
    print('atoa2')
def fechar_sistema():    
    print('atoa3')

def iniciar_sistema():
    print('atoa4')    
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
janela = Tk()#janela aberta
janela.geometry("500x600")
janela.title('Alertas compra e venda de criptos  v2.0')
janela.iconbitmap('icone-sistema.ico')
janela.configure(bg='#f7f7f7')#cor de fundo da janela
# Usando pack na janela principal
top_frame = Frame(janela)
top_frame.pack()

info = Label(top_frame,
    text='Favor abrir Whatsapp Web antes de iniciar o programa',
    fg='red',font=("Times New Roman", 12, "underline")
    ).pack(pady=5)

hora = datetime.now()

infohora = Label(top_frame,
    text=f'{hora.strftime('%H:%M:%S')}',
    font=("Helvetica", 12,
    "underline"))
infohora.pack(pady=5)

infopreco = Label(top_frame,
    text="Clique no botão para atualizar os preços",
    font=("Helvetica", 12),
    justify="left")
infopreco.pack(pady=5)

atualiza_preco = Button(janela,
    text='Visualizar cotações atuais',
    bg='#f7f7f7',
    font=('Times', 10),
    command=atualizar_preco)
atualiza_preco.pack(pady=5)
#se clicar no botão posso fazer ativar uma função que é exatamente a busca de preço atual de crypto igaul o que ja tem

#3 definir valor baixo para comprar e valor alto pra vender
comando =Label(janela,
    text='Digite os valores pedidos abaixo no formato (105000.00, 3850.43)',
    font=("Cambria", 11))
comando.pack(pady=5)

# Usando grid dentro do frame
grid_frame = Frame(janela)
grid_frame.pack()

#label e entry btc
Label(grid_frame, text="BTC - Compra:",
    font=("Cambria", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_btc_compra_min = Entry(grid_frame)
entry_btc_compra_min.grid(row=0, column=1, padx=5, pady=5)

#label e entry btc
Label(grid_frame, text="BTC - Venda :",
    font=("Cambria", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_btc_venda_max = Entry(grid_frame)
entry_btc_venda_max.grid(row=1, column=1, padx=5, pady=5)

#label e entry eth
Label(grid_frame, text="ETH - Compra:",
    font=("Cambria", 11)).grid(row=2, column=0, padx=5, pady=5)
entry_eth_compra_min = Entry(grid_frame)
entry_eth_compra_min.grid(row=2, column=1, padx=5, pady=5)

#label e entry eth
Label(grid_frame, text="ETH - Venda :",
    font=("Cambria", 11)).grid(row=3, column=0, padx=5, pady=5)
entry_eth_venda_max = Entry(grid_frame)
entry_eth_venda_max.grid(row=3, column=1, padx=5, pady=5)

bottom_frame = Frame(janela)
bottom_frame.pack()
# Instrução
info3 =Label(bottom_frame,
    text='Clique em OK pra continuar o sistema',
    font=("Cambria", 11)).pack(pady = 5)

#botão de confirmação
iniciar = Button(bottom_frame,
    text='OK',bg='#a1a1a1',
    command = iniciar_sistema).pack(pady = 5)

info4= Label(bottom_frame,
    text='Caso queira parar o programa clique no botão abaixo',
    font=("Cambria", 11)).pack(pady = 5)

parar = Button(bottom_frame,
    text='Parar',
    bg='#a1a1a1',
    command = fechar_sistema).pack(pady = 5)

janela.protocol("WM_DELETE_WINDOW", fechar_sistema)

# Executar a interface gráfica em paralelo ao loop principal contido em manter sistema
janela.after(100, manter_sistema)  # Executa o loop principal depois de 100ms = 10s
janela.mainloop()





