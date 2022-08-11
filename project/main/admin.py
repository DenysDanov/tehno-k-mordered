from django.contrib import admin
from django.http import HttpRequest

from preferences.admin import PreferencesAdmin
from .models import *

class ImageInline(admin.StackedInline):
    model = MainPageImages
    extra = 1
    max_num = 6
    min_num = 1

class OurClientsInline(admin.StackedInline):
    model = OurClients
    extra = 3
    min_num = 4

class LoansForAnyPurposeServiceInline(admin.StackedInline):
    model = LoansForAnyPurposeService
    extra = 1
    min_num = 1
    max_num = 4


@admin.register(MyPreferences)
class CustomPreferencesAdmin(PreferencesAdmin):
    inlines = [ImageInline, OurClientsInline, LoansForAnyPurposeServiceInline,]

    fieldsets = (
        ('Контакты', {'fields': ('contact_email','contact_phone','contact_address')}),
        ('Соц. сети', {'fields': ('social_linkedin','social_tg','social_fb','social_behance','social_vk','social_skype','social_ig',)}),
        (None, {'fields' : ('about_company',)}),
        ('Сео блок', {'fields' : ('seo_block_title','seo_block_text','seo_block_image',)})
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False