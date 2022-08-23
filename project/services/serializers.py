from rest_framework.serializers import ModelSerializer

from .models import Service, ServiceCategory


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'