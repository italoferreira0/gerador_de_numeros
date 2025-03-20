from rest_framework import serializers
from .models import NumerosGerados

class NumerosGeradosSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumerosGerados
        fields = '__all__'
