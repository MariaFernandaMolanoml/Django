from django.shortcuts import render,redirect,HttpResponse
from miApp.models import Article
from django.db import connection
from django.db.models import Q
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def holaMundo(request):
    lista = []
    i = 0
    while i < 5:
        lista.append("Hola mundo")
        i += 1
    return render(request,'holaMundo.html', {'lista': lista})


def saludo(request):
    lista_saludos = ["¡Hola!", "¡Buenos días!", "¡Buenas tardes!", "¡Buenas noches!", "¡Hola de nuevo!"]

    return render(request,'saludo.html', {
        'lista_saludos': lista_saludos
        })


def presentacion(request):
    listaAspectos = []
    for i in range(1, 6):
        listaAspectos.append(f"Aspecto {i}")

    return render(request,'presentacion.html',{'listaAspectos': listaAspectos})



def quienesSomos(request):
    return render(request, 'quienessomos.html')



def productosyservicios(request):
    return render (request, 'productosyservicios.html')



def clase(request):
        nombre='Maria Fernanda'
        años = [año for año in range(2024, 2051)]
        añosPares = [año for año in años if año % 2 == 0]
        añosImpares = [año for año in años if año % 2 != 0]
        añosBisiestos = [año for año in años if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)]

        return render(request,'años.html',{
            'años': años,
            'añosPares': añosPares,
            'añosImpares': añosImpares, 
            'añosBisiestos': añosBisiestos,
            'mi_variable':'soy un gato que esta en la vista',
            'titulo':'Años',
            'name':nombre
        })

    


def contacto(request, nombre="", apellido=""):
    html=""
    if nombre and apellido:
        html= "<h2> Nombre completo: </h2>"
        html+= f"<h2> Bienvenido {nombre} {apellido} </h2>"
    elif nombre:
        html= "<h2> Nombre sin apellido: </h2>"
        html+= f"<h2> Bienvenido {nombre} </h2>"
    elif apellido:
        html= "<h2> Apellido sin nombre : </h2>"
        html+= f"<h2> Bienvenido {apellido} </h2>"
    else:
        html= "<h2> Sin nombre y apellidos definidos </h2>"


    contacto= """
            Bienvenido al apartado de contactos :
            """
    # return HttpResponse(contacto+f"<h2>Contacto </2>"+html)
    return render(request,'contacto.html', {'texto':''})


# def contacto(request):
#     # Ejemplo de bucle for
#     nombres = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
#     i = 0
#     nombres_while = []
#     while i < len(nombres):
#         nombres_while.append(nombres[i])
#         i += 1


#     # Pasar las listas a la plantilla
#     context = {
#     'nombres_while': nombres_while,
#     }

    # return render(request, 'presentacion.html', context)

# year=2024
# hasta=range(year,2050)

def crearArticulo(request,title,content,public):
    articulo=Article(
    title= title,
    content= content,
    public= public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")

def articulo(request):
    try:
        articulo=Article.objects.get(pk=1, public=True)
        response= f"Articulo consultado: {articulo.title} - {articulo.content}- Estado{articulo.public} "
    except:
        response="<strong>Articulo no encontrado</strong>"
    return HttpResponse(response)

def editar_articulo(request):
    articulo=Article.objects.get(pk=6)
    articulo.content="Novela de Gabo"
    articulo.title="Los 12 cuentos peregrinos"
    articulo.public=True
    articulo.save()
    return HttpResponse(f"El articulo {articulo.id} de nombre: {articulo.title} ha sido actualizado y se estado es: {articulo.public}")

def articulos(request):
    articulos=Article.objects.order_by('id')
    #articulos=Article.objects.filter(public=True,id=5)
    #Lookups en Django
    #articulos=Article.objects.filter(title__contains="analisis y desarrollo de software")
    #articulos=Article.objects.filter(title__iexact="analisis y desarrollo de software")
    #articulos=Article.objects.filter(id__gt=9)
    #articulos=Article.objects.filter(id__in=[1,17,19])
    #articulos=Article.objects.filter(id__range=(3,6))
    #articulos=Article.objects.filter(title__contains="Ana").exclude(public=True)
    articulos=Article.objects.filter(Q(title__contains="analisis")|Q(public=0))

    return render(request,'articulos.html', { 
        'articulos':articulos
    })


def borrar_articulos(request, id):
    # articulos= Article.objects.raw("DELETE FROM miapp_article where id=7")
    articulos=Article.objects.get(pk=id)
    articulos.delete()
    return redirect ('articulosLista')

def editar_articulo_sql(request, id, title, content, public):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE miapp_Article SET title=%s, content=%s, public=%s WHERE id=%s", [title, content, public, id])
    return redirect('articulosLista')

def eliminar_articulo_sql(request, id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM miapp_article WHERE id=%s", [id])
    return redirect('articulosLista')


def saveArticulo(request):
    articulo=Article(
    title= title,
    content= content,
    public= public,
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} ")


def create_articulo(request):
    return render(request,'crear_articulo.html')

