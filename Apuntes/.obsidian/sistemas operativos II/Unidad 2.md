¿Qué es Docker?

Docker es una plataforma de virtualización basada en contenedores. Su objetivo es permitir que una aplicación, junto con todas sus dependencias (bibliotecas, configuraciones, herramientas, etc.), se ejecute de forma consistente en cualquier entorno: una computadora local, un servidor o la nube.

Los contenedores son ligeros, portables y están aislados, lo que evita problemas como “en mi máquina sí funciona”.

## ¿Por qué es más eficiente que una máquina virtual?

A diferencia de una máquina virtual tradicional:

- Los contenedores no requieren un sistema operativo completo.
    
- Comparten el kernel del sistema anfitrión.
    
- Se inician rápidamente.
    
- Consumen menos memoria y almacenamiento.
    

Esto permite una mejor velocidad, uso eficiente de recursos y facilidad para desplegar aplicaciones.


## Arquitectura básica de Docker

### 1. Docker Engine

Es el núcleo de Docker e incluye:

- *Docker Daemon (dockerd)*  
    Proceso en segundo plano responsable de gestionar:
    
    - Contenedores
        
    - Imágenes
        
    - Redes
        
    - Volúmenes
        
- *Docker CLI (interfaz de línea de comandos)*  
    Herramienta que permite al usuario ejecutar comandos como:
    
    - docker run
        
    - docker pull
        
    - docker ps
        
- *API REST*  
    Permite que otras aplicaciones o servicios interactúen con el daemon.
    



### 2. Imágenes

- Son plantillas inmutables que contienen el entorno necesario para ejecutar una aplicación.
    
- Se construyen generalmente a partir de un Dockerfile.
    
- Están organizadas por capas, lo que optimiza espacio y descargas.
    
- Pueden almacenarse en registros públicos o privados, como Docker Hub.
    



### 3. Contenedores

- Son instancias en ejecución de una imagen.
    
- Funcionan como procesos aislados que comparten el kernel del sistema host.
    
- Se pueden iniciar, detener, eliminar y listar mediante comandos como:
    
    - docker run
        
    - docker stop
        
    - docker rm
        
    - docker ps
        

Es posible ejecutar varios contenedores creados desde la misma imagen de forma independiente.



## Elementos adicionales

### Redes

Permiten la comunicación entre contenedores o entre contenedores y el exterior. Las más comunes son:

- bridge (por defecto)
    
- host
    
- overlay
    

### Volúmenes

Espacios utilizados para almacenar datos persistentes aunque el contenedor se elimine o reinicie.


## ¿Por qué usar Docker para WordPress?

1. Instalación rápida: no necesitas configurar manualmente cada componente.
    
2. Ambiente limpio y aislado: no modifica tu sistema operativo.
    
3. Portabilidad: puedes llevar el proyecto a otra computadora fácilmente.
    
4. Control de versiones: eliges qué versión de PHP, MySQL o WordPress usar.
    
5. Escalabilidad: puedes tener varios sitios sin conflictos.
    



## Componentes básicos al usar Docker con WordPress

Normalmente se utilizan dos contenedores principales:

### 1. Contenedor de WordPress

Incluye:

- Archivos de WordPress
    
- PHP
    
- Servidor web (como Apache)
    

Se accede desde el navegador, por ejemplo: localhost:8080.

### 2. Contenedor de base de datos (MySQL o MariaDB)

Guarda toda la información del sitio:

- Usuarios
    
- Entradas
    
- Configuración
    
- Plugins, etc.
  
## Ventajas

- No necesitas instalar WordPress manualmente.
    
- Puedes eliminar todo fácilmente si ya no lo necesitas.
    
- El sitio se puede replicar en otra computadora sin cambiar su apariencia.
    
- Es ideal para desarrollo y pruebas.
    



Examen 
¿Qué es Docker ? programa que permite crear y usar contenedores, que son espacios aislados donde se ejecutan aplicaciones.

¿Qué es virtualización? es crear versiones simuladas como computadoras o sistemas dentro de una sola maquina física. (mucho software en un hardware )

¿Qué es un sistema operativo distribuido? podemos usar 1 o mas hardware

¿Diferencia entre sistema operativo y virtualización? el sistema operativo usa varias computadoras como si fuera una sola mientras que la virtualización divide una computadora en varias maquinas simuladas.

Diferencia entre Docker y un maquina virtual? una maquina virtual se ejecuta sobre el sistema operativo y el Docker se puede conectar directamente al kernel.

**Comandos básicos Docker **

Consultar imágenes(Docker images)
Consultar contenedores(Docker ps)
Instalar una imagen( Docker run)
Arrancar un contenedor(Docker star)
Descargar imágenes(docker pull( nombre de imagen))
Para parar contenedor(Docker stop )
Eliminar un contenedor y una imagen(contenedor(Docker rm) imagen(docker rmi))
Respaldar(docker save -o respaldo.tar Nombre _imagen: etiqueta)

¿Qué es el kernel? es el núcleo del sistema operativo 
¿Contenedor vs imágenes en Docker diferencia? imagen es plantilla de la app y contenedor es imagen en ejecución. 

