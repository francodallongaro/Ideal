from django.contrib import admin
from hello.models import *

# Register your models here.


class FaqsAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'categoria',)
    list_filter = ('categoria',)
    search_fields = ('pregunta', 'respuesta',)


class InLineFoto(admin.TabularInline):
    model = Foto

class ClasificadoAdmin(admin.ModelAdmin):
    # inlines = [InLineFoto, InLinePlano]
    inlines = [InLineFoto]
    list_display = ('nombre', 'tipologia',)
    list_filter = ('tipologia',)
    search_fields = ('nombre', 'tipologia',)

    fieldsets = (
        (None, {
            "fields": (
                'verificada',
                'destacada',
                'vendedor',
                'pack'
            ),
        }),
        ('INFORMACIÓN', {
            "fields": (
                'nombre',
                'tipologia',
                'visita',
                'youtube',
                'tour',
                'descripcion'
            ),
        }),
        ('PORTALES', {
            'classes': ('wide',),
            "fields": (
                ('zonaprop',
                'properati',
                'argenprop',
                'mercadolibre',
                'reporteinmobiliario'),
            ),
        }),
        ('UBICACIÓN', {
            'classes': ('wide',),
            "fields": (
                ('direccion',
                'barrio',
                'cp'),
            ),
        }),
        ('COSTOS', {
            'classes': ('wide',),
            "fields": (
                ('costo',
                'moneda_costo',
                'expensas',
                'moneda_expensas'),
            ),
        }),
        ('INFORMACIÓN', {
            'classes': ('wide',),
            "fields": (
                ('m2_totales',
                'm2_cubiertos',
                'piso',
                'depto',
                'ambientes',
                'dormitorios',
                'banios',
                'orientacion',
                'cocheras',
                'balcones'),
            ),
        }),
        ('AMENITIES', {
            'classes': ('wide',),
            "fields": (
                ('pileta',
                'gimnasio',
                'juegos',
                'solarium',
                'microcine',
                'parrilla',
                'salon_usos_multiples',
                'laundry'),
            ),
        }),
        ('SERVICIOS', {
            'classes': ('wide',),
            "fields": (
                ('seguridad',
                'aire_acondicionado',
                'internet',
                'cable'),
            ),
        }),
        ('EDIFICIO', {
            'classes': ('wide',),
            "fields": (
                ('cant_de_pisos',
                'disposicion',
                'antiguedad',
                'depto_por_piso'),
            ),
        }),
    )

admin.site.register(Usuario)
admin.site.register(Faqs, FaqsAdmin)
admin.site.register(Pack)
admin.site.register(Clasificado, ClasificadoAdmin)