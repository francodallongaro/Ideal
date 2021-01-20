from django.shortcuts import render
from django.http import HttpResponse
from django.urls.base import reverse
from .forms import *
from .models import *
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, "index.html")

def venta(request):

    faqs = Faqs.objects.all()
    packs = Pack.objects.all()

    ctx = {
        'faqs': faqs,
        'packs': packs,
    }

    return render(request, "venta.html", ctx)

def contacto(request):

    faqs = Faqs.objects.all()

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
                return render(request, 'index.html', {})
            else:
                return render(request, 'venta.html', {"faqs": faqs})
    else:
        form = UsuarioForm()
        return render(request, 'contacto.html', {"form": form, "faqs": faqs})

    ctx = {
        'faqs': faqs,
    }

    return render(request, "contacto.html", ctx)

def contacto2(request, pk, *args, **kwargs):

    pack = Pack.objects.get(pk=pk)

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
                return render(request, 'index.html', {})
            else:
                return render(request, 'venta.html', {"pack": pack})
    else:
        form = UsuarioForm()
        return render(request, 'contacto2.html', {"form": form, "pack": pack})

    ctx = {
        'pack': pack,
    }

    return render(request, "contacto2.html", ctx)

def portal(request):

    clasificados = Clasificado.objects.all()
    cuenta = Clasificado.objects.all().count()
    

    # destacados = Clasificado.objects.filter(pack__nombre='ideal').order_by('creacion')[:3]

    ctx = {
        'clasificados': clasificados,
        'cuenta': cuenta,
    }

    return render(request, 'portal.html', ctx)

def clasificado_detalle(request, pk, *args, **kwargs):

    # try:
    clasificado = Clasificado.objects.get(pk=pk)

    tipologia = clasificado.tipologia
    print(tipologia)
    # except Clasificado.DoesNotExist:
    #     raise Http404
    

    similares = Clasificado.objects.filter(tipologia=tipologia).exclude(pk=pk)[:3]
    print(similares)

    # clasificados = Propiedad.objects.all()
    # myFilter = PropiedadFilter(request.GET, queryset=clasificados)
    # clasificados = myFilter.qs

    if request.method == 'POST':
        form = ClasificadoForm(request.POST)
        
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
            return render(request, 'index.html', {})
        else:
            faqs = Faqs.objects.all()
            return render(request, 'venta.html', {"faqs": faqs})
    else:
        form = ClasificadoForm()
        
        ctx = {
            'clasificado': clasificado,
            'similares': similares,
            'form': form,
            # 'myFilter': myFilter,
        }

        return render(request, 'clasificado.html', ctx)

