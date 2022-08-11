from django.views.generic import *
from django.views import *

from typing import *
from callrequest.models import ClientActivitySphere

from services.custom_view import ExtraContext


class IndexPage(ExtraContext, TemplateView):
    template_name = 'pages/index.html'


class ContactsPage(ExtraContext, TemplateView):
    template_name = 'pages/contacts.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['activities'] = ClientActivitySphere.objects.all()


class AboutPage(ExtraContext, TemplateView):
    template_name = 'pages/about-us.html'

