from django.views.generic import *
from django.views import *

from .models import *

class ServiceView(TemplateView):
    template_name = 'pages/services.html'


class ServiceDetail(DetailView):
    template_name = 'pages/specific-service.html'
    model = Service

    