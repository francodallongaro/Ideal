from django.contrib import admin
from .models import *


# class PackAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'precio', 'descripcion')


class InLineFoto(admin.TabularInline):
    model = Foto

class InLinePlano(admin.TabularInline):
    model = Plano


class ClasificadoAdmin(admin.ModelAdmin):
    inlines = [InLineFoto, InLinePlano]
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
                'imagen_principal',
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
                'moneda_expensas',
                'luz',
                'gas',
                'abl',
                'aysa'),
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
                'cochera',
                'cocheras',
                'baulera',
                'antiguedad'),
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
                ('alarma',
                'mascotas',
                'aire_acondicionado',
                'losa_radiante',
                'internet',
                'cable'),
            ),
        }),
    )
    

admin.site.register(Usuario)
admin.site.register(Pack)
# admin.site.register(Clasificado)
# admin.site.register(Pack, PackAdmin)
admin.site.register(Clasificado, ClasificadoAdmin)
admin.site.register(FAQ)
