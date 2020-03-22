from django.shortcuts import render
from .models import project
# Create your views here.
# vista dinamica enlazada a la base de datos
def porfolio(request):
    projects = project.objects.all()
    return render(request, 'portofolio/portafolio.html',{'projects':projects})