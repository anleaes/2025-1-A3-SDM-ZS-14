from rest_framework import serializers

from medicos.models import Medico


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all__"