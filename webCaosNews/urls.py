from django.contrib import admin
from django.urls import path
from webCaosNews import views
from django.conf import settings

# Importar rutas estáticas.
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='inicio'),
    path('detallenoticia/', views.detalleNoticia, name='detalleNoticia'),
    path('formularionoticia/', views.formularioNoticia, name='formularioNoticia'),
    path('paginaautor/', views.paginaAutor, name='paginaAutor'),
    path('login/', views.login, name='login'),
    path('cerrarsesion/', views.cerrarSesion, name='cerrarSesion'),
    path('noticia/<id>/', views.noticia, name='noticia'),
    path('filtrocategoria/', views.filtroCategoria, name='filtroCategoria'),
    path('filtropalabraclave/', views.filtroPalabraClave, name='filtroPalabraClave'),
    path('filtrocategoriaid/<id>/', views.filtroCategoriaId, name='filtroCategoriaId'),
    path('registrousuario/', views.registroUsuario, name='registroUsuario'),
    path('administracionnoticia/', views.administracionNoticia, name='administracionNoticia'),
    path('eliminarnoticia/<id>/', views.eliminarNoticia, name='eliminarNoticia'),
    path('modificarnoticia/<id>/', views.modificarNoticia, name='modificarNoticia'),
    path('actualizarnoticia/', views.actualizarNoticia, name='actualizarNoticia'),
    path('cargarimagengaleria/', views.cargarImagenGaleria, name='cargarImagenGaleria'),
]

# Incluir rutas estáticas.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)