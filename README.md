# EJERCICIOS-MQTT

ej_2cliente_num.py consiste en un cliente mqtt que se conecta al topic 'numbers' y cada vez que lee un número lo almacena en un diccionario en función de si es un entero o un float. Si es entero calcula si es primo. También lleva una tabla de frecuencias de los números que han salido previamente.

ej_3_cliente_temperaturas.py consiste en un cliente mqtt que se conecta a los topics 'temperature/t1' y 'temperature/t2'. Cada vez que lee una temperatura la guarda en su lista correspondiente y cada 5 segundos se calcula la media, máximo y mínimo de las temperaturas recibidas de cada sensor y se vacían para el siguiente cálculo.

ej_4_cliente_humedad.py consiste en un cliente mqtt que lee un sensor de temperatura. Si la temperatura supera un umbral K0 entonces el cliente se suscribirá también al canal de humedad. Si la temperatura baja de K0 o el valor de humedad supera K1 el cliente se desuscribe del canal de humedad.

ej_5_cliente_temporizador.py consiste en un cliente mqtt que se suscribe al topic 'temporizador' y recibe la información de un mensaje a publicar, el tiempo de espera para ello y el topic donde publicarlo. Pasado el tiempo indicado publica el mensaje en dicho topic.

ej_6_cliente_cadena.py consiste en un cliente mqtt que se suscribe al topic 'numbers'. Si el número recibido es un número primo comienza a recibir información de humedad, si esta supera un determinado valor, se envía al topic temporizador que publique en el topic humdedad_umbral el mensaje superada con un tiempo de espera de 5 segundos para que el cliente del ejercicio 5 se encargue de hacerlo.
