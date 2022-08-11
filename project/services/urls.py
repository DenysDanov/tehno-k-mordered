from django.urls import path

from .views import *

app_name = 'services'
urlpatterns = [
    path('', ServiceView.as_view(), name='index'),
    path('<slug:slug>/', ServiceDetail.as_view(), name='detail'),
]