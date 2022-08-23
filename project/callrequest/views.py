from django.http import HttpRequest
from django.utils.translation import gettext as _
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from .responses import *
from .custom import validate_phone_number, validate_request
from .models import CallRequest, CallRequestStatus, ClientActivitySphere
from .serializer import ActivitySerializer


class SendCallRequest(APIView):
    def post(self, request: HttpRequest, *args, **kwargs):
        if not validate_request(request.POST, 'name', 'ph'):
            return APIResponse400(_(f'There`re no name or phone'))

        name = request.POST.get('name')
        phone = request.POST.get('ph')

        if not validate_phone_number(phone): 
            return APIResponse400(_(f'Bad phone number\n{phone=}'))
        
        if validate_request(request.POST, 'activity','request-textarea'):
            CallRequest.objects.create(
                name = name,
                phone = phone,
                status = CallRequestStatus.objects.get(pk=1),
                activity = ClientActivitySphere.objects.get(request.POST.get('activity')),
                textarea = request.POST.get('request-textarea')
            ).save()
            return APIResponse201('')


        cr = CallRequest.objects.create(
            name=name,
            phone=phone,
            status=CallRequestStatus.objects.get(pk=1)
        ).save()
        return APIResponse201('')


class ActivityList(ListAPIView):
    serializer_class = ActivitySerializer
    queryset = ClientActivitySphere.objects.all()