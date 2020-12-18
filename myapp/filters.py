import django_filters
from .models import *


class PropiedadFilter(django_filters.FilterSet):

    class Meta:
        model = Clasificado
        fields = ['nombre', 'tipologia']