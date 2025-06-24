from django.shortcuts import render
from rest_framework import viewsets

from unidades_saude.models import UnidadeSaude
from unidades_saude.serializers import UnidadeSaudeSerializer

class UnidadeSaudeViewSet(viewsets.ModelViewSet):
    queryset = UnidadeSaude.objects.all()
    serializer_class = UnidadeSaudeSerializer