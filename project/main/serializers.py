from rest_framework.serializers import ModelSerializer

from .models import MyPreferences

class PreferenceSerializer(ModelSerializer):
    class Meta:
        model = MyPreferences
        fields = '__all__'