from rest_framework import viewsets
from .models import Integration
from .serializers import IntegrationSerializer


class IntegrationViewSet(viewsets.ModelViewSet):
    """
    Created IntegrationViewSet to return details to all integrations
    """
    queryset = Integration.objects.all()
    serializer_class = IntegrationSerializer
