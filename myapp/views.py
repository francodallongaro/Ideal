from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from .models import *
from .forms import UsuarioForm
from django.http import Http404
from .filters import PropiedadFilter

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {})


def contacto(request):

    faqs = FAQ.objects.all()

    if request.method == 'POST':
            form = UsuarioForm(request.POST)
            
            if form.is_valid():

                # nombre = request.POST['nombre']
                # mensaje = request.POST['mensaje']
                # tel = request.POST['tel']
                # email = request.POST['email']

                # send_mail(
                #     'Consulta: ' + nombre,
                #     'Email: ' + email + ' Telefono: ' + tel + ' Cuerpo del mensaje: ' + mensaje,
                #     'francodallongaro@gmail.com',
                #     ['carrizo.ignacio1990@gmail.com', 'lopezfontenla.mlf@gmail.com'],
                #     fail_silently=False
                # )

                form.save()
                return render(request, 'myapp/success.html', {})
            else:
                return render(request, 'myapp/contacto.html', {"form": form, "error": form.errors, "faqs": faqs})
    else:
        form = UsuarioForm()
        return render(request, 'myapp/contacto.html', {"form": form, "faqs": faqs})

def venta(request):

    packs = Pack.objects.all()
    faqs = FAQ.objects.all()

    ctx = {
        'packs': packs,
        'faqs': faqs,
    }
    return render(request, 'myapp/venta.html', ctx)

def clasificados(request):

    clasificados = Clasificado.objects.all()

    # myFilter = PropiedadFilter(request.GET, queryset=clasificados)

    # clasificados = myFilter.qs
    # 'myFilter': myFilter,

    ctx = {
        'clasificados': clasificados,
    }

    return render(request, 'myapp/clasificados.html', ctx)

def portal(request):

    clasificados = Clasificado.objects.all()

    destacados = Clasificado.objects.filter(pack__nombre='ideal').order_by('creacion')[:3]

    ctx = {
        'clasificados': clasificados,
        'destacados': destacados
    }

    return render(request, 'myapp/portal.html', ctx)

def portal_detail(request, pk, *args, **kwargs):

    try:
        clasificado = Clasificado.objects.get(pk=pk)

    except Clasificado.DoesNotExist:
        raise Http404
    
    # clasificados = Propiedad.objects.all()
    # myFilter = PropiedadFilter(request.GET, queryset=clasificados)
    # clasificados = myFilter.qs



    ctx = {
        'clasificado': clasificado,
        # 'myFilter': myFilter,
    }

    return render(request, 'myapp/clasificado.html', ctx)

