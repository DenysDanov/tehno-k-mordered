from rest_framework.serializers import ModelSerializer

from .models import ClientActivitySphere

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = ClientActivitySphere
        fields = '__all__'
