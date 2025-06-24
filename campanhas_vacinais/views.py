from django.shortcuts import render

from rest_framework import viewsets

from campanhas_vacinais.models import CampanhaVacinal
from campanhas_vacinais.serializers import CamapanhaVacinalSerializer