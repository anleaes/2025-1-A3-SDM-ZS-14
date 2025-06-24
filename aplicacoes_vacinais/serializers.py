from rest_framework import serializers

from aplicacoes_vacinais.models import AplicacaoVacina


class AplicacaoVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AplicacaoVacina
        fields = '__all__'