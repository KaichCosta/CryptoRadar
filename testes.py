from datetime import datetime
import pywhatkit
agora = datetime.now()
hora = agora.hour
minutos = agora.minute + 1  # Adiciona 1 minuto para evitar atraso
pywhatkit.sendwhatmsg('+5537998460473', 'Hora de comprar', hora, minutos)