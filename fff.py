try:#testar esses códigos aqui
    entrada = input("Digite números separados por espaço: ")  # Exemplo: "1 2 três 4"
    numeros = list(map(int, entrada.split()))
    print(numeros)
except ValueError:
    print("Erro: Certifique-se de digitar apenas números separados por espaço!")

# Define o número máximo de valores
n = 3

while True:
    entrada = input(f"Digite exatamente {n} números separados por espaço: ")
    lista = entrada.split()
    if len(lista) == n:
        numeros = list(map(int, lista))
        break
    else:
        print(f"Erro: Digite exatamente {n} valores.")

print(numeros)  # Saída: [valores válidos]

