import tkinter as tk

# Variáveis globais para salvar os limites
limite_max = []
limite_min = []

def salvar_valores():
    global limite_max, limite_min

    # Limpa qualquer mensagem de erro anterior
    mensagem_erro.config(text="")

    valores_max = entrada_max.get()
    valores_min = entrada_min.get()

    # Validação do formato esperado
    if ',' in valores_max and ',' in valores_min:
        try:
            # Tenta converter os valores para float
            valores_max = [float(valor.strip()) for valor in valores_max.split(',')]
            valores_min = [float(valor.strip()) for valor in valores_min.split(',')]

            # Certifique-se de que há exatamente dois valores
            if len(valores_max) == 2 and len(valores_min) == 2:
                limite_max = valores_max
                limite_min = valores_min
                print(f"Limite Máximo: {limite_max}")
                print(f"Limite Mínimo: {limite_min}")
                mensagem_erro.config(text="Valores salvos com sucesso!", fg="green")
            else:
                mensagem_erro.config(text="Erro: Insira exatamente dois valores separados por vírgula.", fg="red")
        except ValueError:
            mensagem_erro.config(text="Erro: Os valores devem ser números válidos.", fg="red")
    else:
        mensagem_erro.config(text="Erro: Certifique-se de separar os valores por vírgula.", fg="red")

def fechar_janela():
    salvar_valores()
    janela.destroy()

# Configuração da interface
janela = tk.Tk()
janela.title('Preços máximos e mínimos venda e compra de criptos')

# Texto explicativo
tk.Label(janela, text='Digite os valores pedidos abaixo no formato (105000.00, 3850.00)').pack(pady=5)

# Entrada para o limite máximo
tk.Label(janela, text='Digite o Preço que deseja ser notificado para venda de (BTC, ETH):').pack(pady=1)
entrada_max = tk.Entry(janela)
entrada_max.pack()

# Entrada para o limite mínimo
tk.Label(janela, text='Digite o Preço que deseja ser notificado para compra de (BTC, ETH):').pack(pady=1)
entrada_min = tk.Entry(janela)
entrada_min.pack()

# Área para exibir mensagens de erro
mensagem_erro = tk.Label(janela, text="", fg="red")
mensagem_erro.pack(pady=5)

# Botão de confirmação
tk.Button(janela, text='OK', command=fechar_janela).pack(pady=5)

janela.mainloop()

# Após fechar a janela, os valores ficam disponíveis
print(f"Valores após fechar: Limite Máximo: {limite_max}, Limite Mínimo: {limite_min}")
