from django.forms import *
from .models import *
from django.utils.translation import gettext as _

class ServiceForm(ModelForm):
    
    # how it works block
    hiw_text_block = models.CharField(_('Краткий блок'), max_length=256)
    hiw_text_yellow_block = models.CharField(_('Краткий блок'), max_length=256)
    hiw_text_big_block = models.TextField(_('Большой блок'))
    hiw_youtube_video_link = models.URLField(_('Ссылка на видео с Youtube'))

    # Important block
    imp_title = models.CharField(_('Заголовок'), max_length=100)
    imp_image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    imp_text = models.TextField(_('Текст'))

    # tabs section block
    tab_1_title = models.CharField(_('Заголовок'), max_length=100)
    tab_1_image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    tab_1_text = models.TextField(_('Текст'))

    tab_2_title = models.CharField(_('Заголовок'), max_length=100)
    tab_2_image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    tab_2_text = models.TextField(_('Текст'))

    tab_3_title = models.CharField(_('Заголовок'), max_length=100)
    tab_3_image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    tab_3_text = models.TextField(_('Текст'))

    tab_4_title = models.CharField(_('Заголовок'), max_length=100)
    tab_4_image = models.ImageField(_('Изображение'), upload_to='main/service/important/')
    tab_4_text = models.TextField(_('Текст'))

    # what we do block
    wwd_text_main = models.TextField(_('Главный текст'))
    wwd_text_second = models.TextField(_('Второй текст'))

    # ul units for what we do block
    ul_1 = models.CharField(_('Текст'), max_length=100)
    ul_2 = models.CharField(_('Текст'), max_length=100)
    ul_3 = models.CharField(_('Текст'), max_length=100)
    # ol units for what we do block
    ol_1 = models.CharField(_('Текст'), max_length=100)
    ol_2 = models.CharField(_('Текст'), max_length=100)
    ol_3 = models.CharField(_('Текст'), max_length=100)

    def save(self, commit: bool = ...):
        service = super().save(commit)
        HowServiceWorksInfo.create(
            service = service,
            text_block = self.cleaned_data['hiw_text_block'],

        )

    class Meta:
        model = Service
        fields = '__all__'


