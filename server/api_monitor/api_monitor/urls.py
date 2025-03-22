"""
URL configuration for api_monitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from monitor.views import APISpecViewSet, IntegrationViewSet

router = DefaultRouter()
router.register(r'api/integrations', IntegrationViewSet)
router.register(r'api/apispec', APISpecViewSet, basename='apispec')

urlpatterns = [
    path('', include(router.urls)),
    path('api/integration/<int:pk>/update/', IntegrationViewSet.as_view({'put': 'update'}), name='integration-update'),
]
