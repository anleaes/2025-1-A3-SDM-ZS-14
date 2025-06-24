from django.shortcuts import render
from rest_framework import viewsets

from vacinas.models import Vacina
from vacinas.serializers import VacinaSerializer


class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer
