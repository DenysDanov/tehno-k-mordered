from django.urls import path

from .views import *


app_name = 'callrequest'
urlpatterns = [
    path('', SendCallRequest.as_view(), name='request'),
    path('activities/', ActivityList.as_view(), name='activities')
]