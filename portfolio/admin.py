from django.contrib import admin
from .models import *


class FilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'file')
    list_display_links = ('title', )
    search_fields = ('title', 'description')
    list_filter = ('time_create', 'theme_id')


class ThemesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'is_published')
    list_display_links = ('name', )
    search_fields = ('name', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Files, FilesAdmin)
admin.site.register(Themes, ThemesAdmin)

