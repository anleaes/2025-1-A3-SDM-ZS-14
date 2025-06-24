from rest_framework import serializers

from estoques_vacina.models import EstoqueVacina

class EstoqueVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueVacina
        fields = "__all__"