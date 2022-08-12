from django.views.generic import *
from django.views import *


from .models import *
from .custom import get_safe_slice

class NewsPage(ListView):
    template_name = 'pages/news.html'
    paginate_by = 9
    model = NewsArticle
    queryset = model.get_published()


class NewsDetail(DetailView):
    template_name = 'pages/news-post.html'
    model = NewsArticle
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context ['last_posts'] = get_safe_slice(NewsArticle.get_published().order_by('-publish_date'), 8)
        return context
