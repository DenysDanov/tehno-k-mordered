from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

from typing import *


class NewsArticle(models.Model):
    
    # publish block
    author = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    is_published = models.BooleanField(_("Опубликовано"), default=False)
    publish_date = models.DateTimeField(_("Дата публикации"), blank=True, null=True)
    
    # content block
    title = models.CharField(_('Заголовок'), max_length=200)
    descr = models.TextField(_('Описание'))
    image = models.ImageField(_('Изображение'), upload_to='main/news/news-images/')

    introduction = models.TextField(_('Вступительная часть'), blank=True)
    conclusion = models.TextField(_('Заключение'), blank=True)

    # technical block
    slug = models.SlugField(_('slug'))

    def publish(self):
        self.is_published = True
        self.publish_date = datetime.now()
        self.save()
    
    def hide(self):
        self.is_published = False
        self.publish_date = None
        self.save()
    
    @classmethod
    def get_published(cls):
        return cls.objects.filter(is_published=True).order_by('-publish_date')
    

class NewsSubtitle(models.Model):
    article = models.ForeignKey(to=NewsArticle, on_delete=models.CASCADE, related_name='subtitles')
    subtitle = models.CharField(_('Подзаголовок'), max_length=250)
    text = models.TextField(_('Текст подзаголовка(в html формате)'))
    

