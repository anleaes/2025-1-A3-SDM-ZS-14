from rest_framework import serializers

from campanha_vacinal_vacina.models import CampanhaVacinalVacina

class CampanhaVacinalVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampanhaVacinalVacina
        fields = '__all__'