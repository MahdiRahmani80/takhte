from django.contrib import admin
from django.urls import path 
from django.conf.urls import url , include


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'' , include('app.urls')) ,
    path('api-auth/', include('rest_framework.urls')),

    url(r"^api/", include('app.api.urls')),
   

]
