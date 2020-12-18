from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('myapp.urls')),
]



# ADMIN CUSTOM
admin.site.site_header = "IDEAL"
admin.site.index_title = "Administración"
admin.site.site_title = "IDEAL"