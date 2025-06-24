from rest_framework import serializers

from campanhas_vacinais.models import CampanhaVacinal
from vacinas.models import Vacina

class CamapanhaVacinalSerializer(serializers.ModelSerializer):
    vacinas = serializers.PrimaryKeyRelatedField(
        many = True,
        queryset= Vacina.objects.all()
    )

    class Meta:
        model = CampanhaVacinal
        fields = "__all__"