from django.shortcuts import render,redirect,HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def holaMundo(request):
    return render(request,'holaMundo.html')

def saludo(request):
    return render(request,'saludo.html')

def presentacion(request):
    return render(request,'presentacion.html')

def quienesSomos(request):
    return render(request, 'quienessomos.html')

def productosyservicios(request):
    return render (request, 'productosyservicios.html')

def clase(request):
    template=""" <h1> Inicio</h1>
                <p>Años desde el 2024 al 2050</p>
                <ul>
             """
    year=2024
    while year<=2050:
        template += f"<li> {str(year)} </li>"
        year+=1
    template +="""</ul><hr>"""
  

    template+="""
                <p>Años Pares</p>
                <ul>
            """
    year=2024 
    while year<=2050:
        if year%2==0:
            template += f"<li> {str(year)}</li>"
        year+=1
    template +="""</ul><hr> """ 


    template +=""" 
                <p> Años impares</p>
                <ul>
            """
    year=2024
    while year<=2050:
        if year %2 !=0:
            template +=f"<li>{str(year)}</li>"
        year+=1
    template +="""</ul><hr> """


    template +="""
                <p>Años biciestos</p>
                <ul>
            """
    year=2024
    while year<=2050:
        if year % 4==0:
            template+= f"<li>{str(year)}</li>"
        year+=1
    template +=""" </ul><hr> """
    
    return render(request,'años.html')

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
    return render(request,'contacto.html')

