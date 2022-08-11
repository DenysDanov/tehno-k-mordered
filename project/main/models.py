from django.db import models
from preferences.models import Preferences
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


class MyPreferences(Preferences):

    # contacts 
    contact_email = models.EmailField(_('E-Mail: '))
    contact_phone = models.CharField(_('Номер телефона'), max_length=16)
    contact_address = models.CharField(_('Адресс офиса'), max_length=200)

    # social media

    social_linkedin = models.URLField(_('LinkedIn'))
    social_tg = models.URLField(_('Telegram'))
    social_fb = models.URLField(_('Facebook'))
    social_behance = models.URLField(_('Behance'))
    social_vk = models.URLField(_('VK'))
    social_skype = models.URLField(_('Skype'))
    social_ig = models.URLField(_('Инстаграм'))

    about_company = models.TextField(_('О компании'))

    # SEO
    seo_block_title = models.CharField(_('Заголовок'), max_length=100)
    seo_block_text = models.TextField(_('Текст'))
    seo_block_image = models.ImageField(_('Изображение'), upload_to='main/index/seo/')

    class Meta:

        verbose_name = _('Настройки')
        verbose_name_plural = _('Настройки')
    

class LoansForAnyPurposeService(models.Model):

    preferences = models.ForeignKey(to=MyPreferences, on_delete=models.CASCADE, related_name='loan_purpose')
    title = models.CharField(_('Заголовок'), max_length=300)
    image = models.ImageField(_('Изображение'), upload_to='main/index/loans/')
    text = models.TextField(_('Текст'))

    class Meta:

        verbose_name = _('Секция "Кредиты на любые цели"')
        verbose_name_plural = _('Секции "Кредиты на любые цели"')


class OurClients(models.Model):
    preferences = models.ForeignKey(to=MyPreferences, on_delete=models.CASCADE, related_name='clients')
    name = models.CharField(_('Название компании клиента'), max_length=100)
    descr = models.TextField(_('Описание'))
    rating = models.IntegerField(_('Оценка (1-5)'),default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])

    class Meta:

        verbose_name = _('Секция "Наши клиенты"')
        verbose_name_plural = _('Секции "Наши клиенты"')


class MainPageImages(models.Model):
    main_image = models.ImageField(_('Изображение на главной странице'), upload_to='main/index/main/')
    preferences = models.ForeignKey(to=MyPreferences, on_delete=models.CASCADE, related_name='main_images')
    
    class Meta:

        verbose_name = _('Изображение для главной страницы')
        verbose_name_plural = _('Изображения для главной страницы')