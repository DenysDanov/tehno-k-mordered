from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
    path('preferences/', PreferencesList.as_view(), name='preferences')
]