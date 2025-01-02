from tkinter import *
from tkinter import messagebox
from datetime import datetime
import threading
import requests
# Dicionário para armazenar os limites
limites = {
    "BTC": {"compra_min": 0, "venda_max": 0},
    "ETH": {"compra_min": 0, "venda_max": 0}
}

def atualizar_preco():
    def tarefa():
        global precos, infohora
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/BTC-USD,ETH-USD")
        requisicao_dic = requisicao.json()
        precos["BTC"]["compra"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        precos["BTC"]["venda"] = round(float(requisicao_dic['BTCUSD']['bid']),2)
        precos["ETH"]["compra"] = round(float(requisicao_dic['ETHUSD']['bid']),2)
        precos["ETH"]["venda"] = round(float(requisicao_dic['ETHUSD']['bid']),2)
        
        texto = f'''
        BTC {precos["BTC"]["compra"]}
        ETH {precos["ETH"]["compra"]}
        '''
        print(texto)
        infopreco.config(text=texto)
        hora = datetime.now()
        infohora.config(text=f'{hora.strftime("%H:%M:%S")}')
    threading.Thread(target=tarefa).start()
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
janela.geometry("450x510")
janela.config(bg='#161616')#cor de fundo da janela
janela.title('Alertas compra e venda de criptos  v2.0')
janela.iconbitmap('icone-sistema.ico')
#img_fundo = Image.open("background_cryptoradar.png")
#bg_img = ImageTk.PhotoImage(img_fundo)

#fundo = Label(janela, image=bg_img)
#fundo.place(x=0, y=0, relwidth=1, relheight=1)  # Expande para cobrir toda a janela

# Usando pack na janela principal
top_frame = Frame(janela, bg='#161616')
top_frame.pack()

info = Label(top_frame,
    text='Favor abrir Whatsapp Web antes de iniciar o programa',
    fg='#d7ad01',
    bg='#161616',
    font=("Bebas Neue", 12)
    ).pack(pady=5)

hora = datetime.now()

infohora = Label(top_frame,
    text=f'{hora.strftime('%H:%M:%S')}',
    fg='white',
    bg='#161616',
    font=("Helvetica", 12,
    "underline"))
infohora.pack(pady=5)

infopreco = Label(top_frame,
    text="Clique no botão para atualizar os preços",
    fg='white',
    bg='#161616',
    font=("Helvetica", 12))
infopreco.pack(pady=5)

atualiza_preco = Button(janela,
    text='Visualizar cotações atuais',
    fg='white',
    bg='#161616',
    highlightbackground='#d7ad01',
    font=('Times', 10),
    command=atualizar_preco)
atualiza_preco.pack(pady=5)
#se clicar no botão posso fazer ativar uma função que é exatamente a busca de preço atual de crypto igaul o que ja tem

#3 definir valor baixo para comprar e valor alto pra vender
comando =Label(janela,
    text='Digite os valores pedidos abaixo no formato (105000.00, 3850.43)',
    fg='white',
    bg='#161616',
    font=("Cambria", 11))
comando.pack(pady=5)

# Usando grid dentro do frame
grid_frame = Frame(janela, bg='#161616')
grid_frame.pack()

#label e entry btc
Label(grid_frame, text="BTC - Compra:",
    fg='white',
    bg='#161616',  
    font=("Cambria", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_btc_compra_min = Entry(grid_frame,
    bg='white',)
entry_btc_compra_min.grid(row=0, column=1, padx=5, pady=5)

#label e entry btc
Label(grid_frame, text="BTC - Venda :",
    fg='white',
    bg='#161616', 
    font=("Cambria", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_btc_venda_max = Entry(grid_frame)
entry_btc_venda_max.grid(row=1, column=1, padx=5, pady=5)

#label e entry eth
Label(grid_frame, text="ETH - Compra:",
    fg='white',
    bg='#161616', 
    font=("Cambria", 11)).grid(row=2, column=0, padx=5, pady=5)
entry_eth_compra_min = Entry(grid_frame)
entry_eth_compra_min.grid(row=2, column=1, padx=5, pady=5)

#label e entry eth
Label(grid_frame, text="ETH - Venda :",
    fg='white',
    bg='#161616', 
    font=("Cambria", 11)).grid(row=3, column=0, padx=5, pady=5)
entry_eth_venda_max = Entry(grid_frame)
entry_eth_venda_max.grid(row=3, column=1, padx=5, pady=5)

bottom_frame = Frame(janela, bg='#161616')
bottom_frame.pack()
# Instrução
info3 =Label(bottom_frame,
    text='Clique em OK pra continuar o sistema',
    fg='white',
    bg='#161616', 
    font=("Cambria", 11)).pack(pady = 5)

#botão de confirmação
iniciar = Button(bottom_frame,
    text='OK',
    fg='white',
    bg='#161616',
    command = iniciar_sistema).pack(pady = 5)

info4= Label(bottom_frame,
    text='Caso queira parar o programa clique no botão abaixo',
    fg='white',
    bg='#161616', 
    font=("Cambria", 11)).pack(pady = 5)

parar = Button(bottom_frame,
    text='Parar',
    fg='white',
    bg='#161616',
    command = fechar_sistema).pack(pady = 5)

janela.protocol("WM_DELETE_WINDOW", fechar_sistema)

# Executar a interface gráfica em paralelo ao loop principal contido em manter sistema
janela.after(100, manter_sistema)  # Executa o loop principal depois de 100ms = 10s
janela.mainloop() 





