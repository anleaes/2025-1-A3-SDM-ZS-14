from rest_framework import viewsets

from agendamentos.models import Agendamento
from agendamentos.serializers import AgendamentoSerializer


class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
