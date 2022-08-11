from django.contrib import admin

from .models import *

class HowServiceWorksInline(admin.StackedInline):
    model = HowServiceWorksInfo
    extra = 1
    max_num = 1

class ImportantInline(admin.StackedInline):
    model = ServiceImportantInfo
    extra = 1
    max_num = 4
    min_nim = 1

class TabsSectionInline(admin.StackedInline):
    model = TabsSectionInfo
    extra = 4
    max_num = 4
    min_nim = 1

class WhatWeDoInline(admin.StackedInline):
    model = WhatWeDoInfo
    extra = 1
    max_num = 1
    min_nim = 1

class WhatWeDoUlInline(admin.StackedInline):
    model = WhatWeDoUlUnits
    extra = 3

class WhatWeDoOlInline(admin.StackedInline):
    model = WhatWeDoOlUnits
    extra = 3

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [
        HowServiceWorksInline,
        ImportantInline,
        TabsSectionInline,
        WhatWeDoInline,
        WhatWeDoUlInline,
        WhatWeDoOlInline,
        ]

admin.site.register(ServiceCategory)