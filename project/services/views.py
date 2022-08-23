from django.http import Http404, response
from rest_framework.generics import ListAPIView

from .serializers import ServiceSerializer
from .models import *


class ServiceView(ListAPIView):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()


class ServiceDetail(ListAPIView):
    serializer_class = ServiceSerializer

    def get_object(self, slug):
        try:
            return Service.objects.get(slug=slug)
        except Service.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        obj = self.get_object(slug)
        serializer_class = ServiceSerializer(obj)
        return response(serializer_class.data)


    