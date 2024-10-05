from django.contrib import admin
from .models import Opera, Singer


class SingerInline(admin.TabularInline):
    model = Singer
    extra = 1
    fields = ['name', 'voice', 'opera']
    readonly_fields = ['opera']


class OperaAdmin(admin.ModelAdmin):
    inlines = [SingerInline]
    list_display = ['title']


admin.site.register(Opera, OperaAdmin)
