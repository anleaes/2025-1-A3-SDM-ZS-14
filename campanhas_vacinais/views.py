from django.shortcuts import render

from rest_framework import viewsets

from campanhas_vacinais.models import CampanhaVacinal
from campanhas_vacinais.serializers import CamapanhaVacinalSerializer

class CampanhaVacinalViewSet(viewsets.ModelViewSet):
    queryset = CampanhaVacinal.objects.all()
    serializer_class = CamapanhaVacinalSerializer
