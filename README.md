# LoraNetworkConf
Configuración de la red lora para gateway y sensores

## Diseño de la red

Deberán tenerse en cuenta diferentes variables para el diseño de la red LoRa, teniendo en cuenta que para incrementar la distancia de comunicación se usa un ancho de banda muy pequeño en lugar de incrementar la potencia. Teoricamente LoRa tiene un Link Budget de 154 dB, lo cual hace referencia a una distancia de 1300Km en condiciones perfectas, pero diferentes pérdidas durante el camino como óstaculos, reflexiones, etc. hacen que se disminuya significativamente esta distancia. 

![alt Network](https://github.com/diegoavellanedat17/LoraNetworkConf/blob/master/LoraNetwork.PNG)


## Dispositivos como Nodos
Los siguientes son dispositivos para usar como Nodos LoRa: 
- RFM95
- SX1276
- LoPy

## LoRa Gateway | MultiTech Conduit 
Info del Gateway LoRa configurable [ MultiTech Conduit ](https://www.multitech.com/brands/multiconnect-conduit)

## Pruebas LoPy Pysense
las sigueintes corresponden a las pruebas del LoPy y Pysense, tanto las conexiones del hardware como el desarrollo del Firmware para obtener los datos de cada uno de los sensores.

Las siguientes corresponden a las características de la parjeta Pysense:
- Sensor de luz ambiental
- Sensor de presión barométrica
- Sensor de humedad
- Acelerómetro de 3 ejes y 12 bits
- Sensor de temperatura
- Puerto USB con acceso en serie
- Cargador de batería LiPo
- Compatibilidad con tarjeta microSD
- Operación de ultra baja potencia (~ 1uA en DeepSleep)

Los siguientes son los pines de la tarjeta Pysense :

![alt Pysense](https://github.com/diegoavellanedat17/LoraNetworkConf/blob/master/Pysense.PNG)

