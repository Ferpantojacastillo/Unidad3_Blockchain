Introducción a las redes VLAN
Redes VLAN : subred lógica que agrupa puertos de switch como si estuviera en la misma LAN independiente de su ubicación física.   
*Todas las redes vlan tienen un identificador
Tiene su propio dominio de broadcast

¿Por que usar una VLAN? para mayor seguridad, control de trafico, simplificación de gestión, optimización de recursos.
¿Cuáles son los beneficios?
broadcast: método de transmisión de datos que permite enviar un paquete desde un punto a todos los dispositivos o usuarios conectados en una misma red simultáneamente, sin la necesidad de conocer sus direcciones individuales.
ARP: protocolo esencial que permite traducir direcciones IP lógicas en direcciones MAC físicas para que los dispositivos puedan comunicarse correctamente en una red local.
VLAN de datos trafico de usuarios finales
VLAN de voz proriza Qos para telefonia ip
VLAN de gestión:
VLAN de invitados:
VLAN de transito:

Evitar VLAN1 para trafico de usuarios  utilizar solo para gestión
Limitar VLAN en trunk para reducir superficie de ataques solo poner las que queremos que entren

### DISEÑO LOGICO

las IP del Router
- V4 192.168.18.60
- Puerta de enlace predeterminada 192.168.18.1
Switch
- 192.168.180.61
Inventario*
	Router
Servicios=>DHCP
		   DDNS
		   LAN
		   VPN
	 Switch
	Servicios=>     VLAN Setting
				System Setting
				SNMP
				Port setting
				PoE+
				Spanning tree
				Link agregation
				Multicast/IP config
				LBD
				QoS


Rangos:
192.168.18.60-192.168.18.250
AP(acces point)

	Router
entrar: 192.168.18.1
Red: MANADA_DE_LOBAS
Contraseña: MANADADELOBAS123
	 Switch
entrar: 192.168.18.60
Usuario: admin
Contraseña:MANADADELOBAS




Características
Router
![[Pasted image 20251002094509.png]]


Switch


Preguntas y Concepto
Preguntas y Concepto

## 🔹 Conceptos por Capa (Modelo OSI) aplicados al Switch Linksys

### *Capa 2 (Enlace de datos)*

- *Definición: se encarga de la conmutación de tramas y del direccionamiento mediante **MAC addresses*.
    
- *Funciones en Linksys*:
    
    - *VLAN Setting*: segmentación lógica de la red.
        
    - *Spanning Tree*: evita bucles en la red.
        
    - *Port Setting*: configuración básica de velocidad y dúplex.
        
    - *Link Aggregation (LAG)*: unir varios puertos para mayor ancho de banda.
        
    - *LBD (Loopback Detection)*: detección de bucles en capa 2.
        
    - *PoE+*: energía por el puerto Ethernet a dispositivos (APs, cámaras IP, teléfonos VoIP).
        

---

### *Capa 3 (Red)*

- *Definición: maneja **direcciones IP*, permite comunicación entre diferentes redes y funciones de administración de tráfico.
    
- *Funciones en Linksys*:
    
    - *DHCP*: asignación automática de direcciones IP.
        
    - *DDNS*: actualización dinámica de nombres de dominio con IPs públicas.
        
    - *VPN*: soporte de redes privadas virtuales para acceso seguro.
        
    - *Multicast/IP Config*: gestión de tráfico multicast e IP de administración.
        
    - *SNMP (Simple Network Management Protocol)*: monitoreo remoto de dispositivos.
        
    - *System Setting*: configuración de la IP de administración del switch.
        

---

### *Capa 4 (Transporte)*

- *Definición: trabaja con **puertos TCP/UDP*, permitiendo priorización y control más avanzado de aplicaciones.
    
- *Funciones en Linksys*:
    
    - *QoS (Quality of Service)*: prioriza tráfico de voz, video o aplicaciones críticas.
        
        - Ejemplo: darle mayor prioridad al tráfico de *VoIP (puerto UDP 5060)* que a descargas.
            

---

## 🔹Switch Linksys

1. *¿Qué diferencia hay entre capa 2, 3 y 4?*
    
    - *Capa 2: direcciona con **MAC* y maneja conmutación, VLANs, STP, LAG.
        
    - *Capa 3: direcciona con **IP*, soporta funciones de enrutamiento básico, DHCP, SNMP, multicast.
        
    - *Capa 4: filtra y prioriza tráfico según **puertos TCP/UDP*, usado en QoS avanzado.
        
2. *¿Qué capa es nuestro switch Linksys?*
    
    - Un switch Linksys administrable *no es solo capa 2, porque maneja funciones de **red (DHCP, VPN, SNMP, multicast)*.
        
    - Tampoco es un firewall completo de capa 4, pero *sí ofrece QoS avanzado*.  
         Entonces: *es un switch de Capa 3 (multicapa) con capacidades limitadas de Capa 4 (QoS por puertos TCP/UDP).*



Tarea 2.2

![[Cuadro sinóptico de llaves moderno papel blanco.png]]
