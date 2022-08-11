from django.contrib import admin
from .models import CallRequest, CallRequestComment, CallRequestStatus, ClientActivitySphere

class CommentsInline(admin.StackedInline):
    extra = 1
    model = CallRequestComment

admin.site.register(CallRequestStatus)
admin.site.register(ClientActivitySphere)


@admin.register(CallRequest)
class RequestAdmin(admin.ModelAdmin):
    inlines = [CommentsInline,]
    list_display = ['__str__', 'status']
    readonly_fields = ('name', 'phone')

