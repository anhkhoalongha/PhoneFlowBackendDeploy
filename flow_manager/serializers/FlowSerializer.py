from rest_framework import serializers
from ..models import FLow

class FLowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FLow
        fields = '__all__'