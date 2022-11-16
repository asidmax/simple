from django.contrib import admin

from .models import Ss
from .models import Rubric


class SsAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'content', 'price', 'published',)
    list_display_links = ('title', 'content',)
    search_fields = ('title', 'content',)


admin.site.register(Ss, SsAdmin)
admin.site.register(Rubric)