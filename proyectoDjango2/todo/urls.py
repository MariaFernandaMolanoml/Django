from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns= [
    path('',views.home,name="home"),
<<<<<<< HEAD
=======
    path('inicio/',views.inicio,name="inicio"),
>>>>>>> 8d181453d83d4553837ed4f7e12a0e11a912d9ab
    path('admin/', admin.site.urls),
    path('agregar/',views.agregar,name="agregar"),
    path('clase/',views.clase,name="clase"),
    path("eliminar/<int:tarea_id>/",views.eliminar,name="eliminar"),
    path("editar/<int:tarea_id>/",views.editar,name="editar"),
    path('contacto/',views.contacto, name="contacto"),
    path('contacto/<str:nombre>',views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>',views.contacto, name="contacto"),
    path('holaMundo/', views.holaMundo,name="holaMundo"),
    path('saludo/', views.saludo,name="saludo"),
    path('presentacion/', views.presentacion,name="presentacion"),
    path('productosyservicios/', views.productosyservicios,name="productosyservicios"),
    path('acercaDe/', views.quienesSomos, name="acercaDe"),
]

