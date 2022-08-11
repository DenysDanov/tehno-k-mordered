from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import *
from django.views import *
from django.utils.translation import gettext as _

from .custom import validate_phone_number, validate_request
from .models import CallRequest, CallRequestStatus, ClientActivitySphere


class SendCallRequest(View):
    def post(self, request: HttpRequest, *args, **kwargs):
        if not validate_request(request.POST, 'name', 'ph'):
            return HttpResponseBadRequest(_(f'There`re no name or phone'))

        name = request.POST.get('name')
        phone = request.POST.get('ph')

        if not validate_phone_number(phone): 
            return HttpResponseBadRequest(_(f'Bad phone number\n{phone=}'))
        
        if validate_request(request.POST, 'activity','request-textarea'):
            activity, textarea = request.POST.get('activity'), request.POST.get('request-textarea')
            CallRequest.objects.create(
                name = name,
                phone = phone,
                status = CallRequestStatus.objects.get(pk=1),
                activity = ClientActivitySphere.objects.get(activity),
                textarea = textarea
            ).save()
            return HttpResponse('')


        cr = CallRequest.objects.create(
            name=name,
            phone=phone,
            status=CallRequestStatus.objects.get(pk=1)
        ).save()
        return HttpResponse('')