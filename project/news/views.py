from django.http import Http404, response
from rest_framework.generics import ListAPIView

from .paginator import NewsPaginator
from .serializers import NewsSerializer
from .models import *
from .custom import get_safe_slice


class NewsPage(ListAPIView):
    serializer_class = NewsSerializer
    queryset = NewsArticle.get_published()
    pagination_class = NewsPaginator

class NewsDetail(ListAPIView):
    serializer_class = NewsSerializer

    def get_object(self, slug):
        try:
            return NewsArticle.objects.get(slug=slug)
        except NewsArticle.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        snippet = self.get_object(slug=slug)
        serializer = NewsSerializer(snippet)
        return response(serializer.data)

