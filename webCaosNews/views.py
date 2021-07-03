from django.db.models.fields import AutoField
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime

# Tabla Categoria
from .models import Categoria, Noticia, Galeria

# PARA LOGIN ###################################################################
# Tabla Usuarios del sistema
from django.contrib.auth.models import User

# Validaciones de login
from django.contrib.auth import authenticate, logout, login as login_aut

# Decoradores
from django.contrib.auth.decorators import login_required
###################################################################


def registroUsuario(request):
    mensaje = ''

    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtApellido")
        usuario = request.POST.get("txtUsuario")
        email = request.POST.get("txtMail")
        password = request.POST.get("txtContrasena")

        try:
            usu = User()
            usu.first_name = nombre
            usu.last_name = apellido
            usu.email = email
            usu.username = usuario
            usu.set_password(password)
            usu.save()
            messages.success(request, '¡Usuario creado correctamente!')

            # Método ir a Index.
            categorias = Categoria.objects.all() #Equivale a un select * from categoria;
            noticias = Noticia.objects.all()
            cantNoticias = Noticia.objects.all().count()
            return render(request, "index.html", {"cat":categorias, "not":noticias, "cant":cantNoticias})
            

        except:
            messages.success(request, 'No se pudo crear el usuario.')
        
    return render(request, "registroUsuario.html")

def cerrarSesion(request):
    logout(request)
    # Método ir a Index.
    categorias = Categoria.objects.all() #Equivale a un select * from categoria;
    noticias = Noticia.objects.all()
    cantNoticias = Noticia.objects.all().count()
    messages.success(request, '¡Has cerrado sesión correctamente!')
    return render(request, "index.html", {"cat":categorias, "not":noticias, "cant":cantNoticias})

def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        contrasena = request.POST.get("txtContrasena")
        acceso = authenticate(request, username = usuario, password = contrasena)

        if acceso is not None and acceso.is_active:
            login_aut(request, acceso)
            # Método ir a Index.
            categorias = Categoria.objects.all() #Equivale a un select * from categoria;
            noticias = Noticia.objects.all()
            cantNoticias = Noticia.objects.all().count()
            messages.success(request, '¡Has iniciado sesión correctamente!')
            return render(request, "index.html", {"cat":categorias, "not":noticias, "cant":cantNoticias})

        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, "login.html") 

def filtroCategoria(request):
    noticias = Noticia.objects.all()
    cantNoticias = Noticia.objects.all().count()
    if request.POST:
        categoria = request.POST.get("cboCategoria")
        objCategoria = Categoria.objects.get(nombre = categoria)
        noticias = Noticia.objects.filter(Categoria = objCategoria)
        noticiasCarrusel = Noticia.objects.filter(activo=True).order_by('-fecha')[:3]
        cantNoticias = Noticia.objects.filter(Categoria = objCategoria).count()

    categorias = Categoria.objects.all()
    return render(request, "index.html", {"not":noticias, "cat":categorias, "cant":cantNoticias, "notcar":noticiasCarrusel})

def filtroCategoriaId(request, id):
    objCategoria = Categoria.objects.get(nombre = id)
    noticias = Noticia.objects.filter(Categoria = objCategoria)
    cantNoticias = Noticia.objects.filter(Categoria = objCategoria).count()
    noticiasCarrusel = Noticia.objects.filter(activo=True).order_by('-fecha')[:3]

    categorias = Categoria.objects.all()
    return render(request, "index.html", {"not":noticias, "cat":categorias, "cant":cantNoticias, "notcar":noticiasCarrusel})

def filtroPalabraClave(request):
    noticias = Noticia.objects.all()
    cantNoticias = Noticia.objects.all().count()
    if request.POST:
        keyword = request.POST.get("txtKeyword")
        noticias = Noticia.objects.filter(titulo__contains = keyword)
        cantNoticias = Noticia.objects.filter(titulo__contains = keyword).count()
        noticiasCarrusel = Noticia.objects.filter(activo=True).order_by('-fecha')[:3]

    categorias = Categoria.objects.all()
    return render(request, "index.html", {"not":noticias, "cat":categorias, "cant":cantNoticias, "notcar":noticiasCarrusel})

def noticia(request, id):
    noticias = Noticia.objects.get(id=id)
    categorias = Categoria.objects.all() #Equivale a un select * from categoria;
    galeria = Galeria.objects.filter(Noticia = noticias)
    return render(request, "noticia.html", {"cat":categorias, "not":noticias, "galeria":galeria})

def index(request):
    categorias = Categoria.objects.all() #Equivale a un select * from categoria;
    noticias = Noticia.objects.filter(activo=True)
    noticiasCarrusel = Noticia.objects.filter(activo=True).order_by('-fecha')[:3]
    cantNoticias = Noticia.objects.filter(activo=True).count()
    return render(request, "index.html", {"cat":categorias, "not":noticias, "cant":cantNoticias, "notcar":noticiasCarrusel})

def detalleNoticia(request):
    return render(request, "detalleNoticia.html")

@login_required(login_url='/login/')
def formularioNoticia(request):
    if request.POST:
        titulo = request.POST.get("txtTitulo")
        lead = request.POST.get("txtLead")
        categoria = request.POST.get("selCategoria")
        imagen = request.FILES.get("inputImagen")
        cuerpo = request.POST.get("txtCuerpo")
        fecha = datetime.now()

        objCat = Categoria.objects.get(nombre = categoria) #Buscar el obj categoría.

        noticia = Noticia()
        noticia.titulo = titulo
        noticia.lead = lead
        noticia.cuerpo = cuerpo
        noticia.fecha = fecha
        noticia.periodista = request.user.username

        if imagen is not None:
            noticia.imagen = imagen

        noticia.Categoria = objCat

        noticia.save()
        messages.success(request, 'Noticia registrada con éxito.')

    categorias = Categoria.objects.all()

    datos = {"cat":categorias}
    return render(request, "formularioNoticia.html", datos)

def paginaAutor(request):
    return render(request, "paginaAutor.html")

@login_required(login_url='/login/')
def administracionNoticia(request):
    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(periodista = request.user.username)
    contadorNoticias = Noticia.objects.filter(periodista = request.user.username).count()
    contadorNoticiasActivas = Noticia.objects.filter(activo=True, periodista = request.user.username).count()
    contadorNoticiasInactivas = contadorNoticias - contadorNoticiasActivas

    datos = {"cat":categorias, "not":noticias, "cant":contadorNoticias, "cantActiva":contadorNoticiasActivas, "cantInactiva":contadorNoticiasInactivas}

    return render(request, "administracionNoticia.html", datos)

@login_required(login_url='/login/')
def eliminarNoticia(request, id):
    mensaje = ''
    try:
        noticia = Noticia.objects.get(id = id)
        noticia.delete()
        mensaje = "¡Noticia eliminada correctamente!"
    except:
        mensaje = "No existe la noticia."

    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(periodista = request.user.username)

    datos = {"mensaje":mensaje, "cat":categorias, "not":noticias}

    return render(request, "administracionNoticia.html", datos)
    
@login_required(login_url='/login/')
def modificarNoticia(request, id):
    mensaje = ''

    try:
        noticia = Noticia.objects.get(id = id)
        categorias = Categoria.objects.all()

        datos = {"cat":categorias, "not":noticia}
        return render(request, "modificarnoticia.html", datos)

    except:
        mensaje = "No existe la noticia."

    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(periodista = request.user.username)

    datos = {"mensaje":mensaje, "cat":categorias,"not":noticias}

    return render(request, "administracionNoticia.html", datos)

@login_required(login_url='/login/')
def actualizarNoticia(request):
    mensaje = ''

    if request.POST:
        id = request.POST.get("txtId")
        titulo = request.POST.get("txtTitulo")
        lead = request.POST.get("txtLead")
        categoria = request.POST.get("selCategoria")
        imagen = request.FILES.get("inputImagen")
        cuerpo = request.POST.get("txtCuerpo")

        objCat = Categoria.objects.get(nombre = categoria) #Buscar el obj categoría.
        objNot = Noticia.objects.get(id = id)

        try:
            objNot.titulo = titulo
            objNot.lead = lead
            objNot.categoria = objCat
            objNot.cuerpo = cuerpo
            objNot.comentario = 'Modificado.'

            if imagen is not None:
                objNot.imagen = imagen
            objNot.save()

            mensaje = "Noticia modificada"

        except:
            mensaje = "Noticia no modificada"

    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(periodista = request.user.username)

    datos = {"mensaje":mensaje, "cat":categorias, "not":noticias}
    return render(request, "administracionNoticia.html", datos)

@login_required(login_url='/login/')
def cargarImagenGaleria(request):
    mensaje = ''

    if request.POST:
        idNoticia = request.POST.get("txtIdNoticia")
        imagen = request.FILES.get("inputImagen")
        objNoticia = Noticia.objects.get(id = idNoticia)

        galeria = Galeria()
        galeria.imagen = imagen
        galeria.Noticia = objNoticia
        galeria.save()

        mensaje = "Agregó imagen a noticia de ID" + idNoticia

    categorias = Categoria.objects.all()
    noticias = Noticia.objects.filter(periodista = request.user.username)
    datos = {"cat":categorias, "not":noticias, "mensaje":mensaje}

    return render(request, "administracionNoticia.html", datos)