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
