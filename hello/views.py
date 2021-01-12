from django.shortcuts import render
from django.http import HttpResponse
from django.urls.base import reverse
from .models import *
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, "index.html")

def venta(request):
    return render(request, "venta.html")

def contacto(request):
    return render(request, "contacto.html")

def portal(request):
    return render(request, "portal.html")

# def portal_detail(request, pk, *args, **kwargs):

#     try:
#         clasificado = Clasificado.objects.get(pk=pk)

#     except Clasificado.DoesNotExist:
#         raise Http404
    
#     # clasificados = Propiedad.objects.all()
#     # myFilter = PropiedadFilter(request.GET, queryset=clasificados)
#     # clasificados = myFilter.qs



#     # ctx = {
#     #     'clasificado': clasificado,
#     #     # 'myFilter': myFilter,
#     # }

#     return render(request, 'clasificado.html')

