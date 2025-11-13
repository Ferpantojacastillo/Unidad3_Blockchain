**Objetivo clase 1**
Es proponer soluciones de diferentes cosas para cuando resolver problemas 
**objetivo clase 2**: Saber cuales son los sistemas operativos y sus herramientas
Que es un sistema operativo distribuido? es un sistema que gestiona un conjunto de computadoras independientemente.

virtualización: técnica que permite representar virtualmente un sistema operativo(proceso de software para representar hardware físico o sistema operativo).
 **objetivo día 3** : Empezar a ver los beneficios de los sistemas operativos distribuidos y la virtualización 
 Ahorro de recursos de hardware 
 Reducción de costos 
 Escalabilidad y flexibilidad
 Aislamiento 
 Alta disponibilidad y recuperación ante desastres 
 Pruebas y desarrollos 
 Seguridad 
 Gestión centralizada 
 Migración en caliente 
 optimización del ciclo de vida de hardware 
 
*Objetivo día 4*
 Repasar que es un sistema operativo y analizar las características de la virtualización 
¿Por qué es importante un sistema operativo? porque con este es del modo que algún dispositivo funcione bien. 
¿Cómo funciona un sistema operativo? pues es como un intermediario entre el dispositivo y un usuario este hace que funcionen los programas en nuestro dispositivo 
¿Qué componentes conocen?
¿Cuáles sistemas operativos conocen? Windows, IOS, Android.
¿Cuáles diferencias hay entre los SO que conocen? Pues que por ejemplo en Android solo se utiliza en Celulares Y que pues como El IOS solo en dispositivos Mac.

Características Clave de la virtualización 
**Abstracción de hardware**: capa intermedia entre el hardware real y el software, que traduce las operaciones del programa en instrucciones que el hardware entiende, sin que el programador tenga que preocuparse por cómo funciona cada componente físico.
**Portabilidad**: Se refiere a la capacidad de un software de ser ejecutado en diferentes maquinas o sistemas operativos. 
**Escalabilidad**: es la capacidad de un sistema, proceso o tecnología de adaptarse y **crecer** al aumentar la carga de trabajo o la demanda, manteniendo un buen rendimiento sin perder eficiencia. 
**Flexibilidad de entornos**:capacidad para adaptarse a los requisitos de hardware
**Snapchots y clonación**:es una copia instantánea del estado de un sistema, son archivos de solo lectura que se crean rápido y de forma eficiente, útiles para la protección de datos, restaurar un sistema y para prueba de software.  

Tarea Tabla comparativa de las supercomputadoras
 

|                          | El Capitán                   | Frontier                  | Aurora                          | JUPITER booster                     | Eagle                                 | HPC6                    | Fugaku                    | Alps                          | Lumi                    | Miztli                   |
| :----------------------- | ---------------------------- | ------------------------- | ------------------------------- | ----------------------------------- | ------------------------------------- | ----------------------- | ------------------------- | ----------------------------- | ----------------------- | ------------------------ |
| CPU                      | AMD 4th Gen EPYC 24C 1.8 GHz | AMD EPYC 64C 2.0 GHz      | Intel Xeon Max 9470 52C 2.4 GHz | SiPearl GH200 Superchip 72C 3.0 GHz | Intel Xeon Platinum 8480C 48C 2.0 GHz | AMD EPYC 64C 2.0 GHz    | Fujitsu A64FX 48C 2.2 GHz | NVIDIA Grace 72C 3.1 GHz      | AMD EPYC 64C 2.0 GHz    | Intel Xeon 8,344 núcleos |
| GPU                      | AMD Instinct MI300A.         | 4× AMD Instinct MI250X    | Intel Data Center GPU Max       | NVIDIA GH200 Superchip              | NVIDIA H100                           | AMD Instinct MI250X     |                           | NVIDIA GH200 Superchip        | AMD Instinct MI250X     | AMD Instinct MI250X      |
| Interconexión            | HPE Slingshot-11             | Slingshot-11              | Slingshot-11                    | Quad-Rail NVIDIA InfiniBand NDR200  | NVIDIA InfiniBand NDR                 | Slingshot-11            | Tofu D                    | Slingshot-11                  | Slingshot-11            | Infiniband QDR 40 Gbps   |
| almacenamientos          | Lustre multinivel (PBs)      | 679 PB Orion Lustre       | Lustre multinivel (PBs)         | Lustre multinivel (PBs)             | Azure Storage (PBs)                   | Lustre multinivel (PBs) | Lustre multinivel (PBs)   | Lustre multinivel (PBs)       | Lustre multinivel (PBs) | 750 TB Lustre            |
| Sistema de refrigeración | Líquida directa              | Líquida directa           | Líquida directa                 | Líquida directa                     | Aire/Líquida (centros Azure)          | Líquida directa         | Líquida directa           | Líquida directa               | Líquida directa         | Líquida/Aire             |
| Ubicación                | LLNL, California (EE. UU.)   | ORNL, Tennessee (EE. UU.) | Argonne, Illinois (EE. UU.)     | Jülich, Alemania                    | Microsoft Azure, EE. UU.              | AWS (EE. UU.)           | RIKEN, Japón              | HPE (localización no pública) | CSC, Finlandia          | UNAM, Ciudad de México   |
| Sistema operativo        | TOSS                         | HPE Cray OS               | Linux (RHEL/Cray Linux)         | Red Hat Enterprise Linux            | Linux (Azure HPC OS)                  | RHEL 8.9                | IHK/McKernel + Linux      | HPE Cray OS                   | HPE Cray OS             | RHEL / Scientific Linux  |
|                          |                              |                           |                                 |                                     |                                       |                         |                           |                               |                         |                          |

Objetivo día 5 
Lineal del tiempo de los sistemas operativos 
![[Pasted image 20250904103906.jpg]]
Objetivo día 6
Analizar las características clave de los sistemas operativos distribuidos 
Trasparecía: la característica que oculta al usuario y al programador la naturaleza compleja de un  servidor distribuido.
Recursos Compartidos: un método para organizar 
Escalabilidad: un sistema operativo puede escalar fácilmente añadiendo mas nodos al sistema.
Tolerancia a fallos: son sistemas que permiten que los discos sean tolerantes a fallos
Concurrencia: múltiples procesos pueden ejecutarse simultáneamente en diferentes nodos sin que falle.
Comunicación y coordinación : se necesitan comunicarse entre si y para lograr esto es atreves de protocolos de comunicación RPC o mensaje y debe de haber una coordinación 
*Ejemplos de sistemas operativos distribuidos*
Google File System
Apache Hadoop HDFS
PelicanHPC

La virtualización es usar un solo hardware físico para crear varias máquinas virtuales independientes, como si fueran computadoras separadas dentro de una misma.
Un sistema operativo distribuido es aquel que hace que un conjunto de computadoras conectadas en red funcionen como si fueran una sola, compartiendo recursos y tareas de manera coordinada.
La diferencia entre estos es que la virtualización se divide en muchos y el sistema operativo distribuido es que muchos se juntan en uno. 
**Conceptos básicos**
Sistemas de archivos: conjunto de reglas y estructuras, todo tiene un lugar físico.
Windows                 Linux 
NTFS - 16TB           ext4 - 16 TB
Fat32 - 46B              ext3 - 2 TB
Fat16 - 26b
exfat - 16 EB 

Examen 
¿Qué es Docker ?
¿Qué es virtualización?
¿Qué es un sistema operativo distribuido?
¿Diferencia entre sistema operativo y virtualización?
