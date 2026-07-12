
**Estudiante:** [MILTON CAMILO NINASUNTA OÑA]  
**Asignatura:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica  

---

Descripción del Sistema
Este sistema es una aplicación de consola modular desarrollada en Python para gestionar las operaciones básicas de un restaurante. Permite registrar, listar y buscar de forma dinámica tanto los productos del menú como los clientes del establecimiento, procesando los datos ingresados en tiempo real a través de una interfaz interactiva de comandos.

Estructura del Proyecto
El proyecto respeta una arquitectura modular por capas para separar las entidades de la lógica de negocio y el controlador de la interfaz de usuario:

```text
restaurante_app/
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── cliente.py
│
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
│
├── main.py
└── README.md