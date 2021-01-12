from django.db import models
from django.urls import reverse



# PLANES
"""
Planes que aparecen en la pagina: COMPLETAR
Esta formado por: nombre, precio, descripcion.
"""
class Pack(models.Model):

    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=10)
    valuacion_propiedad = models.BooleanField(default=False)
    foto = models.BooleanField(default=False)
    tour = models.BooleanField(default=False)
    redaccion = models.BooleanField(default=False)
    publicacion = models.BooleanField(default=False)
    destacado = models.BooleanField(default=False)
    cartel = models.BooleanField(default=False)
    secretario = models.BooleanField(default=False)
    visitas = models.BooleanField(default=False)
    ficha_tecnica = models.BooleanField(default=False)
    soporte_post_venta = models.BooleanField(default=False)
    experto = models.BooleanField(default=False)
    reportes_semanales = models.BooleanField(default=False)
    visitas_acompanadas = models.BooleanField(default=False)
    estudio_titulos = models.BooleanField(default=False)
    gestion_online = models.BooleanField(default=False)
    ambientacion = models.BooleanField(default=False)

    borradores = models.BooleanField(default=False)
    asesoramiento_legal = models.BooleanField(default=False)

    financiacion = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Pack")
        verbose_name_plural = ("Packs")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Pack_detail", kwargs={"pk": self.pk})


    # USUARIOS
"""
Contacto, para crear form que aparece en la pagina: COMPLETAR
Esta formado por: nombre, tel, email.
"""

# TIPO
COMPRAVENTA_CHOICES = (
    ('Vendedor', 'Vendedor'),
    ('Comprador', 'Comprador'),
    ('Ambas', 'Ambas')
)

class Usuario(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50, blank=True)
    
    estado = models.CharField(
        choices=COMPRAVENTA_CHOICES,
        default='Vendedor',
        max_length=50)

    testimonio = models.CharField(max_length=50, blank=True)

    tel = models.IntegerField()
    email = models.EmailField(max_length=254)


    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)

    def get_absolute_url(self):
        return reverse("Contacto_detail", kwargs={"pk": self.pk})




# LISTADO DE TODOS LOS BARRIOS DE CABA
BARRIOS_CHOICES = (
    ('Agronomía', 'Agronomía'),
    ('Almagro', 'Almagro'),
    ('Balvanera', 'Balvanera'),
    ('Barracas', 'Barracas'),
    ('Belgrano', 'Belgrano'),
    ('Boedo', 'Boedo'),
    ('Caballito', 'Caballito'),
    ('Chacarita', 'Chacarita'),
    ('Coghlan', 'Coghlan'),
    ('Colegiales', 'Colegiales'),
    ('Constitucion', 'Constitucion'),
    ('Flores', 'Flores'),
    ('Floresta', 'Floresta'),
    ('La Boca', 'La Boca'),
    ('La Paternal', 'La Paternal'),
    ('Liniers', 'Liniers'),
    ('Mataderos', 'Mataderos'),
    ('Monte Castro', 'Monte Castro'),
    ('Monserrat', 'Monserrat'),
    ('Nueva Pompeya', 'Nueva Pompeya'),
    ('Núñez', 'Núñez'),
    ('Palermo', 'Palermo'),
    ('Parque Avellaneda', 'Parque Avellaneda'),
    ('Parque Chacabuco', 'Parque Chacabuco'),
    ('Parque Chas', 'Parque Chas'),
    ('Parque Patricios', 'Parque Patricios'),
    ('Puerto Madero', 'Puerto Madero'),
    ('Recoleta', 'Recoleta'),
    ('Retiro', 'Retiro'),
    ('Saavedra', 'Saavedra'),
    ('San Cristóbal', 'San Cristóbal'),
    ('San Nicolás', 'San Nicolás'),
    ('San Telmo', 'San Telmo'),
    ('Vélez Sárfield', 'Vélez Sárfield'),
    ('Versalles', 'Versalles'),
    ('Villa Crespo', 'Villa Crespo'),
    ('Villa del Parque', 'Villa del Parque'),
    ('Villa Devoto', 'Villa Devoto'),
    ('Villa General Mitre', 'Villa General Mitre'),
    ('Villa Lugano', 'Villa Lugano'),
    ('Villa Luro', 'Villa Luro'),
    ('Villa Ortúzar', 'Villa Ortúzar'),
    ('Villa Pueyrredón', 'Villa Pueyrredón'),
    ('Villa Real', 'Villa Real'),
    ('Villa Riachuelo', 'Villa Riachuelo'),
    ('Villa Santa Rita', 'Villa Santa Rita'),
    ('Villa Soldati', 'Villa Soldati'),
    ('Villa Urquiza', 'Villa Urquiza')
)

# OPCIONES PARA LAS ORIENTACIONES
ORIENTACION_CHOICES = (
    ('Norte', 'Norte'),
    ('Noreste', 'Noreste'),
    ('Este', 'Este'),
    ('Sudeste', 'Sudeste'),
    ('Sur', 'Sur'),
    ('Sudoeste', 'Sudoeste'),
    ('Oeste', 'Oeste'),
    ('Noroeste', 'Noroeste'),
)

# OPCIONES DE MONEDAS
MONEDAS_CHOICES = (
    ('$', '$'),
    ('USD', 'USD'),
)

# TIPOLOGIAS
TIPOLOGIA_CHOICES = (
    ('Departamento', 'Departamento'),
    ('Casa', 'Casa'),
    ('Casa Country', 'Casa Country'),
    ('PH', 'PH')
)

# CONDICION
CATEGORIA_CHOICES = (
    ('En Venta', 'En Venta'),
    ('Alquiler', 'Alquiler')
)

# SERVICIOS
SERVICIOS_CHOICES = (
    ('-', '-'),
    ('Fibertel', 'Fibertel'),
    ('Arnet', 'Arnet'),
    ('Telecentro', 'Telecentro'),
    ('Cablevision', 'Cablevision'),
    ('DirecTV', 'DirecTV')
)

# DEPARTAMENTOS LETRAS
DEPTO_CHOICES = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E'),
    ('F', 'F'),
    ('G', 'G'),
    ('H', 'H'),
)

# NUMEROS PARA CANTIDADES
NUM_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ('13', '13'),
    ('14', '14'),
    ('15', '15'),
    ('16', '16'),
    ('17', '17'),
    ('18', '18'),
    ('19', '19'),
    ('20', '20'),
    ('21', '21')
)


class Clasificado(models.Model):

    destacada = models.BooleanField(default=False, blank=True)
    verificada = models.BooleanField(default=False, blank=True)

    creacion = models.DateTimeField(auto_now_add=True)

    pack = models.ForeignKey(Pack, related_name='pack', on_delete=models.SET_NULL, default=None, null=True)

    vendedor = models.ForeignKey(Usuario, related_name='usuario', on_delete=models.SET_NULL, default=None, null=True)

    tipologia = models.CharField(
        choices=TIPOLOGIA_CHOICES,
        default='Departamento',
        max_length=50)

    nombre = models.CharField(max_length=50, blank=True)
    descripcion = models.TextField(blank=True)
    
    zonaprop = models.BooleanField(default=False)
    properati = models.BooleanField(default=False)
    argenprop = models.BooleanField(default=False)
    mercadolibre = models.BooleanField(default=False)
    reporteinmobiliario = models.BooleanField(default=False)
    direccion = models.CharField(max_length=50, blank=True)

    barrio = models.CharField(
        choices=BARRIOS_CHOICES,
        default='Agronomía',
        max_length=50)

    cp = models.IntegerField(blank=True, default=0)

    costo = models.IntegerField(blank=True, default=0)
    moneda_costo = models.CharField(
        choices=MONEDAS_CHOICES,
        default='USD',
        max_length=50)

    expensas = models.IntegerField(blank=True, default=0)
    moneda_expensas = models.CharField(
        choices=MONEDAS_CHOICES,
        default='$',
        max_length=50)

    luz = models.IntegerField(blank=True, default=0)
    gas = models.IntegerField(blank=True, default=0)
    abl = models.IntegerField(blank=True, default=0)
    aysa = models.IntegerField(blank=True, default=0)
   

    # imagen_principal = models.ImageField(upload_to="", null=True, blank=True)

    m2_totales = models.IntegerField(blank=True, default=0)
    m2_cubiertos = models.IntegerField(blank=True, default=0)
    piso = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')
    depto = models.CharField(
        choices=DEPTO_CHOICES,
        max_length=50,
        default='A')
    ambientes = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')
    dormitorios = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')
    banios = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')
    orientacion = models.CharField(
        choices=ORIENTACION_CHOICES,
        default='Norte',
        max_length=50)
    antiguedad = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')
    cochera = models.BooleanField(default=False)
    cocheras = models.CharField(
        choices=NUM_CHOICES,
        max_length=10,
        default='1')

    baulera = models.BooleanField(default=False)

    pileta = models.BooleanField(default=False)
    gimnasio = models.BooleanField(default=False)
    juegos = models.BooleanField(default=False)
    solarium = models.BooleanField(default=False)
    microcine = models.BooleanField(default=False)
    parrilla = models.BooleanField(default=False)
    salon_usos_multiples = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)

    alarma = models.BooleanField(default=False)
    mascotas = models.BooleanField(default=False)
    aire_acondicionado = models.BooleanField(default=False)
    losa_radiante = models.BooleanField(default=False)
    
    internet = models.CharField(
        choices=SERVICIOS_CHOICES,
        max_length=50,
        default='-')
    cable = models.CharField(
        choices=SERVICIOS_CHOICES,
        max_length=50,
        default='-')

    class Meta:
        verbose_name = ("Clasificado")
        verbose_name_plural = ("Clasificados")

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Clasificado_detail", kwargs={"pk": self.pk})



# class Foto(models.Model):

#     propiedad = models.ForeignKey(Clasificado, on_delete=models.CASCADE, default=None)
#     imagen = models.ImageField(upload_to="propiedades/", null=True, blank=True)
#     nombre = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = ("Foto")
#         verbose_name_plural = ("Fotos")

#     def __str__(self):
#         return self.nombre

#     def get_absolute_url(self):
#         return reverse("Foto_detail", kwargs={"pk": self.pk})

# class Plano(models.Model):

#     propiedad = models.ForeignKey(Clasificado, on_delete=models.CASCADE, default=None)
#     imagen = models.ImageField(upload_to="planos/", null=True, blank=True)
#     nombre = models.CharField(max_length=50)

#     class Meta:
#         verbose_name = ("Plano")
#         verbose_name_plural = ("Planos")

#     def __str__(self):
#         return self.nombre

#     def get_absolute_url(self):
#         return reverse("Foto_detail", kwargs={"pk": self.pk})
