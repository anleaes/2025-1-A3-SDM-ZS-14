from django.shortcuts import render

from rest_framework import viewsets
from estoques_vacina.models import EstoqueVacina
from estoques_vacina.serializers import EstoqueVacinaSerializer

class EstoqueVacinaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueVacina.objects.all()
    serializer_class = EstoqueVacinaSerializer
