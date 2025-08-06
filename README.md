# 📡 CryptoRadar

> Um sistema de monitoramento de preços de criptomoedas com notificações automatizadas em tempo real via WhatsApp. Nunca mais perca uma oportunidade de mercado!

![Python](https://img.shields.io/badge/python-3.10_3.11_3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![Requests](https://img.shields.io/badge/requests-API-red?style=for-the-badge)

## 🚀 Sobre o Projeto

O CryptoRadar foi criado para resolver um problema comum para entusiastas de criptomoedas: a necessidade de verificar constantemente os preços para não perder o momento certo de comprar ou vender.

Este script automatiza todo o processo. Ele utiliza uma API para buscar os valores das criptomoedas em tempo real e, através de uma interface gráfica simples, permite que o usuário defina "alarmes" de preço. Quando o valor de uma moeda atinge o alvo definido, uma notificação é enviada automaticamente para o seu WhatsApp.

## ✨ Funcionalidades

* **Monitoramento em Tempo Real:** Busca de preços de Bitcoin e Ethereum.
* **Alertas Personalizados:** Defina qual cripto e qual preço (acima ou abaixo) você quer monitorar.
* **Notificações no WhatsApp:** Automação que abre o WhatsApp Web e envia uma mensagem para a lista de contatos da planilha excel .
* **Interface Gráfica Simples:** Feito com Tkinter para facilitar a configuração dos alertas.
* **Processamento em Background:** Graças ao `threading`, a interface não trava enquanto o monitoramento acontece.

## 🛠️ Tecnologias e Bibliotecas

Este projeto foi construído utilizando:

* **Python**
* **API:** Awesome API
* **Interface Gráfica:**
    * `tkinter`: Para criar a janela e os componentes visuais.
* **Automação e Web:**
    * `requests`: Para fazer as chamadas à API de criptomoedas.
    * `webbrowser`: Para abrir o WhatsApp Web no navegador.
    * `pyautogui`: Para controlar o mouse e teclado e enviar a mensagem.
* **Manipulação de Dados e Arquivos:**
    * `openpyxl`: Para ler ou escrever dados em planilhas Excel.
    * `urllib`, `os`, `sys`, `time`, `datetime`: Bibliotecas padrão para diversas funcionalidades.
* **Execução Paralela:**
    * `threading`: Para garantir que o monitoramento rode sem congelar a interface do usuário.

## ✅ Como Começar (Fácil e Rápido)

Este programa foi compilado em um executável para Windows, então você não precisa instalar Python nem nenhuma biblioteca para usá-lo. Basta seguir os passos:

1.  **Baixe o Programa**
    * Acesse a pasta `CryptoRadar.App` neste repositório.
    * Clique no botão verde **"< > Code"** e depois em **"Download ZIP"**.

2.  **Descompacte os Arquivos**
    * Encontre o arquivo `CryptoRadar.zip` que você baixou.
    * Clique com o botão direito sobre ele e escolha **"Extrair tudo..."**. Salve em uma pasta de sua preferência.

3.  **Execute o Radar**
    * Abra a pasta que você acabou de extrair.
    * Encontre e dê um duplo clique no arquivo **`index.exe`** para iniciar o programa.

4.  **Pré-requisito Importante**
    * Para que as notificações funcionem, **certifique-se de que você já está com o login feito no WhatsApp Web** no seu navegador de internet padrão (Google Chrome, Firefox, etc.).

## 🎮 Como Usar

1.  Ao executar o programa, a janela principal será aberta.
2.  Preencha os campos para a criptomoeda que deseja monitorar e o preço de alerta. (Todos os 4 campos devem estar preenchidos, **`exemplo`**, se não quiser receber alerta do ETH coloque o preço de compra extremamente alto exemplo: 999999 e venda, coloque um valor baixo, exemplo: 5
3.  Clique no botão "OK".
4.  O sistema começará a verificar o preço em segundo plano. Deixe o programa rodando.
5.  Quando o preço for atingido, o navegador abrirá com o WhatsApp e enviará a mensagem de alerta.
