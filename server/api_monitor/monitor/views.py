from rest_framework import viewsets
from .models import Integration
from .models import APISpec
from .serializers import IntegrationSerializer, ApiSpecSerializer


class IntegrationViewSet(viewsets.ModelViewSet):
    """
    Created IntegrationViewSet to return details to all integrations
    """
    queryset = Integration.objects.all()
    serializer_class = IntegrationSerializer

class APISpecViewSet(viewsets.ReadOnlyModelViewSet): 
    queryset = APISpec.objects.all()
    serializer_class = ApiSpecSerializer
