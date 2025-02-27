# Proyecto Web en Django - Página de ventas de figuras de animé

## Descripción
Este es un proyecto web desarrollado en Django para el curso de **Programación Web, 2023** de **Ingeniería en Informática** en **Duoc UC, sede Antonio Varas**. 
La aplicación simula una página de ventas de figuras de animé. El proyecto incluye las secciones básicas de un e-commerce, tales como productos, carrito de compras y un CRUD sencillo para el administrador.

## Características
- Sección de productos de figuras de animé.
- Carrito de compras simulado.
- CRUD (Crear, Leer, Actualizar, Eliminar) de productos para el administrador.
- Interfaz sencilla y fácil de usar.

## Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes programas:
- **Python 3.12 o superior**: [Descargar Python](https://www.python.org/downloads/)
- **Django 4.1.2 o superior**: El proyecto está desarrollado con esta versión de Django.

## Instalación
1. **Clonar el repositorio**:
   
   **Abre tu terminal y clona el repositorio**
   ```cli
   git clone https://github.com/Pablo-Maldonado-Presas/ya-compra-kudasai.git
3. **Configuración en Windows *(Opcional, si hay restricciones de ejecución)***:
   
   Abrir PowerShell en modo administrador y ejecutar:
   ```cli
   Set-ExecutionPolicy Unrestricted
5. **Crear y activar un entorno virtual**:

   **Crear**
   ```cli
   python -m venv venv
   ```
   Activar (*Windows*)
   ```cli
   .\venv\Scripts\activate
   ```
   Activar (*macOS/Linux*)
   ```cli
   source venv/bin/activate 
   ```
6. **Migración y administración de base de datos** (*opcional*):
   - Ejecutar las migraciones de la base de datos para preparar el proyecto con los datos almacenados:
     ```cli
     python manage.py migrate
   - Crear un superusuario (para acceder al panel de administración de Django):
     ```cli
     python manage.py createsuperuser
## Ejecución y acceso a la página
1. **Ejecución**:
    ```cli
    python manage.py runserver
2. **Accesos**:
   - Página: http://127.0.0.1:8000
   - CRUD: http://127.0.0.1:8000/crud
     - Username: supervisor | Password: otakusftw
   - Interfaz de administración http://127.0.0.1:8000/admin
  
---
## Galería de capturas
Para ver capturas de pantalla de la aplicación, visita la [galería de imágenes](https://pablo-maldonado-presas.github.io/ya-compra-kudasai/gallery/).
