from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns= [
    path('',views.home,name="home"),
    path('inicio/',views.inicio,name="inicio"),
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

