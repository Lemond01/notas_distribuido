# Notas_distribuido
Este proyecto implementa un sistema de notas distribuido, en el que se usan contenedores Docker para alojar el servidor y el cliente que se comunican mediante sockets; permite al usuario crear, leer y eliminar notas. Además, puede exportar las notas en formato PDF/,txt, y se ha usado Docker para contenerizar tanto el servidor como el cliente.

## Organizacion de Contenido
notas_distribuido/
├── cliente/
│   ├── client.py                  // Contiene el código del cliente que interactúa con el servidor.
│   ├── Dockerfile                 // Contiene instrucciones para construir las imágenes Docker para cada uno de los servicios (cliente).
│   └── requirements.txt           // Lista las dependencias necesarias para ejecutar el cliente.
├── servidor/
│   ├── server.py                  // Contiene el código del servidor que maneja las solicitudes del cliente.
│   └── Dockerfile                 // Contiene instrucciones para construir las imágenes Docker para cada uno de los servicios (servidor).
├── docker-compose.yml             // Define cómo se deben ejecutar los contenedores de Docker para el cliente y el servidor.
├── README.md

## Instalación y Configuración del Proyecto
