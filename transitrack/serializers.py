from rest_framework import serializers
from .models import Ruta, Conductor

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class RutaSerializer(serializers.ModelSerializer):
    conductor = ConductorSerializer(read_only=True)  
    conductor_id = serializers.PrimaryKeyRelatedField(
        queryset=Conductor.objects.all(), source='conductor', write_only=True
    )

    class Meta:
        model = Ruta
        fields = ['id', 'origen', 'destino', 'horario', 'conductor', 'conductor_id']
