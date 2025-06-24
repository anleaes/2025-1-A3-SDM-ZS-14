from django.shortcuts import render

from rest_framework import viewsets
from estoques_vacina.models import EstoqueVacina
from estoques_vacina.serializers import EstoqueVacinaSerializer