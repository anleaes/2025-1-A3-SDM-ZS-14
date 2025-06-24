from django.shortcuts import render
from rest_framework import viewsets

from campanha_vacinal_vacina.models import CampanhaVacinalVacina
from campanha_vacinal_vacina.serializers import CampanhaVacinalVacinaSerializer

class CampanhaVacinalVacinaViewSet(viewsets.ModelViewSet):
    queryset = CampanhaVacinalVacina.objects.all()
    serializer_class = CampanhaVacinalVacinaSerializer