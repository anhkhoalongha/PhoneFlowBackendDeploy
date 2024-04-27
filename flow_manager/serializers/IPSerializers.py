from rest_framework import serializers
from ..models import IP

class IPSerializer(serializers.ModelSerializer):
    class Meta:
        model = IP
        fields = '__all__'