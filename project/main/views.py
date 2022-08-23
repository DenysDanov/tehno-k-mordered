from rest_framework.generics import ListAPIView

from .serializers import PreferenceSerializer
from .models import MyPreferences


class PreferencesList(ListAPIView):
    queryset = MyPreferences.objects.all()[0]
    serializer_class = PreferenceSerializer


