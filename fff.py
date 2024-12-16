from tkinter import *

# Variáveis globais
limite_max = []
limite_min = []

def salvar_valores():
    global limite_max, limite_min
    msg_erro.config(text='')  # Limpa qualquer mensagem de erro anterior

    valores_max = entrada_max.get()
    valores_min = entrada_min.get()

    if ',' in valores_max and ',' in valores_min:
        try:
            valores_max = [float(valor.strip()) for valor in valores_max.split(',')]
            valores_min = [float(valor.strip()) for valor in valores_min.split(',')]
            if len(valores_max) == 2 and len(valores_min) == 2:
                limite_max = valores_max
                limite_min = valores_min
                print(f"Limite Máximo: {limite_max}")
                print(f"Limite Mínimo: {limite_min}")
                msg_erro.config(text='Valores válidos!', fg='green')
                return True  # Nenhum erro
            else:
                msg_erro.config(text='Forneça exatamente dois valores (BTC, ETH)', fg='red')
                return False
        except ValueError:
            msg_erro.config(text='Digite os valores no formato correto (ex: 105000.00, 3850.00)', fg='red')
            return False
    else:
        msg_erro.config(text='Separe os valores por vírgula.', fg='red')
        return False

def iniciar_sistema():
    if salvar_valores():
        global sistema_iniciado
        sistema_iniciado = True
        janela.iconify()  # Minimiza a janela

def fechar_sistema():
    global sistema_iniciado
    janela.destroy()
    print('SISTEMA FECHADO COM SUCESSO')

# JANELA
janela = Tk()
janela.configure(bg='#f7f7f7')
janela.title('Preços máximos e mínimos venda e compra de criptos')

# Mensagens e entradas
info = Label(janela, text='Abra o WhatsApp Web antes de iniciar o programa', fg='red', font=("Helvetica", 12, "underline"))
info.pack(pady=5)

comando = Label(janela, text='Digite os valores no formato (105000.00, 3850.00)', font=("Helvetica", 10))
comando.pack(pady=5)

info1 = Label(janela, text='Preço para venda de (BTC, ETH):', font=("Helvetica", 10))
info1.pack(pady=1)

entrada_max = Entry(janela)
entrada_max.pack(pady=3)

info2 = Label(janela, text='Preço para compra de (BTC, ETH):', font=("Helvetica", 10))
info2.pack(pady=1)

entrada_min = Entry(janela)
entrada_min.pack(pady=3)

msg_erro = Label(janela, text='', fg='red')
msg_erro.pack(pady=1)

# Botões
Button(janela, text='OK', bg='#a1a1a1', command=iniciar_sistema).pack(pady=5)
Button(janela, text='Parar', bg='#a1a1a1', command=fechar_sistema).pack(pady=5)

# Mensagem final
info3 = Label(janela, text='Clique em OK para iniciar ou em Parar para fechar.', font=("Helvetica", 10))
info3.pack(pady=10)

janela.mainloop()

if 'sistema_iniciado' in globals() and sistema_iniciado:
    print('Sistema iniciado com sucesso.')


