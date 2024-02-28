from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='saludo')
def saludo(value):
    largo=''
    if len(value)>=8:
        largo='<p>Tu nombre es muy largo </p>'
    return f'<h1 style="background: green;color:white;">Bienvenido, {value} </h1>'+largo

@register.filter(name='descuento')
def descuento(value, descuento):
    return f'${value - descuento}'

@register.filter(name='emoji_booleano')
def emoji_booleano(value):
    emojis = {
        True: '👍',
        False: '👎',
    }
    return emojis.get(value, '😐')

@register.filter(name='dia_semana')
def dia_semana(fecha):
    fecha = datetime.strptime(fecha, '%Y-%m-%d')
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return dias_semana[fecha.weekday()]