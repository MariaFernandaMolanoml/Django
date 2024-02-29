from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
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
    path('articulos/', views.articulos, name= "articulosLista"),
]