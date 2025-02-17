from django.shortcuts import render, get_object_or_404, redirect
from tienda.models import Producto, Categoria
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User

# Create your views here.


def inicio(request):
    return render(request, 'inicio.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle_producto.html', {'producto': producto})

def contacto(request):
    return render(request, 'contacto.html')


# AUTENTICACIÓN
class CustomLoginView(LoginView):
    template_name = 'login.html'
    
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'



# CRUD
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def index(request):
    productos= Producto.objects.all()
    context={"productos":productos}
    return render(request, 'productos/index.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def listadoSQL(request):
    productos= Producto.objects.raw('SELECT * FROM productos_producto')
    print(productos)
    context={"productos":productos}
    return render(request, 'productos/listadoSQL.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def crud(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'productos/productos_list.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def productosAdd(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        categoria = request.POST.get('categoria')
        stock = request.POST.get('stock')

        objCategoria = Categoria.objects.get(id_categoria=categoria)
        obj = Producto.objects.create(id=id,
                                      nombre=nombre,
                                      descripcion=descripcion,
                                      precio=precio,
                                      id_categoria=objCategoria,
                                      stock=stock)
        obj.save()
        context = {'mensaje': "Ok, datos grabados..."}
        return render(request, 'productos/productos_add.html', context)
    else:
        categorias = Categoria.objects.all()
        
        ultimo_producto = Producto.objects.order_by('-id').first()
        if ultimo_producto:
            nueva_id = ultimo_producto.id + 1
        else:
            nueva_id = 1  # Si no hay productos existentes, asigna el ID 1

        context = {'categorias': categorias, 'nueva_id': nueva_id}
        return render(request, 'productos/productos_add.html', context)        

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def productos_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id=pk)

        producto.delete()
        mensaje="Bien, datos eliminados..."
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'productos/productos_list.html', context)
    except:
        mensaje="Error, id no existe..."
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje': mensaje}
        return render(request, 'productos/productos_list.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def productos_findEdit(request,pk):
    if pk != "":
        producto=Producto.objects.get(id=pk)
        categorias=Categoria.objects.all()

        print(type(producto.id_categoria.categoria))

        context={'producto':producto,'categorias':categorias}
        if producto:
            return render(request, 'productos/productos_edit.html', context)
        else:
            context={'mensaje':"Error, id no existe..."}
            return render(request, 'productos/productos_list.html', context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_authenticated and user.username == 'supervisor', login_url='login')
def productosUpdate(request):
    if request.method == "POST":
        id=request.POST["id"]
        nombre=request.POST["nombre"]
        descripcion=request.POST["descripcion"]
        precio=request.POST["precio"]
        categoria=request.POST["categoria"]
        stock=request.POST["stock"]

        objCategoria=Categoria.objects.get(id_categoria = categoria)

        producto = Producto()
        producto.id=id
        producto.nombre=nombre
        producto.descripcion=descripcion
        producto.precio=precio
        producto.id_categoria=objCategoria
        producto.stock=stock
        producto.save()

        categorias=Categoria.objects.all()
        context={'mensaje':"Ok, datos actualizados...",'categorias':categorias, 'producto':producto }
        return render(request, 'productos/productos_edit.html', context)
    else:
        productos = Producto.objects.all()
        context={'productos':productos}
        return render(request, 'productos/productos_list.html', context)