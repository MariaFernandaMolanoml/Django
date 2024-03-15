from django.contrib import admin
from django.urls import path,include
from .import views
from django .conf import settings

urlpatterns = [
    path ('admin/', admin.site.urls),
    path('inicio/',views.inicio,name="inicio"),
    path('clase/',views.clase,name="clase"),
    path('contacto/',views.contacto, name="contacto"),
    path('contacto/<str:nombre>',views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>',views.contacto, name="contacto"),
    path('holaMundo/', views.holaMundo,name="holaMundo"),
    path('saludo/', views.saludo,name="saludo"),
    path('presentacion/', views.presentacion,name="presentacion"),
    path('productosyservicios/', views.productosyservicios,name="productosyservicios"),
    path('quienesSomos/', views.quienesSomos, name="quienesSomos"),
    path('crearArticulo/',views.crearArticulo, name="crearArticulo"),
    path('crearArticulo/<str:title>/<str:content>/<str:public>',views.crearArticulo, name="crearArticulo"),
    path('articulo/',views.articulo,name="articulo"),
    path('editar_articulo/',views.editar_articulo,name="editar_articulo"),
    path('articulos/', views.articulos, name="articulos"),
    path('borrar_articulos/<int:id>', views.borrar_articulos, name= "borrar_articulos"),
    path('editar-articuloSQL/<int:id>/<str:title>/<str:content>/<str:public>', views.editar_articulo_sql, name="editarArticuloSQL"),
    path('borrar-articuloSQL/<int:id>', views.eliminar_articulo_sql, name="borrarSQL"),
    # path('createArticulo/', views.saveArticulo, name="createArticulo"),
    path('createArticulo/', views.create_articulo, name="create"),
    path('create-full-articulo/', views.create_full_articulo, name="create_full"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)