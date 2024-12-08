from datetime import datetime
import time
import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
hora = datetime.now()

webbrowser.open('https://web.whatsapp.com/')
time.sleep(10)
workbook = openpyxl.load_workbook('contatos-notificados.xlsx')
pagina_contatos = workbook['Plan1']

for linha in pagina_contatos.iter_rows(min_row=5):
    #nome, telefone
    nome = linha[2].value    
    telefone = linha[3].value
    #mensagem que será enviada aos contatos
    msg = f'Olá {nome}, hora de vender {simbolo}, {hora.strftime('%d/%m/%Y, %H:%M')}'
    #link que abrirá o zap
    link_mensagem_zap = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'

    webbrowser.open(link_mensagem_zap)

    time.sleep(15)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.hotkey('ctrl', 'w')
    time.sleep(2)

    pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)

    print('FINALIZADO')
    break

