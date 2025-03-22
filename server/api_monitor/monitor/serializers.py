from rest_framework import serializers
from .models import ApiSpec, Integration


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integration
        fields = '__all__'

class APISpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiSpec
        fields = '__all__'
