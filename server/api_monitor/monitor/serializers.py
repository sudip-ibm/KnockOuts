from rest_framework import serializers
from .models import Integration


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = '__all__'
        
class APISpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = APISpec
        fields = '__all__'
