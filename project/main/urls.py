from django.urls import path

from .views import *

app_name = 'main'
urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('about-us/', AboutPage.as_view(), name='about'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
]