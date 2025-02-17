import os
import django

# Establecer la variable de entorno DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db.settings")

# Cargar la configuración de Django
django.setup()

from tienda.models import Categoria, Producto

categorias = [
    'Figura',
    'Manga',
    'Peluche',
    'Decoración',
    # Agrega más categorías si es necesario
]

productos = [
    {
        'nombre': 'Colección Manga Zetman',
        'descripcion': 'Tomo 1 al 20 de la última obra de Masakazu Katsura, en idioma japonés',
        'precio': 50000,
        'categoria': 'Manga'
    },
    {
        'nombre': 'Figura Rei Ayanami Plugsuit Style Pear - Evangelion',
        'descripcion': 'De la popular serie animé Rebuild of Evangelion, una figura a escala 1/7 de Rei Ayanami. Esculpida por Miki Ousaka, una figura llena de detalles para añadir a la colección',
        'precio': 170000,
        'categoria': 'Figura'
    },
    {
        'nombre': 'Colección Manga The Promised Neverland',
        'descripcion': 'Edición Limitada',
        'precio': 80000,
        'categoria': 'Manga'
    },
    {
        'nombre': 'Peluche Pikachu Maiko Han Geisha - Pokemon',
        'descripcion': 'Adorable peluche de la mascota ícono de la serie televisiva',
        'precio': 30000,
        'categoria': 'Peluche'
    },
    {
        'nombre': 'Figura Steel Knights XINGTIAN Mecha',
        'descripcion': 'JOYTOY',
        'precio': 90000,
        'categoria': 'Figura'
    },
    {
        'nombre': 'Figura Sukuna - Jujutsu Kaisen',
        'descripcion': 'Figura de colección',
        'precio': 35000,
        'categoria': 'Figura'
    },
    {
        'nombre': 'Figura Queen - One Piece',
        'descripcion': 'Bandai Spirits Ichibansho',
        'precio': 45000,
        'categoria': 'Figura'
    },
    {
        'nombre': 'Figura Kyoujuro Rengoku - Kimetsu no Yaiba',
        'descripcion': 'Bandai',
        'precio': 45000,
        'categoria': 'Figura'
    }
]

for producto_data in productos:
    categoria_nombre = producto_data.pop('categoria')
    categoria, _ = Categoria.objects.get_or_create(categoria=categoria_nombre)

    producto_data['id_categoria_id'] = categoria.id_categoria  # Asignamos el ID de la categoría al diccionario de datos

    producto, created = Producto.objects.get_or_create(nombre=producto_data['nombre'], defaults=producto_data)
    producto.id_categoria = categoria  # Asignamos la categoría al producto
    producto.descripcion = producto_data['descripcion']
    producto.precio = producto_data['precio']
    producto.save()
