from tkinter import *

# Cria a janela principal
janela = Tk()
janela.title("Janela Personalizada")
janela.geometry("400x300")

# Define a cor de fundo da janela
janela.configure(bg="lightblue")

# Texto com cor e fonte personalizada
titulo = Label(janela, text="Bem-vindo!", fg="white", bg="blue", font=("Arial", 18, "bold"))
titulo.pack(pady=10)

# Botão com cor e fonte personalizada
botao = Button(janela, text="Clique Aqui", fg="black", bg="yellow", font=("Helvetica", 14, "italic"))
botao.pack(pady=10)

# Rodar a interface
janela.mainloop()
