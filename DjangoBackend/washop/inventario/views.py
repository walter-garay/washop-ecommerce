from django.shortcuts import render
from rest_framework import viewsets
from inventario import serializers, models

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer


