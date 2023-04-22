import time
import random
import statistics
from paho.mqtt.client import Client
import sys
from time import sleep

values = [] #Lista para almacenar los valores de humedad

# Función para saber si es primo un número entero positivo
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para hallar la media
def media(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

def on_connect(client, rc):
    print("Conectado con código de resultado: " + str(rc))
    client.subscribe("numbers") #Primero nos conectamos al topic 'numbers'
    
# Función que se ejecutará cuando se reciba un mensaje del topic "numbers"
def on_message_numbers(client, userdata, message):
    number = int(message.payload.decode())
    print(f"Número recibido: {number}")
    if primo(number): #Si es primo nos suscribimos al canal humedad durante 5 segundos
        print("Número primo, leyendo humedad durante 7 segundos...")
        values.clear()
        client.subscribe("humidity")
        time.sleep(7) # Esperamos 7 segundos
        client.unsubscribe("humidity")

# Función que se ejecutará cuando se reciba un mensaje del topic "humidity"
def on_message_humidity(client, userdata, message):
    humidity = float(message.payload.decode())
    print(f"Received humidity: {humidity}")
    values.append(humidity) #Añadimos el valor a la lista values de humedades
    mean = 0
    if len(values) >= 5: #Si ya hemos leído 5 valores hallamos la media y vaciamos values
        mean = calculate_mean(values)
        print(f"Media humedad últimos 5 valores: {mean}")
        values.clear()
    if mean > 20: #Si superamos la humedad umbral se publica en temporizador para que se publique en 5 segundos el mensaje superada en el topic humedad_umbral
        print('Humdedad umbral superada, poniendo temporizador...')
        client.publish('temporizador', 'humedad_umbral;5;superada')
        



def main(hostname):
    
    client = Client()
    client.on_connect = on_connect
    client.on_message = on_message_numbers
    client.message_callback_add("humidity", on_message_humidity)
    client.username_pw_set('cadena_client', password=None)
    client.connect(hostname)
    client.loop_start()
    
    while True:
        sleep(1)

if __name__ == '__main__':
    hostname = 'simba.fdi.ucm.es'
    if len(sys.argv)>1:
        hostname = sys.argv[1]
    main(hostname)


