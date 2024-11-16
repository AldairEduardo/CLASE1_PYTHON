import pandas as pd
import pywhatkit as kit
import datetime
import time
import schedule

def enviar_mensajes():
    # Cargar el archivo Excel
    archivo_excel = "Clientes.xlsx"  # Cambia esto al nombre de tu archivo
    df = pd.read_excel(archivo_excel)

    # Obtener la fecha actual
    hoy = datetime.datetime.now()
    mes_actual = hoy.strftime("%Y-%m")

    # Filtrar los mensajes que corresponden al mes actual
    df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')  # Asegúrate de que las fechas estén bien formateadas
    df_mes_actual = df[df['Fecha'].dt.strftime("%Y-%m") == mes_actual]

    # Enviar mensajes a cada cliente
    for index, row in df_mes_actual.iterrows():
        numero = row['Número']  # Columna con los números de teléfono
        link = row['Link WhatsApp']  # Columna con los enlaces o mensajes personalizados
        
        # Extraer solo el número del link o usar directamente el número
        if not link.startswith("https://api.whatsapp.com"):
            mensaje = link
        else:
            mensaje = "⚠️Recuerda realizar tu pago de CHAT GPT PLUS⚠️"  # Mensaje por defecto

        # Configuración de tiempo para enviar los mensajes
        hora_envio = hoy.hour  # Enviar a la hora actual
        minuto_envio = (hoy.minute + 1) % 60  # Enviar al siguiente minuto
        
        print(f"Enviando mensaje a {numero}...")
        try:
            # Enviar el mensaje
            kit.sendwhatmsg(numero, mensaje, hora_envio, minuto_envio)
            time.sleep(5)  # Esperar para evitar bloqueos
        except Exception as e:
            print(f"Error al enviar el mensaje a {numero}: {e}")

# Programar la tarea para que se ejecute automáticamente cada mes
schedule.every().month.do(enviar_mensajes)

print("Esperando para enviar mensajes...")
while True:
    schedule.run_pending()
    time.sleep(1)
