from django.urls import include, path
from .views import *



urlpatterns = [
    path('', index, name='home'),
    path('venta/', venta, name='venta'),
    path('contacto/', contacto, name='contacto'),
    path('clasificados/', clasificados, name='clasificados'),
    path('portal/', portal, name='portal'),
    path('portal/<int:pk>/', portal_detail, name='portal_detail'),
] 