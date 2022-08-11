from django.views.generic import *
from django.views import *

from .custom_view import ExtraContext
from .models import *

class ServiceView(ExtraContext,TemplateView):
    template_name = 'pages/services.html'


class ServiceDetail(ExtraContext,DetailView):
    template_name = 'pages/specific-service.html'
    model = Service

    