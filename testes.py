from datetime import datetime
import time

from urllib.parse import quote
import webbrowser

from tkinter import *

# Variáveis globais
limite_max = []
limite_min = []
sistema_iniciado = False
#AGORA É FAZER UM TRATAMENTO DE ERRO DECENTE to fazendo kkk
def salvar_valores():
    # Lê os valores inseridos pelo usuário
    global limite_max, limite_min
# Limpa qualquer mensagem de erro anterior
    msg_erro.config(text='')

    valores_max = entrada_max.get()
    valores_min = entrada_min.get()
    #validação, deu um erro que fechou a janela antes de aparecer o erro escrito na interface
    # Converte os valores para float e os armazena nas variáveis
    if ',' in valores_max and ',' in valores_min:
        try:
            valores_max = [float(valor.strip ()) for valor in valores_max.split(',')]
            valores_min = [float(valor.strip()) for valor in valores_min.split(',')]
            if len(valores_max) == 2 and len(valores_min) == 2:
                limite_max = valores_max
                limite_min = valores_min
                print(f"Limite Máximo: {limite_max}")
                print(f"Limite Mínimo: {limite_min}")
                msg_erro.config(text='Valores válidos!', fg='green')
                return True  # Nenhum erro
            else:
                msg_erro.config(text='Certifique-se de fornecer exatamente dois valores, primeiro para BTC e o segundo para ETH',fg='red')
                print("Erro: Certifique-se de fornecer exatamente dois valores para cada limite.")
                return False  # Nenhum erro
        except ValueError:
            msg_erro.config(text='Digite os Preços no formato pedido',fg='red')
            print("Erro: Certifique-se de digitar os valores no formato correto (ex: 105000.00, 3850.00)")
            return False
    else:
        msg_erro.config(text='Erro: Certifique-se de separar os valores por vírgula.', fg='red') 
        return False      

def iniciar_sistema():
    if salvar_valores():
        global sistema_iniciado  # Define uma flag global para controle
        sistema_iniciado = True  # Altera o estado da flag
        janela.quit()         # Fecha a janela e permite o restante do código ser executado

def fechar_sistema():
    global sistema_iniciado
    time.sleep(2)
    janela.destroy


#JANELA ABERTA
janela = Tk()
janela.title('Preços máximos e mínimos venda e compra de criptos')

info = Label(janela, text='Favor abrir Whatsapp Web antes de iniciar o programa',)
info.pack(pady = 5)

comando =Label(janela, text='Digite os valores pedidos abaixo no formato (105000.00, 3850.00)')
comando.pack(pady = 5)

info1 = Label(janela, text='Digite o Preço que deseja ser notificado para venda de (BTC, ETH):')
info1.pack(pady = 1)

entrada_max = Entry(janela)#caixa de digitação
entrada_max.pack()
# Área para exibir mensagens de erro
msg_erro = Label(janela, text='', fg='red')
msg_erro.pack(pady=1)

info2 = Label(janela, text='Digite o Preço que deseja ser notificado para compra de (BTC, ETH):')
info2.pack(pady = 1)

entrada_min = Entry(janela)#caixa de digitação
entrada_min.pack()
msg_erro = Label(janela, text='', fg='red')
msg_erro.pack(pady=1)

#botão de confirmação
Button(janela, text='OK',command = iniciar_sistema).pack(pady = 5)

# Instrução
info3 =Label(janela, text='Clique em OK pra continuar o sistema')
info3.pack(pady = 5)

info4= Label(janela, text='Caso queira parar o programa clique no botão abaixo')
info4.pack(pady = 5)
Button(janela, text='Parar', command = fechar_sistema).pack(pady = 5)

janela.mainloop()

if sistema_iniciado:
    print(f"Valores salvos:\nLimite Máximo: {limite_max}\nLimite Mínimo: {limite_min}")
    print('Sistema iniciado com sucesso!')
else:
    print('Sistema não foi iniciado devido a erros nos valores.')

