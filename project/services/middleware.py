

from django.http import HttpResponse
from .models import *

class ExtraContextMiddleware:

    
    def __init__(self, get_response):
        self.get_response = get_response
        self.extra_context = {
        'categories' : ServiceCategory.objects.all(),
        'services' : Service.objects.all(),
        }
        self.exclude = []

    def __call__(self, request):

        response: HttpResponse = self.get_response(request)
        response.context.update(
            {k: v for k,v in self.extra_context.values() if k not in self.exclude})
        return response