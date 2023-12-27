from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter
from inventario.views import *

from django.urls import path, include


router = DefaultRouter()

router.register('inventario', views.UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('', RedirectView.as_view(url='api/v1/'))
]
