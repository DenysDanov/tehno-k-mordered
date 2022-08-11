from django.db import models
from django.utils.translation import gettext as _


class ServiceCategory(models.Model):
    ''' Модель категории услуг '''
    name = models.CharField(_('Название категории'), max_length=100)
    slug = models.SlugField(_('SLUG категории'), unique=True)
    descr = models.TextField(_('Описание категории'))

    class Meta:
        verbose_name = _('Категория услуги')
        verbose_name_plural = _('Категории услуги')


class Service(models.Model):
    ''' Модель услуги '''
    name = models.CharField(_('Название услуги'), max_length=100)
    slug = models.SlugField(_('SLUG услуги'), unique=True)
    category = models.ForeignKey(to=ServiceCategory, on_delete=models.DO_NOTHING, related_name="services")
    image = models.ImageField(_('Изображения для услуги'), upload_to='main/service/image/')
    descr = models.CharField(_('Описание услуги'), max_length=350)

    class Meta:
        verbose_name = _('Услуга')
        verbose_name_plural = _('Услуги')
    
class HowServiceWorksInfo(models.Model):
    ''' Информация для блока "Как работает?" '''
    service = models.OneToOneField(to=Service, related_name="how_it_works", on_delete=models.CASCADE)
    text_block = models.CharField(_('Краткий блок'), max_length=256)
    text_yellow_block = models.CharField(_('Краткий блок'), max_length=256)
    text_big_block = models.TextField(_('Большой блок'))
    youtube_video_link = models.URLField(_('Ссылка на видео с Youtube'))

    class Meta:
        verbose_name = _('Как работает?')
        

class ServiceImportantInfo(models.Model):
    ''' Информация для блока "Важное" '''
    service = models.ForeignKey(to=Service, related_name="important", on_delete=models.CASCADE)
    title = models.CharField(_('Заголовок'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    text = models.TextField(_('Текст'))
    

    class Meta:
        verbose_name = _('Важное')
        

class TabsSectionInfo(models.Model):
    ''' Инфромация для блока "tabs-section" '''
    # 4 to 1 as well
    title = models.CharField(_('Заголовок'), max_length=100)
    image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    col_1 = models.CharField(_('Колонка 1'), max_length=350)
    col_2 = models.CharField(_('Колонка 2'), max_length=350)
    col_3 = models.CharField(_('Колонка 3'), max_length=350)
    col_4 = models.CharField(_('Колонка 4'), max_length=350)
    service = models.ForeignKey(to=Service, related_name="tabs", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('tabs-section')
     

class WhatWeDoInfo(models.Model):
    ''' Информация для блока "Что мы делаем" '''
    text_main = models.TextField(_('Главный текст'))
    text_second = models.TextField(_('Второй текст'))
    service = models.OneToOneField(to=Service, related_name="whatwedo", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _('Что мы делаем')


class WhatWeDoUlUnits(models.Model):
    ''' Строки ul списка в блоке "Что мы делаем" '''
    info_block = models.ForeignKey(to=Service, related_name='ul', on_delete=models.CASCADE)
    text = models.CharField(_('Текст'), max_length=100)

class WhatWeDoOlUnits(models.Model):
    ''' Строки ol списка в блоке "Что мы делаем?" '''
    info_block = models.ForeignKey(to=Service, related_name='ol', on_delete=models.CASCADE)
    text = models.CharField(_('Текст'), max_length=100)
