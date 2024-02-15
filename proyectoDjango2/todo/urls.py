from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns= [
    path('',views.home,name="home"),
    path('admin/', admin.site.urls),
    path('agregar/',views.agregar,name="agregar"),
    path('clase/',views.clase,name="clase"),
    path("eliminar/<int:tarea_id>/",views.eliminar,name="eliminar"),
    path("editar/<int:tarea_id>/",views.editar,name="editar"),
    path('contacto/',views.contacto, name="contacto"),
    path('contacto/<str:nombre>',views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>',views.contacto, name="contacto"),
]
