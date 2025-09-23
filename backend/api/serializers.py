from rest_framework import serializers
from .models import costumer

class CostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = costumer
        fields = '__all__'