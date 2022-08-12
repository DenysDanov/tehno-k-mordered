from django.http import HttpRequest

from typing import Any, Dict
from re import search

from django.urls import reverse

from .models import Service, ServiceCategory

def decode_path(request: HttpRequest) -> list:
    path = request.path_info
    decoder = {
        r'^\/' : {'name': 'Главная', 'url': reverse('main:index')},
        r'^\/news\/' : {'name': 'Новости', 'url': reverse('news:index')},
        r'^\/services\/' : {'name': 'Услуги', 'url': reverse('services:index')},
        r'^\/about\-us\/$' : {'name': 'О нас', 'url': reverse('main:about')},
        r'^\/contacts\/$' : {'name': 'Контакты', 'url': reverse('main:contacts')},
        r'^\/news\/\D+' : {'name': 'Новость', 'url': ''},
        r'^\/services\/\D+' : {'name': 'Услуга', 'url': ''}
    }
    return [v for k,v in decoder.items() if search(k, path)]
    


class ExtraContext:
    
    def get_context_data(self,**kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        context['categories'] = ServiceCategory.objects.all()
        context['top_section_units'] = decode_path(self.request)
        return context
