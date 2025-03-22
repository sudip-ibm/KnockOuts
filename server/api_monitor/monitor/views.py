from rest_framework import viewsets
from .models import Integration
from monitor.models import APISpec
from .serializers import IntegrationSerializer
from .serializers import APISpecSerializer

class IntegrationViewSet(viewsets.ModelViewSet):
    """
    Created IntegrationViewSet to return details to all integrations
    """
    queryset = Integration.objects.all()
    serializer_class = IntegrationSerializer

class APISpecViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = APISpec.objects.all()
    serializer_class = APISpecSerializer
