from rest_framework import viewsets
from .models import AplicacaoVacina
from .serializers import AplicacaoVacinaSerializer

class AplicacaoVacinaViewSet(viewsets.ModelViewSet):
    queryset = AplicacaoVacina.objects.all()
    serializer_class = AplicacaoVacinaSerializer