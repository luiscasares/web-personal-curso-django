from django.shortcuts import render, HttpResponse, Http404
import datetime
# Create your views here.


#Vistas creadas usando métodos
def home(request):
    #hora = datetime.datetime.now()
    #return HttpResponse(html_base + """<h1>Mi web personal</h1><h2>Portada</h2> <p>La fecha es %s </p>""" % hora)
    return render(request, 'core/home.html')

def acerca(request):
    return render(request, 'core/acerca.html')

def contacto(request):
    return render(request, 'core/contacto.html')
    


