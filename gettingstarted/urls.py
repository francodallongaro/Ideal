from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("venta/", hello.views.venta, name="venta"),
    path("contacto/", hello.views.contacto, name="contacto"),
    path("portal/", hello.views.portal, name="portal"),
    
    path("admin/", admin.site.urls),
]
