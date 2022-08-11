from django.urls import path

from .views import *

app_name = 'news'
urlpatterns = [
    path('', NewsPage.as_view(), name='index'),
    path('<slug:slug>/', NewsDetail.as_view(), name='news-post')
]