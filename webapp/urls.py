from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS

    path('power/', admin.site.urls),
    path("auth/", include("myauth.urls")),
    path("", include("basic.urls")),
]
