from django.shortcuts import render, redirect, HttpResponse
from.models import Tarea
from.forms import TareaForm
# Create your views here.
def home(request):
    tareas=Tarea.objects.all()
    context={'tareas':tareas}
    return render(request,'todo/home.html',context)
    
def agregar(request):
    if request.method=='POST':
        form=TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm()
        context={'form':form}
        return render(request,'todo/agregar.html',context)
    
def eliminar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('home')

def editar(request,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    if request.method=="POST":
        form=TareaForm(request.POST,instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TareaForm(instance=tarea)
    context={'form':form}
    return render(request,'todo/editar.html',context)

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
    
    return HttpResponse(template)