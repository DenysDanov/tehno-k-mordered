from django.utils.translation import ngettext

from django.contrib import admin, messages
from .models import *





class SubtitlesInline(admin.StackedInline):
    model = NewsSubtitle
    extra = 1


@admin.register(NewsArticle)
class ArticleAdmin(admin.ModelAdmin):
    
    inlines = [SubtitlesInline, ]
    exclude = ['is_published']
    readonly_fields = ('author', 'publish_date')
    list_display = ['title', 'is_published']
    actions = ['publish']

    def save_model(self, request: Any, obj, form: Any, change: Any) -> None:
        obj.author = request.user
        
        return super().save_model(request, obj, form, change)
    
    @admin.action(description='Mark selected stories as published')
    def publish(self, request, queryset):
        updated = [article.publish() for article in queryset]
        self.message_user(request, ngettext(
            '%d story was successfully marked as published.',
            '%d stories were successfully marked as published.',
            len(updated),
        ) % len(updated), messages.SUCCESS)
